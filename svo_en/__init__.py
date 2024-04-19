from otree.api import (
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    models,
    widgets,
    Page,
    WaitPage,
)

author = "Your name here"
doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = "svo_en"
    NUM_ROUNDS = 1
    PLAYERS_PER_GROUP = None
    INSTRUCTIONS_TEMPLATE = "svo_en/Instructions.html"
    OWN_FIRST = (100, 98, 96, 94, 93, 91, 89, 87, 85)
    OWN_SECOND = (100, 94, 88, 81, 75, 69, 63, 56, 50)
    OWN_THIRD = (50, 54, 59, 63, 68, 72, 76, 81, 85)
    OWN_FOURTH = (50, 54, 59, 63, 68, 72, 76, 81, 85)
    OWN_FIFTH = (85, 87, 89, 91, 93, 94, 96, 98, 100)
    OWN_SIXTH = (85, 85, 85, 85, 85, 85, 85, 85, 85)
    OTHER_FIRST = (50, 54, 59, 63, 68, 72, 76, 81, 85)
    OTHER_SECOND = (50, 56, 63, 69, 75, 81, 88, 94, 100)
    OTHER_THIRD = (100, 89, 79, 68, 58, 47, 36, 26, 15)
    OTHER_FOURTH = (100, 98, 96, 94, 93, 91, 89, 87, 85)
    OTHER_FIFTH = (15, 19, 24, 28, 33, 37, 41, 46, 50)
    OTHER_SIXTH = (85, 76, 68, 59, 50, 41, 33, 24, 15)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    svo_score = models.FloatField()
    offer_1 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5, 6, 7, 8, 9]
    )
    offer_2 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5, 6, 7, 8, 9]
    )
    offer_3 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5, 6, 7, 8, 9]
    )
    offer_4 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5, 6, 7, 8, 9]
    )
    offer_5 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5, 6, 7, 8, 9]
    )
    offer_6 = models.IntegerField(
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5, 6, 7, 8, 9]
    )


# FUNCTIONS
def set_payoffs(player: Player):
            player.payoff += (1 / 1000) * (
                C.OWN_FIRST[player.offer_1 - 1]
                + C.OWN_SECOND[player.offer_2 - 1]
                + C.OWN_THIRD[player.offer_3 - 1]
                + C.OWN_FOURTH[player.offer_4 - 1]
                + C.OWN_FIFTH[player.offer_5 - 1]
                + C.OWN_SIXTH[player.offer_6 - 1]
                + C.OTHER_FIRST[player.offer_1 - 1]
                + C.OTHER_SECOND[player.offer_2 - 1]
                + C.OTHER_THIRD[player.offer_3 - 1]
                + C.OTHER_FOURTH[player.offer_4 - 1]
                + C.OTHER_FIFTH[player.offer_5 - 1]
                + C.OTHER_SIXTH[player.offer_6 - 1]
            )

# PAGES
class Introduction(Page):
    pass


class Page1(Page):
    form_model = "player"
    form_fields = ["offer_1", "offer_2", "offer_3"]


class Page2(Page):
    form_model = "player"
    form_fields = ["offer_4", "offer_5", "offer_6"]

    def before_next_page(player: Player, timeout_happened):
        set_payoffs(player)
        player.participant.vars["svo_result"] = player.participant.payoff

class Results(Page):
    pass


page_sequence = [Introduction, Page1, Page2]
