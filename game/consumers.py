import re
import json
import logging
from channels import Group
from channels.sessions import channel_session
from .models import *

log = logging.getLogger(__name__)


@channel_session
def ws_connect(message):
    """
    Websocket connect
    :param message:
    :return:
    """
    prefix, label = message['path'].decode('ascii').strip('/').split('/')
    log.debug('Game connect')
    Group('game-'+label, channel_layer=message.channel_layer).add(message.reply_channel)
    message.channel_session['game'] = label


@channel_session
def ws_receive(message):
    """
    Websocket recieve
    :param message:
    :return:
    """
    label = message.channel_session['game']
    d = json.loads(message['text'])
    grid_cell = d['row_col'].split(":")
    game = Game.objects.get(game_name=label)
    player = Player.objects.get(id=d['player'])
    if Color.objects.filter(player=player).exists():
        color = Color.objects.get(player=player)
        color.count += 1
        color.save()
    game_color = GamePlayer.objects.create(row=grid_cell[0], col=grid_cell[1], player=player)
    data = {'row':grid_cell[0], 'col':grid_cell[1], 'color':color.color}
    Group('game-'+label, channel_layer=message.channel_layer).send({'text': json.dumps(data)})


@channel_session
def ws_disconnect(message):
    """
    Websocket disconnect
    :param message:
    :return:
    """
    try:
        label = message.channel_session['game']
        Group('game-'+label, channel_layer=message.channel_layer).discard(message.reply_channel)
    except:
        pass