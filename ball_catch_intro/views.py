from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    #form_model = models.Player
    #form_fields = ['color']


    def vars_for_template(self):
        intro_text = "ball_catch_intro/Instructions.html"

        if self.round_number > 1 and self.player.id_in_group == 2 :
            intro_text="ball_catch_intro/Instructions_2.html"

        return {
            'introduction': intro_text,
        }



page_sequence = [
    Introduction
]
