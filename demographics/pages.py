from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page


class MyPage(Page):
    form_model = models.Player
    form_fields = ["age", "is_female", "education", "background"]


page_sequence = [MyPage]
