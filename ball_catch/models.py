from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, WaitPage,
    Currency as c, currency_range
)


author = "rap"

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
                g.session.vars['avgcatch'] = g.average



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



# FROM INTRO

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,WaitPage,
    Currency as c, currency_range
)
import random
import itertools
import operator
import functools


author = "rizal"

doc = """
Ball-Catching Task
"""


class Constants(BaseConstants):
    name_in_url = 'ball_catch_intro'
    players_per_group = None
    num_rounds=1

class Shufflewaitpage(WaitPage):
    wait_for_all_groups = True

class Subsession(BaseSubsession):
    def creating_session(self):
        # alternate assignment to blue or red before first round
        colors = itertools.cycle(['blue', 'red'])
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['color'] = next(colors)
            players = self.get_players()

            random.shuffle(players)

            blue_players = [p for p in players if p.participant.vars['color'] == 'blue']
            red_players = [p for p in players if p.participant.vars['color'] == 'red']

            # initializes matrix

            group_matrix = []

            # appends pairs of players from the blue treatment to the end of a matrix of groups.
            while red_players:
                red_group = [
                    red_players.pop(),
                    red_players.pop()
                ]
                group_matrix.append(red_group)

            # appends pairs of players from the blue treatment to the end of a matrix of groups.
            while blue_players:
                blue_group = [
                    blue_players.pop(),
                    blue_players.pop()
                ]
                group_matrix.append(blue_group)

            # commits the matrix as the new grouping for this round.
            self.set_group_matrix(group_matrix)

        else:
            self.group_like_round(1)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
    #def #self.participant.vars['blue'] = 'blue_group'
        #self.participant.vars['red'] = 'red_group'

    #color=models.BooleanField()

