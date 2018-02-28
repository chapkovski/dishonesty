from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    age = models.PositiveIntegerField(
        verbose_name='What is your age?',
        min=13, max=40)

    gender = models.CharField(
        choices=['Male', 'Female'],
        verbose_name='What is your gender?',
        widget=widgets.RadioSelect())

    crt_bat = models.PositiveIntegerField(
        verbose_name='''
        A bat and a ball cost 22 dollars in total.
        The bat costs 20 dollars more than the ball.
        How many dollars does the ball cost?'''
    )

    crt_widget = models.PositiveIntegerField(
        verbose_name='''
        "If it takes 5 machines 5 minutes to make 5 widgets,
        how many minutes would it take 100 machines to make 100 widgets?"
        '''
    )

    crt_lake = models.PositiveIntegerField(
        verbose_name='''
        In a lake, there is a patch of lily pads.
        Every day, the patch doubles in size.
        If it takes 48 days for the patch to cover the entire lake,
        how many days would it take for the patch to cover half of the lake?
        '''
    )

    income1 = models.CharField(
        choices=['$1,000 - $ 2,000',
                 '$ 2,001 – $3,100',
                 '$3,101 -  $5,000', '$5,001 -  $7,250', '$7,251  and over'],
        verbose_name='How much was your INCOME last month?',
        widget=widgets.RadioSelect())

    income2 = models.CharField(
        choices=['The richest in the class',
                 'Among the richest in the class',
                 'Richer than most your friends', 'About average', 'The poorest in the class'],
        verbose_name='Compared to other people in your Class, would you describe you as…..(?',
        widget=widgets.RadioSelect())

    trust1 = models.CharField(
        choices=['Never',
                 'Rarely (every month)',
                 'Sometimes (every two weeks)', 'Often (every week)', 'Very often (every day)'],
        verbose_name='How often have you interacted with your friends in your class this month?',
        widget=widgets.RadioSelect())

    trust2 = models.CharField(
        choices=['1','2','3', '4', '5'],
        verbose_name='Most of my friends in my class are trustworthy.',
        widget=widgets.RadioSelectHorizontal())

    trust3 = models.CharField(
        choices=['1','2','3', '4', '5'],
        verbose_name='Most of my friends in my class are trustful of others.',
        widget=widgets.RadioSelectHorizontal())

    trust4 = models.CharField(
        choices=['1','2','3', '4', '5'],
        verbose_name='Most of my friends in my class are basically good and kind.',
        widget=widgets.RadioSelectHorizontal())
    hexaco1 = models.CharField(
        choices=['1','2','3', '4', '5'],
        verbose_name='I can look at a painting for a long time.',
        widget=widgets.RadioSelectHorizontal())

    hexaco2 = models.CharField(
        choices=['1','2','3', '4', '5'],
        verbose_name='I make sure that things are in the right spot.',
        widget=widgets.RadioSelectHorizontal())
    hexaco3 = models.CharField(
        choices=['1','2','3', '4', '5'],
        verbose_name='I remain unfriendly to someone who was mean to me.',
        widget=widgets.RadioSelectHorizontal())
    hexaco4 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='Nobody likes talking with me.',
        widget=widgets.RadioSelectHorizontal())

    hexaco5 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='I am afraid of feeling pain.',
        widget=widgets.RadioSelectHorizontal())
    hexaco6 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='I find it difficult to lie',
        widget=widgets.RadioSelectHorizontal())
    hexaco7 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='I think science is boring.',
        widget=widgets.RadioSelectHorizontal())

    hexaco8 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='I postpone complicated tasks as long as possible.',
        widget=widgets.RadioSelectHorizontal())
    hexaco9 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='I often express criticism.',
        widget=widgets.RadioSelectHorizontal())
    hexaco10 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='I easily approach strangers. ',
        widget=widgets.RadioSelectHorizontal())
    hexaco11 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='Even when I am treated badly, I remain calm.',
        widget=widgets.RadioSelectHorizontal())
    hexaco12 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='I have to cry during a sad or romantic movie.',
        widget=widgets.RadioSelectHorizontal())
    hexaco13 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='I worry less than others.',
        widget=widgets.RadioSelectHorizontal())
    hexaco14 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='I would like to know how to make lots of money in a dishonest manner',
        widget=widgets.RadioSelectHorizontal())
    hexaco15 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='I have a lot of imagination.',
        widget=widgets.RadioSelectHorizontal())
    hexaco16 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='I work very precisely.',
        widget=widgets.RadioSelectHorizontal())

    hexaco17 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='I tend to quickly agree with others.',
        widget=widgets.RadioSelectHorizontal())
    hexaco18 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='I like to talk with others.',
        widget=widgets.RadioSelectHorizontal())
    hexaco19 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='I can easily overcome difficulties on my own.',
        widget=widgets.RadioSelectHorizontal())

    hexaco20 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='I want to be famous.',
        widget=widgets.RadioSelectHorizontal())
    hexaco21 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='I like people with strange ideas.',
        widget=widgets.RadioSelectHorizontal())
    hexaco22 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='I often do things without really thinking.',
        widget=widgets.RadioSelectHorizontal())
    hexaco23 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='I am seldom cheerful.',
        widget=widgets.RadioSelectHorizontal())
    hexaco24 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='I am entitled to special treatment.',
        widget=widgets.RadioSelectHorizontal())

    ypi1 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='Often I act extra nice and sweet to get what I want, even with people I don’t like.',
        widget=widgets.RadioSelectHorizontal())

    ypi2 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='When someone asks me something, I usually have a quick answer that sounds believable, but I just made it up.',
        widget=widgets.RadioSelectHorizontal())
    ypi3 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='I will become a well-known and important person; I know that already.',
        widget=widgets.RadioSelectHorizontal())
    ypi4 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='The world would be a better place if I were the boss.',
        widget=widgets.RadioSelectHorizontal())

    ypi5 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='I like to exaggerate when I tell about something.',
        widget=widgets.RadioSelectHorizontal())
    ypi6 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='Sometimes I find myself lying for no special reason.',
        widget=widgets.RadioSelectHorizontal())
    ypi7 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='Fooling others is the best way to get what I want from them',
        widget=widgets.RadioSelectHorizontal())

    ypi8 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='It is easy for me to make other people to do things that suit me well. ',
        widget=widgets.RadioSelectHorizontal())
    ypi9 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='It is weak to feel guilty when you have hurt others.',
        widget=widgets.RadioSelectHorizontal())
    ypi10 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='Feeling bad when you have done something wrong is a waste of time.  ',
        widget=widgets.RadioSelectHorizontal())
    ypi11 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='It is weak to feel nervous or worried.',
        widget=widgets.RadioSelectHorizontal())
    ypi12 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='Feelings are less important to me than they are for others.',
        widget=widgets.RadioSelectHorizontal())
    ypi13 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='If I watch sad things on TV or in a movie, it usually does not get to me. ',
        widget=widgets.RadioSelectHorizontal())
    ypi14 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='When others are sad, I don’t really care.',
        widget=widgets.RadioSelectHorizontal())
    ypi15 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='I like to do things just because they feel cool or exciting.',
        widget=widgets.RadioSelectHorizontal())
    ypi16 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='I like to get into situations that give me a thrill.',
        widget=widgets.RadioSelectHorizontal())

    ypi17 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='It often happens that I do things without thinking ahead.',
        widget=widgets.RadioSelectHorizontal())
    ypi18 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='I prefer to spend my money right away rather than save it.',
        widget=widgets.RadioSelectHorizontal())
    ypi19 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='I find rules to be nothing but a nuisance.',
        widget=widgets.RadioSelectHorizontal())

    ypi20 = models.CharField(
        choices=['1', '2', '3', '4', '5'],
        verbose_name='I don’t think it is necessary to tell my parents what I am going to do when I go outside.',
        widget=widgets.RadioSelectHorizontal())

    religion = models.PositiveIntegerField(
        verbose_name='''
        How many times have you attended religious services during the past year?
            ''',
        min=0, max=100
    )

    religion1 = models.CharField(
        choices=['Prayer is a regular part of my daily life','I usually pray in times of stress or need but rarely at any other time','I pray only during formal ceremonies','I never pray'],
        verbose_name='Which of the following best describes your practice of prayer or religious meditation',
        widget=widgets.RadioSelect())

    religion2 = models.CharField(
        choices=['Almost always',
                 'Usually',
                 'Sometimes', 'Never'],
        verbose_name='When you have serious personal problem how often do you take religious advice or teaching into consideration?',
        widget=widgets.RadioSelect())

    religion3 = models.CharField(
        choices=['Prayer is a regular part of my daily life',
                 'I usually pray in times of stress or need but rarely at any other time',
                 'I pray only during formal ceremonies', 'I never pray'],
        verbose_name= 'Which of the following best describes your practice of prayer or religious meditation ?',
        widget=widgets.RadioSelect())

    religion4 = models.CharField(
        choices=['No influence',
                 'A small influence',
                 'Some influence', 'A fair amount of influence','A large influence'],
        verbose_name='How much influence would you say that religion has on the way that you choose to act and the way that you choose to spend your time each day ?',
        widget=widgets.RadioSelect())

    religion5 = models.CharField(
        choices=['I am sure that god really exists and that He is active in my life',
                 'Although I sometimes question His existence I do believe in God and believe He knows me as a Person',
                 'I don’t know if there is a personal God, but I do believe in a higher power of some kind',
                 'I don’t know if there is a personal God, or a higher power in some kind and I don’t know if I ever will',
                 'I don’t believe in a personal God or in a higher power'],
        verbose_name='Which of the following statements comes closest to your belief about God?',
        widget=widgets.RadioSelect())

    religion6 = models.CharField(
        choices=['I believe in a personal life after death, a soul existing as a specific individual spirit',
                 'I believe in a soul existing after death as a part of a universal spirit',
                 'I believe in a life after death of some kind, but I really don’t know what it would be like',
                 'I don’t know whether there is any kind of life after death and aI don’t know if I will ever know',
                 'I don’t believe in any kind of life after death'],
        verbose_name='Which of the following statements comes closest to your belief about life after death (immortality)',
        widget=widgets.RadioSelect())

    religion7 = models.CharField(
        choices=['Almost daily',
                 'Frequently',
                 'Sometimes', 'Rarely', 'Never'],
        verbose_name='During the past year, how often have you experienced a feeling of religious reverence of devotion?',
        widget=widgets.RadioSelect())
