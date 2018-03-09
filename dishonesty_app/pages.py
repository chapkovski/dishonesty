from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from .forms import GuessFormSet


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


class GuessStrategy(Page):
    def is_displayed(self):
        return self.player.role() == 'receiver'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = GuessFormSet(instance=self.player)
        return context

    def post(self):
        self.object = self.get_object()
        self.form = self.get_form(
            data=self.request.POST, files=self.request.FILES, instance=self.object)

        formset = GuessFormSet(self.request.POST, instance=self.player)

        if not formset.is_valid():
            context = self.get_context_data()
            context['formset'] = formset
            self.form.add_error(None, 'all fields are required!')
            context['form'] = self.form
            return self.render_to_response(context)
        formset.save()
        return super().post()

    def before_next_page(self):
        self.player.dump_guess_answer = self.player.dumping_answer()
        sender_decision = Constants.endowment - self.group.kept
        alloc_to_guess = self.group.get_player_by_role('sender').participant.vars['allocation']
        receiver_guess = self.player.guesses.get(sender_choice=alloc_to_guess).answer
        diff = sender_decision - receiver_guess
        self.group.receiver_guess = receiver_guess
        self.group.diff_guess = diff


class Results(Page):
    def offer(self):
        return Constants.endowment - self.group.kept

    def bonus2(self):
        return Constants.endowment - self.group.kept + self.subsession.bonus * self.subsession.bonus_multiplier

    def vars_for_template(self):
        return {
            'offer': Constants.endowment - self.group.kept,
            'bonus2': Constants.endowment - self.group.kept + self.subsession.bonus * self.subsession.bonus_multiplier
        }


page_sequence = [
    DGInstructions,
    AllocationInfo,
    DGInstructions2,
    Offer,
    ResultsWaitPage,
    GuessStrategy,
    Results
]
