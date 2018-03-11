from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class WorkerPage(Page):
    def is_displayed(self):
        return self.player.role() == 'worker'


class Introduction(Page):
    def vars_for_template(self):
        intro_text = "ball_catch/Instructions.html"
        return {
            'introduction': intro_text,
        }


class Task(WorkerPage):
    form_model = 'player'
    form_fields = ['catches', 'clicks', 'score', 'expense']

    def vars_for_template(self):
        return {
            'prize': self.player.prize,
            'cost': self.player.cost,
        }

    def before_next_page(self):
        self.player.set_payoff()
        

        


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        # TODO: important! the following code may produce wrong results if we later switch to multi-round RET.
        # TODO: for one round version it's ok
        # Understood. I think one round is enough for me now
        # I also need to show the partner's (workers) productivity, in the sender page 
        
        workers = [p for p in self.subsession.get_players() if p.role() == 'worker']
        total_catch = sum([p.catches for p in workers])
        avgcatch = round(total_catch / len(workers),1)
        self.session.vars['avgcatch'] = avgcatch
        total_income = sum([p.payoff for p in workers if p.payoff is not None])
        avgincome = round(total_income / len(workers),1)
        self.session.vars['avgpoints'] = avgincome
        
        

class Results(WorkerPage):
    ...


class Roundhistory(WorkerPage):
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


page_sequence = [
    Introduction,
    Task,
    ResultsWaitPage,
    Results,
    Roundhistory
]
