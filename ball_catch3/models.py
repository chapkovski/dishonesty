from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, WaitPage,
    Currency as c, currency_range
)
import random
import csv
import itertools
from django.db import models as djmodels

author = "rizal"

doc = """
Ball-Catching Task
"""


class Constants(BaseConstants):
    name_in_url = 'ball_catch3'
    players_per_group = None

    num_rounds = 1

    prize_and_cost = [1, 2, 3, 4]



class Subsession(BaseSubsession):
    def creating_session(self):
        # alternate assignment to blue or red before first round
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
    total_blue = models.IntegerField()
    average = models.IntegerField()

    def biru(self):
        totalblue = 0
        group_num = 0
        if Player.role=='blue_group':
            for g in self.get_group():
                g.total_blue= totalblue + g.catches()
                print('total_blue is:', g.total_blue)
                group_num += 1
                g.average1=g.total_blue/group_num
                g.average=round(g.average1,2)
                g.session.vars['avg'] = g.average



class Player(BasePlayer):

    condition = models.IntegerField()
    prize = models.IntegerField()
    cost = models.IntegerField()
    catches = models.IntegerField()
    clicks = models.IntegerField()
    score = models.IntegerField()
    expense = models.IntegerField()
    color = models.BooleanField


    def role(self):
        if self.participant.vars['color']=='blue':
            return 'blue_group'
        else : return 'red_group'

    def set_payoff(self):
        self.payoff = self.score - self.expense
        self.ballcatch = self.catches*1
        self.participant.vars['income1'] = self.payoff
        self.participant.vars['catches1']= self.ballcatch

# ini kalau group masih pake yang lama #

    def get_partner_catch(self):
        partner = self.get_others_in_group()[0]
        return partner.participant.vars['catches2']

    def get_partner_income(self):
        partner = self.get_others_in_group()[0]
        return partner.participant.vars['income2']

