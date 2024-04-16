from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, checkLetters
import random


class Instructions(Page):
    timeout_seconds = 60

class Page1(Page):
    timeout_seconds = 15
    form_model = 'player'
    form_fields = ['answer_1']

class Page2(Page):
    timeout_seconds = 15
    form_model = 'player'
    form_fields = ['answer_2']

class Page3(Page):
    timeout_seconds = 15
    form_model = 'player'
    form_fields = ['answer_3']

class Page4(Page):
    timeout_seconds = 15
    form_model = 'player'
    form_fields = ['answer_4']

class Page5(Page):
    timeout_seconds = 15
    form_model = 'player'
    form_fields = ['answer_5']

class Page6(Page):
    timeout_seconds = 15
    form_model = 'player'
    form_fields = ['answer_6']

class Page7(Page):
        timeout_seconds = 15
        form_model = 'player'
        form_fields = ['answer_7']

class Page8(Page):
    timeout_seconds = 15
    form_model = 'player'
    form_fields = ['answer_8']

class Recall(Page):
    timeout_seconds = 30
    form_model = 'player'
    form_fields = ['recall']

class Results(Page):
    def vars_for_template(self):
        self.player.correct = self.player.answer_1 + self.player.answer_2  + + self.player.answer_3 + self.player.answer_4 + self.player.answer_5 + self.player.answer_6 + self.player.answer_7 + self.player.answer_8
        self.player.num_recall = checkLetters(Constants.sequence,self.player.recall)

page_sequence = [
    Instructions,
    Page1,
    Page2,
    Page3,
    Page4,
    Page5,
    Page6,
    Page7,
    Page8,
    Recall,
    Results
]
