from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, WaitPage,
    Currency as c, currency_range
)
import random
import csv
import itertools

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

        else: self.group_like_round(1)

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

total_group = models.IntegerField(doc="""the total amount of catches""",initial=0)
group_num = models.IntegerField(doc="""number of group""",initial=0)

class Group(BaseGroup):
    ...
    #def aggregate(self):
       # if self.round_number == 1:
        #    for p in self.get_players():
          #      players = self.get_players()
           #     players.total= total_group + Player.catches()
           #     print('total is:', players.total)
           #     p.average1=g.total_blue/group_num
           #     p.average=round(p.average1,2)
           #     p.session.vars['avg'] = p.average


class Player(BasePlayer):

    condition = models.IntegerField()
    prize = models.IntegerField()
    cost = models.IntegerField()
    catches = models.IntegerField(doc="""the amount of catches""",initial=0)
    clicks = models.IntegerField()
    score = models.IntegerField(doc="""the amount of score""", initial=0)
    expense = models.IntegerField(doc="""cost of clicking""", initial=0)


    def role(self):
        if self.participant.vars['color']=="red" :
            return 'sender'
        if self.participant.vars['color']=="blue":
            return 'receiver'


    def set_payoff(self):
        self.payoff = self.score - self.expense
        self.ballcatch = self.catches*1
        print('@@@@ ballcatch:', self.ballcatch)
        self.participant.vars['income1'] = self.payoff
        print('@@@@ income1:', self.participant.vars['income1'])
        self.participant.vars['catches1']= self.ballcatch

    def get_partner(self):
        self.partner = self.get_others_in_group()[0]
        self.partner.payoff = self.partner.score - self.partner.expense
        print('@@@@ payoff:', self.partner.payoff)
        self.partner.ballcatch = self.partner.catches * 1
        self.participant.vars['income2'] = self.partner.payoff
        print('@@@@ income2:', self.participant.vars['income2'])
        self.participant.vars['catches2'] = self.partner.ballcatch
        print('@@@@ catches2:', self.participant.vars['income2'])



