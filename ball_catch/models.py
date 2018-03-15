from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, WaitPage,
    Currency as c, currency_range
)
import random
import csv
import itertools
from django.db import models as djmodels

author = "rap, chapkovski"

doc = """
    Ball-Catching Task
"""


class Constants(BaseConstants):
    name_in_url = 'ball_catch3'
    players_per_group = None

    num_rounds = 1
    ret_timer = 10
    prize_and_cost = [1, 2, 3, 4]


class Subsession(BaseSubsession):
    def creating_session(self):
        # alternate assignment to blue or red before first round
        colors = itertools.cycle(['blue', 'red'])
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['color'] = next(colors)

        if self.round_number == 1:
            for p in self.get_players():
                my_prize_and_cost = Constants.prize_and_cost.copy()
                random.shuffle(my_prize_and_cost)
                p.participant.vars['my_prize_and_cost'] = my_prize_and_cost

            for p in self.get_players():
                p.condition = p.participant.vars['my_prize_and_cost'][self.round_number - 1]
                if p.condition <= 2:
                    p.prize = 10
                    p.cost = 5 * (p.condition - 1)
                else:
                    p.prize = 20
                    p.cost = 5 * (p.condition - 2)


class Group(BaseGroup):
    total_catch = models.IntegerField(doc="""the total amount of catches""", initial=0)
    total_income = models.IntegerField(doc="""the total amount of payoff""", initial=0)
    avg = models.IntegerField(doc="""the total amount of catches""", initial=0)
    avgincome = models.IntegerField(doc="""the total amount of payoff""", initial=0)


class Player(BasePlayer):
    work_timer = djmodels.DateTimeField(null=True)
    condition = models.IntegerField()
    prize = models.IntegerField()
    cost = models.IntegerField()
    catches = models.IntegerField(doc="""the amount of catches""", initial=0)
    clicks = models.IntegerField(initial=0)
    score = models.IntegerField(doc="""the amount of score""", initial=0)
    expense = models.IntegerField(doc="""cost of clicking""", initial=0)
    # catches2 = models.IntegerField(doc="""try to find out what is inside""", initial=0)

    def role(self):
        if self.participant.vars['color'] == "red":
            return 'idle'
        if self.participant.vars['color'] == "blue":
            return 'worker'

    def set_payoff(self):
        self.payoff = self.score - self.expense
        self.participant.vars['output2'] = self.catches
        self.participant.vars['income2'] = self.payoff
