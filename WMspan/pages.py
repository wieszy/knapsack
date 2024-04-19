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

    def before_next_page(self):
        self.player.set_payoffs()

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
    Recall
]
