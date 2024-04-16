from otree.api import (
    BasePlayer,
    BaseGroup,
    BaseSubsession,
    BaseConstants,
    Page,
)

doc = """
Knapsack Problem
"""


class Group(BaseGroup):
    pass


# this includes all fields that a player may submit
class Player(BasePlayer):
    pass


class C(BaseConstants):
    NAME_IN_URL = "knapsack_results"
    NUM_ROUNDS = 1
    PLAYERS_PER_GROUP = None
    EUR_PER_TALER = 0.04
    POINTS_CUSTOM_NAME = "Talers"


class Subsession(BaseSubsession):
    pass


class Intro(Page):
    pass


page_sequence = [
    Intro,
]
