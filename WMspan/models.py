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
    GBP_PER_CORRECT = 0.10

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
    
    def set_payoffs(self):
        self.correct = self.answer_1 + self.answer_2  + + self.answer_3 + self.answer_4 + self.answer_5 + self.answer_6 + self.answer_7 + self.answer_8
        self.num_recall = checkLetters(Constants.sequence,self.recall)
        self.payoff += (self.correct + self.num_recall)*Constants.GBP_PER_CORRECT
        self.participant.vars["wm_span_result"] = self.payoff

    
# FUNCTIONS
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
    

    

            
