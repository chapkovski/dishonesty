from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'rizal adi prima'

doc = """
create a random number to be seen by participant
"""


class Constants(BaseConstants):
    name_in_url = 'random_number2c'
    players_per_group = None
    num_rounds = 1
    multiplier = 10
    endowment = 100

class Subsession(BaseSubsession):
    def is_displayed(self):
        return self.participant.vars['color'] == 'blue'


    def creating_session(self):
        for p in self.get_players():
            p.randnumber = random.randint(1, 10)
            p.participant.vars['randnumber2c'] = p.randnumber


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    randnumber = models.FloatField()
