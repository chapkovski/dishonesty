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

