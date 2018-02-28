from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Demographics(Page):
    form_model = models.Player
    form_fields = ['age',
                   'gender']


class CognitiveReflectionTest(Page):
    form_model = models.Player
    form_fields = ['crt_bat',
                   'crt_widget',
                   'crt_lake']

class Religion (Page):
    form_model = models.Player
    form_fields = ['religion','religion1','religion2','religion3','religion4','religion5','religion6','religion7',
                   'income1','income2']

class Psychometri(Page):
    form_model = models.Player
    form_fields = ['trust1','trust2','trust3','trust4',
                   'hexaco1','hexaco2','hexaco3','hexaco4','hexaco5','hexaco6','hexaco7','hexaco8','hexaco9',
                   'hexaco10','hexaco11','hexaco12','hexaco13','hexaco14','hexaco15','hexaco16','hexaco17',
                   'hexaco18','hexaco19','hexaco20','hexaco21','hexaco22','hexaco23','hexaco24']

class Mypage (Page):
    form_model = models.Player
    form_fields = ['ypi1', 'ypi2', 'ypi3', 'ypi4', 'ypi5', 'ypi6', 'ypi7', 'ypi8', 'ypi9',
                   'ypi10', 'ypi11', 'ypi12', 'ypi13', 'ypi14', 'ypi15', 'ypi16', 'ypi17',
                   'ypi18', 'ypi19', 'ypi20']

class Results (Page):
  pass

page_sequence = [
    Demographics,
    CognitiveReflectionTest,
    Religion,
    Psychometri,
    Mypage
 ]
