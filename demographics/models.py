from otree.api import (
    models,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
)


author = "Wiebke Szymczak"

doc = """
Demographics questionnaire 
"""


class Constants(BaseConstants):
    name_in_url = "demographics"
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.PositiveIntegerField()

    is_female = models.BooleanField(
        choices=[
            [True, "Female"],
            [False, "Male"],
        ]
    )

    education = models.PositiveIntegerField(
        choices=[
            [1, "Other"],
            [2, "High School diploma or equivalent"],
            [3, "Bachelor degree or equivalent"],
            [4, "Master degree or equivalent"],
            [5, "Doctoral degree or equivalent"],
        ]
    )

    background = models.PositiveIntegerField(
        choices=[
            [1, "Yes, I have attended one class on Business and/or Economics."],
            [
                2,
                "Yes, I have attended more than one class on Business and/or Economics.",
            ],
            [3, "Yes, I have studied Business or Economics as my major."],
            [0, "No, I have not attended any classes on either topic."],
        ]
    )
