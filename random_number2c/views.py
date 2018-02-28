from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Instructions(Page):
    pass

class MyPage(Page):

    def vars_for_template(self):
       return {'randnumber2c': self.player.participant.vars['randnumber2c'],'allocation2c':self.player.participant.vars['randnumber2c']*10,}


    def is_displayed(self):
           return self.player.id_in_group == 1

class ResultsWaitPage(WaitPage):

    def vars_for_template(self):
        if self.player.id_in_group == 2:
            body_text = "You are participant 2. Waiting for participant 1 to decide."
        else:
            body_text = 'Please wait'


class Results(Page):
    pass


page_sequence = [
    Instructions,
    MyPage,
    ResultsWaitPage
]
