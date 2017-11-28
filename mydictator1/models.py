from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
from collections import defaultdict

doc = """
One player decides how to divide a certain amount between himself and the other
player.

"""


class Constants(BaseConstants):
    name_in_url = 'mydictator1'
    players_per_group = 2
    num_rounds = 2

    instructions_template = 'mydictator1/Instructions.html'

    # Initial amount allocated to the dictator
    endowment = c(60)
    kept_choices = range(10, 100, 10)

    multiplier = 2


class Subsession(BaseSubsession):

    def before_session_starts(self):
        if self.round_number == 1:
            paying_round = random.randint(1, Constants.num_rounds)
            self.session.vars['paying_round'] = paying_round
        if self.round_number == 3:
            # reverse the roles
            for group in self.get_groups():
                players = group.get_players()
                players.reverse()
                group.set_players(players)
        if self.round_number > 3:
            self.group_like_round(3)
"""""""""
 only if we random the assignment to be executed for each round
    def before_session_starts(self):
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['color'] = random.choice(['blue', 'red'])

 --> only if we want to have it multiple round
   def before_session_starts(self):
       if self.round_number == 1:
           paying_round = random.randint(1, Constants.num_rounds)
       self.session.vars['paying_round'] = paying_round
        if self.round_number == 3:
            # reverse the roles
            for group in self.get_groups():
                players = group.get_players()
                players.reverse()
                group.set_players(players)
        if self.round_number > 3:
            self.group_like_round(3)
"""""""""

class Group(BaseGroup):
    kept = models.CurrencyField(
        doc="""Amount sender decided to keep for himself""",
        min=0, max=Constants.endowment,
        verbose_name='I will keep (from 0 to %i)' % Constants.endowment
    )

    Ikeep = models.CurrencyField(
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


class Player(BasePlayer):
    color = models.CharField()

    def role(self):
        if self.id_in_group == 1:
            return 'sender'
        if self.id_in_group == 2:
            return 'receiver'

    def summary_table(self):
        payoff_dict = defaultdict(float)

        for player in self.participant.get_players():
            app_name = player._meta.app_label
            payoff_dict[app_name] += player.payoff or 0

        return payoff_dict
