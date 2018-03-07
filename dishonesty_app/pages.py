from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class SenderPage(Page):
    def is_displayed(self):
        return self.player.role() == 'sender'


class AllocationInfo(SenderPage):
    ...


class DGInstructions(SenderPage):
    ...


class DGInstructions2(Page):
    def vars_for_template(self):
        intro_text = "dishonesty_app/includes/{}Instructions.html".format(self.player.role())
        a = list(Constants.kept_choices)
        b = [i * 2 for i in a]
        c = [int(Constants.endowment - i) for i in a]
        return {
            'introduction': intro_text,
            'a': a, 'b': b, 'c': c,
        }


class Offer(SenderPage):
    form_model = models.Group
    form_fields = ['kept', 'should_keep']


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()

    def vars_for_template(self):
        if self.player.role() == 'receiver':
            body_text = "You are participant 2. Waiting for participant 1 to decide."
        else:
            body_text = 'Please wait'
        return {'body_text': body_text}


class Results(Page):
    def vars_for_template(self):
        return {

        }


page_sequence = [
    DGInstructions,
    AllocationInfo,
    DGInstructions2,
    Offer,
    ResultsWaitPage,
    Results
]
