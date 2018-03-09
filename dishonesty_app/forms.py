import django.forms as forms
from .models import Player, GuessChoice, Constants
from django.forms import inlineformset_factory
from otree.api import widgets


class GuessForm(forms.ModelForm):
    class Meta:
        model = GuessChoice
        fields = ['answer']
        widgets = {
            'answer': widgets.RadioSelectHorizontal,
        }

    def __init__(self, *args, **kwargs):
        print('I AM IN FORM INIT')
        super().__init__(*args, **kwargs)
        self.fields['answer'].empty_label = None
        self.fields['answer'].choices = ((int(i), i) for i in Constants.offer_choices)


GuessFormSet = inlineformset_factory(Player, GuessChoice,
                                     extra=0,
                                     can_delete=False,
                                     form=GuessForm,
                                     )
