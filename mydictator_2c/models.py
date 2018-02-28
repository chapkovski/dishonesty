from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


doc = """
One player decides how to divide a certain amount between himself and the other
player.

"""


class Constants(BaseConstants):
    name_in_url = 'mydictator_2c'
    players_per_group = 2
    num_rounds = 1


    # Initial amount allocated to the dictator
    endowment = c(100)

    kept_choices = range (10, 100, 10)

    multiplier=2


class Player(BasePlayer):
    allocation2c=models.IntegerField()

    def role(self):
        if self.id_in_group == 1:
            return 'sender'
        if self.id_in_group == 2:
            return 'receiver'

    #def get_partner_catch(self):
        #partner = self.get_others_in_group()[0]
        #return partner.participant.vars['catches1']

    #def get_partner_income(self):
        #partner = self.get_others_in_group()[0]
        #return partner.participant.vars['income1']


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                p.allocation2c=p.participant.vars['randnumber2c']*10



class Group(BaseGroup):
    kept = models.CurrencyField(
        doc="""Amount sender decided to keep for himself""",
        min=0, max=Constants.endowment,
        verbose_name='I will keep (from 0 to %i)' % Constants.endowment
    )

    Ikeep = models.CurrencyField (
        choices=Constants.kept_choices,
        doc="""receiver kept""",
        verbose_name='I understand that the amount of random number advise me to allocate this amount',
        widget=widgets.RadioSelectHorizontal()
    )




    def set_payoffs(self):
        sender = self.get_player_by_id(1)
        receiver = self.get_player_by_id(2)
        if self.round_number == 1:
            sender.payoff = self.kept * 2
            receiver.payoff = Constants.endowment - self.kept
        if self.round_number == 2:
            sender.payoff = self.kept
            receiver.payoff = (Constants.endowment - self.kept) * 2






