from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

doc = """
One player decides how to divide a certain amount between himself and the other
player.

there are four possible treatments:
mydictator_2 : dictator + moral prime, with Random Number 'n' and endowment X
mydictator _2b  mydictator_2+ bonus for the receiver M  
mydictator _2c  mydictator_2 + bonus for the receiver M*2
mydictator _3x  mydictator_2 + info of relative performance of the receiver in the effort game 
"""


class Constants(BaseConstants):
    name_in_url = 'dshnst'
    players_per_group = 2
    num_rounds = 1
    endowment = c(100)
    kept_choices = range(10, 101, 10)
    rand_multiplier = 10


class Subsession(BaseSubsession):
    is_bonus_treatment = models.BooleanField(doc='true if bonus part is in treatment')
    bonus_multiplier = models.FloatField(doc='the multiplier of bonus for a recipient. Is used in some treatments')
    bonus = models.CurrencyField(doc="""how large is the bonus that should be paid to recipient. For 
                                        baseline treatment it is 0. For treatments with bonus (2b, 2c) it is a
                                         fixed amount or doubled fixed amount""",
                                 initial=0)

    def creating_session(self):

        self.bonus = self.session.config.get('bonus', 0)
        self.is_bonus_treatment = True if self.bonus > 0 else False
        self.bonus_multiplier = self.session.config.get('bonus_multiplier', 1)
        if self.round_number == 1:
            for p in self.session.get_participants():
                p.vars['randnumber'] = random.randint(1, 10)
                p.vars['allocation'] = p.vars['randnumber'] * 10


class Group(BaseGroup):
    kept = models.CurrencyField(
        doc="""Amount sender decided to keep for himself""",
        min=0, max=Constants.endowment,
        verbose_name='I will keep (from 0 to %i)' % Constants.endowment
    )

    should_keep = models.CurrencyField(
        choices=Constants.kept_choices,
        doc="""receiver kept""",
        verbose_name='I understand that the amount of random number advise me to allocate this amount',
        widget=widgets.RadioSelectHorizontal()
    )

    def set_payoffs(self):
        sender = self.get_player_by_role('sender')
        receiver = self.get_player_by_role('receiver')
        sender.payoff = self.kept * 2
        receiver.payoff = Constants.endowment - self.kept + self.subsession.bonus * self.subsession.bonus_multiplier


class Player(BasePlayer):
    def role(self):
        if self.id_in_group == 1:
            return 'sender'
        if self.id_in_group == 2:
            return 'receiver'
