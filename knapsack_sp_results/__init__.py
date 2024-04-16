import random
from otree.database import db
from otree.api import (
    BasePlayer,
    BaseGroup,
    BaseSubsession,
    BaseConstants,
    Page,
    models,
    widgets,
)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    charity_choice = models.StringField(
        choices=[
            ["Project 1: The Nature Conservancy", "Project 1"],
            ["Project 2: School on Wheels", "Project 2"],
            ["Project 3: Second Harvest Food Bank of Orange County", "Project 3"],
            ["Project 4: California Fire Foundation", "Project 4"],
            ["Project 5: Second Harvest Food Bank of Orange County", "Project 5"],
            ["Project 6: Abilities OC", "Project 6"],
        ],
        widget=widgets.RadioSelect,
        verbose_name="What project will the charitable payment benefit?",
    )  # type: ignore
    chosen_round = models.IntegerField()


class C(BaseConstants):
    NAME_IN_URL = "knapsack_intro"
    NUM_ROUNDS = 1
    PLAYERS_PER_GROUP = None
    EUR_PER_TALER = 0.04
    POINTS_CUSTOM_NAME = "Talers"


class Subsession(BaseSubsession):
    pass


class ChooseCharity(Page):
    form_model = "player"
    form_fields = ["charity_choice"]

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.chosen_round = random.choice([2, 3, 4, 6, 7, 8])  # type: ignore


def convert_payouts(round):
    eround = {**round}
    eround["value_self"] = C.EUR_PER_TALER * round["value_self"]
    eround["value_other"] = C.EUR_PER_TALER * (round["value_other"] or 0)

    return eround


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        prp = db._db.execute(
            f"select * from knapsack_sp_tasks_player where participant_id = :pid and round_number in (2,3,4, 6,7,8)",
            params={"pid": player.participant.id},
        )  # type: ignore
        player_rounds = [dict(zip(row.keys(), row)) for row in prp]  # type: ignore

        charity_in_bi = not (player_rounds[0]["mode"] == "sp")

        block_i = []
        block_ii = []
        for pr in player_rounds:
            if pr["round_number"] == player.chosen_round:
                pr["class"] = "table-success"
                selected = convert_payouts(pr)
            else:
                pr["class"] = ""
            (block_i if pr["round_number"] < 5 else block_ii).append(pr)

        return dict(block_i=block_i, block_ii=block_ii, selected=selected, charity_in_bi=charity_in_bi)  # type: ignore


page_sequence = [ChooseCharity, Results]
