from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    def vars_for_template(self):
        intro_text = "ball_catch3/Instructions.html"

        if self.round_number== 1 and self.participant.vars['color'] == 'blue' :
            intro_text="ball_catch3/Instructions_2.html"

        return {
            'introduction': intro_text,
        }

    #def is_displayed(self):
        #return self.player.is_playing()


class Task(Page):
    form_model = models.Player
    form_fields = ['catches', 'clicks', 'score', 'expense']

    def vars_for_template(self):
        return {
            'prize': self.player.prize,
            'cost': self.player.cost,
        }

    def before_next_page(self):
        self.player.set_payoff()

    def is_displayed(self):
        return self.participant.vars['color']=='blue'


class firstphase(Page):
    def is_displayed(self):
        return self.participant.vars['color']=='blue'

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.biru()
        for g in self.group.get_players():
            self.group.biru()

class Results(Page):
    def is_displayed(self):
        return self.participant.vars['color']=='blue'

class Roundhistory(Page) :
    def vars_for_template(self):

        round_history = []
        for me_prev_round in self.player.in_all_rounds():
            round_history.append({
                'round_number': me_prev_round.round_number,
                'me': me_prev_round,
                'others': me_prev_round.get_others_in_group(),

            })

            other_player_ids = [p.id_in_group for p in self.player.get_others_in_group()]

            return {
                'other_player_ids': other_player_ids,
                'round_history': round_history
            }
    def is_displayed(self):
        return self.participant.vars['color']=='blue'

page_sequence = [
    Introduction,
    firstphase,
    Task,
    ResultsWaitPage,
    Results,
    Roundhistory
]

# FROM INTRO

from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    #form_model = models.Player
    #form_fields = ['color']


    def vars_for_template(self):
        intro_text = "ball_catch_intro/Instructions.html"

        if self.round_number > 1 and self.player.id_in_group == 2 :
            intro_text="ball_catch_intro/Instructions_2.html"

        return {
            'introduction': intro_text,
        }



page_sequence = [
    Introduction
]
