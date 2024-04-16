import itertools as it
from otree.api import (
    BasePlayer,
    BaseGroup,
    BaseSubsession,
    BaseConstants,
    Page,
    models,
    read_csv,
    ExtraModel,
)
import random
from datetime import datetime

doc = """
Knapsack Problem
"""

# 2*3*2 = 12 treatment groups
treatment_groups = it.product(
    ["sp_first", "mp_first"],
    ["donation", "mixed", "damage"],
    ["double_sp_values", "double_mp_values"],
)

task_count = 4

endowments = {
    "donation": [0, 0, 0, 0],
    "mixed": [300, 160, 120, 150],
    "damage": [600, 320, 240, 300],
}


class Project(ExtraModel):
    iid = models.IntegerField()
    treatment_group = models.StringField()
    task = models.IntegerField()
    item = models.IntegerField()
    value_self = models.IntegerField()
    value_other = models.IntegerField()
    cost = models.IntegerField()


# I gave you the type info explicitly, how are you missing types?
project_options = read_csv("knapsack_sp_tasks/exp_values.csv", Project)  # type: ignore
tasks = set(map(lambda x: x["task"], project_options))


class Event(ExtraModel):
    participant_id = models.IntegerField()
    participant_code = models.StringField()
    session_id = models.IntegerField()
    session_code = models.StringField()
    type = models.StringField()
    target = models.IntegerField()
    timestamp = models.StringField()
    round = models.IntegerField()
    treatment_group = models.StringField()


def create_event(player, type, target):
    return Event.create(
        participant_id=player.participant.id,
        participant_code=player.participant.code,
        session_id=player.participant.session.id,
        session_code=player.participant.session.code,
        type=type,
        target=target,
        timestamp=str(datetime.now().isoformat()),
        round=player.round_number,
        treatment_group="__".join(player.participant.vars["treatment_group"]),
    )


class Group(BaseGroup):
    pass


# this includes all fields that a player may submit
class Player(BasePlayer):
    value_self = models.IntegerField()
    value_other = models.IntegerField(blank=True)  # type: ignore
    cost = models.IntegerField()
    treatment_group = models.StringField()
    mode = models.StringField()


class C(BaseConstants):
    NAME_IN_URL = "knapsack_tasks"
    NUM_ROUNDS = task_count * 2
    PLAYERS_PER_GROUP = None
    EUR_PER_TALER = 0.04
    POINTS_CUSTOM_NAME = "ECU"


def creating_session(subsession, tgc=it.cycle(treatment_groups)):
    if subsession.round_number == 1:
        for player in subsession.get_players():
            player.participant.vars["treatment_group"] = tgc.__next__()


class Subsession(BaseSubsession):
    pass


class Choose(Page):
    form_model = "player"
    form_fields = ["value_self", "value_other", "cost"]

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        create_event(player, "submit", None)

        player.treatment_group = "__".join(player.participant.vars["treatment_group"])  # type: ignore
        player.mode = (  # type: ignore
            "sp"
            if (player.participant.vars["treatment_group"][0] == "sp_first")
            != (player.round_number > task_count)
            else "mp"
        )

    @staticmethod
    def error_message(player: Player, values):
        if values["cost"] == values["value_self"] == 0:
            return "Please choose some projects."

    @staticmethod
    def vars_for_template(player: Player):
        sp_round = (player.participant.vars["treatment_group"][0] == "sp_first") != (
            player.round_number > task_count
        )
        return dict(
            block_n="II" if (player.round_number // task_count) == 1 else "I",
            block_name=(
                "second" if (player.round_number // task_count) == 1 else "first"
            ),
            sp_round=sp_round,
            test_round=((player.round_number - 1) % task_count) == 0,
            task_idx=((player.round_number - 1) % task_count),
            task_count=task_count - 1,
            endowment=endowments[player.participant.vars["treatment_group"][1]][
                (player.round_number - 1) % task_count
            ],
        )

    @staticmethod
    def js_vars(player: Player):
        sp_round = (player.participant.vars["treatment_group"][0] == "sp_first") != (
            player.round_number > task_count
        )
        value_multiplier = (
            2
            if (
                sp_round
                == (player.participant.vars["treatment_group"][2] == "double_sp_values")
            )
            != ((player.round_number - 1) % 4 == 0)  # behavior reversed for test rounds
            else 1
        )

        options = [
            task
            for task in project_options
            if task["task"] == (player.round_number - 1) % task_count
            and task["treatment_group"] == player.participant.vars["treatment_group"][1]
        ]

        return dict(
            single_player=sp_round,
            options=random.sample(options, len(options)),
            budget=player.session.config["budget"],
            value_multiplier=value_multiplier,
            endowment=endowments[player.participant.vars["treatment_group"][1]][
                (player.round_number - 1) % task_count
            ],
            group=player.participant.vars["treatment_group"],
        )

    @staticmethod
    def live_method(player: Player, data):
        create_event(player, data["event"], data["target"])
        return {0: {"from": player.participant.id, **data}}


class BlockChange(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == task_count


class Results(Page):
    @staticmethod
    def is_displayed(player):
        return (player.round_number - 1) % task_count == 0

    @staticmethod
    def vars_for_template(player: Player):
        sp_round = (player.participant.vars["treatment_group"][0] == "sp_first") != (
            player.round_number > task_count
        )
        return dict(
            block_n="II" if (player.round_number // task_count) == 1 else "I",
            sp_round=sp_round,
            test_round=((player.round_number - 1) % task_count) == 0,
            task_idx=((player.round_number - 1) % task_count) + 1,
            task_count=task_count,
        )


page_sequence = [Choose, Results, BlockChange]
