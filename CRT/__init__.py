from typing import Dict

from otree.api import *

doc = """
4 cognitive reflection test
"""


class C(BaseConstants):
    NAME_IN_URL = 'CRT'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    CRT1 = models.IntegerField(
        label='''1.Amy received both the 25th highest and the 25th lowest mark in the class. 
        How many students are in the class? ''',
    )
    CRT2 = models.IntegerField(
        label='''2.	Benjamin buys a pig for £70, sells it for £80, 
        buys it back for £100 and sells it finally for £120. How many pounds has he made?'''
    )
    CRT3 = models.IntegerField(
        label='''3.	Charlie and David’s age add up to 110 years old, 
        Charlie is 100 years older than David. How old is David?'''
    )
    CRT4 = models.IntegerField(
        label='''4.	If it takes 5 machines 5 minutes to make 5 widgets, 
        how long would it take 100 machines to make 100 widgets?'''
    )
    total_correct_answers = models.IntegerField(initial=0)


def set_payoffs(player: Player):
    if player.CRT1 == 49:
        player.total_correct_answers += 1
    if player.CRT2 == 30:
        player.total_correct_answers += 1
    if player.CRT3 == 5:
        player.total_correct_answers += 1
    if player.CRT4 == 5:
        player.total_correct_answers += 1
    player.payoff = 4 * player.total_correct_answers
    player.participant.CRT_result = player.total_correct_answers


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['CRT1', 'CRT2', 'CRT3', 'CRT4']

    def before_next_page(player: Player, timeout_happened):
        set_payoffs(player)


class Results(Page):
    pass


page_sequence = [MyPage]