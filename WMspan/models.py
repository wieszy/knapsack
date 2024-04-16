from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from django import forms

author = 'Working span test'

doc = """
This is a shortened version of the Conway et al. (2005) test for operation span.
"""


class Constants(BaseConstants):
    name_in_url = 'WMspan'
    players_per_group = None
    num_rounds = 1

    num_letters = 8
    sequence = 'BNKJSQHT'

    num_questions = 8

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    answer_1 = models.IntegerField(
    choices=[
        [0, 'False'],
        [1, 'True'],
    ], widget=widgets.RadioSelect
    )
    answer_2 = models.IntegerField(
    choices=[
        [0, 'False'],
        [1, 'True'],
    ], widget=widgets.RadioSelect
    )
    answer_3 = models.IntegerField(
    choices=[
        [1, 'False'],
        [0, 'True'],
    ], widget=widgets.RadioSelect
    )
    answer_4 = models.IntegerField(
    choices=[
        [1, 'False'],
        [0, 'True'],
    ], widget=widgets.RadioSelect
    )
    answer_5 = models.IntegerField(
    choices=[
        [0, 'False'],
        [1, 'True'],
    ], widget=widgets.RadioSelect
    )
    answer_6 = models.IntegerField(
    choices=[
        [1, 'False'],
        [0, 'True'],
    ], widget=widgets.RadioSelect
    )
    answer_7 = models.IntegerField(
    choices=[
        [1, 'False'],
        [0, 'True'],
    ], widget=widgets.RadioSelect
    )
    answer_8 = models.IntegerField(
    choices=[
        [0, 'False'],
        [1, 'True'],
    ], widget=widgets.RadioSelect
    )

    correct = models.IntegerField()

    recall = models.StringField()
    num_recall = models.IntegerField()


def checkLetters(original, recall):
    list1 = list(original)
    list2 = list(recall)
    m = 0
    i = 0
    while i < len(list2):
        if list2[i] in list1:
            m+=1
            i+=1
        else:
            i+=1
    return m
