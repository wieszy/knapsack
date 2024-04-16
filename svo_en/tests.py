from otree.api import Currency as cu, currency_range
from . import Page1, Page2, Results
from otree.api import Bot


class PlayerBot(Bot):

    def play_round(self):
        yield (Page1)
        yield (Page2)
        yield (Results)
