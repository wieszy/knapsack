from otree.api import (
    BasePlayer,
    BaseGroup,
    BaseSubsession,
    BaseConstants,
    models,
    Page,
)

doc = """
Welcome
"""


class Group(BaseGroup):
    pass


# this includes all fields that a player may submit
class Player(BasePlayer):
    prolific_id = models.StringField()


class C(BaseConstants):
    NAME_IN_URL = "welcome"
    NUM_ROUNDS = 1
    PLAYERS_PER_GROUP = None
    EUR_PER_TALER = 0.04
    POINTS_CUSTOM_NAME = "Talers"


class Subsession(BaseSubsession):
    pass


class Intro(Page):
    form_model = "player"
    form_fields = ["prolific_id"]


page_sequence = [
    Intro,
]



