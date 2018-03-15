from channels import Group
from channels.generic.websockets import WebsocketConsumer
from ball_catch.models import Player, Constants
import json
from random import randint
import datetime
from datetime import timezone


class TaskTracker(WebsocketConsumer):
    url_pattern = (
        r'^/tasktracker' +
        '/participant/(?P<participant_code>[a-zA-Z0-9_-]+)' +
        '/player/(?P<player>[0-9]+)' +
        '$')

    def clean_kwargs(self):
        self.player = self.kwargs['player']
        self.participant = self.kwargs['participant_code']

    def receive(self, text=None, bytes=None, **kwargs):
        self.clean_kwargs()
        player = Player.objects.get(pk=self.player, participant__code=self.participant)
        jsontext = json.loads(text)
        date = jsontext.get('start_date')
        game_over = jsontext.get('game_over')
        msg = dict()
        if date:

            python_date = datetime.datetime.fromtimestamp(date / 1000.0).replace(tzinfo=timezone.utc)
            if player.work_timer is None:
                msg['game_start'] = True
                player.work_timer = python_date
                player.save()
            millisec = int((player.work_timer.replace(tzinfo=timezone.utc).timestamp() + Constants.ret_timer) * 1000)
            msg['milleseconds'] = millisec
            self.send(msg)
        if game_over:
            player.catches = jsontext.get('catches')
            player.clicks = jsontext.get('clicks')
            player.score = jsontext.get('score')
            player.expense = jsontext.get('expense')
            player.save()

    def connect(self, message, **kwargs):
        self.clean_kwargs()
        print('client connected')

    def disconnect(self, message, **kwargs):
        print('client DISconnected')

    def send(self, content):
        self.message.reply_channel.send({'text': json.dumps(content)})
