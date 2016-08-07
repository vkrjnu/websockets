from django.shortcuts import render
from django.views.generic import View
from django.template import RequestContext
from django.http import HttpResponse
from game.models import *
import uuid
from django.contrib import messages


class PlayGame(View):
    def get(self, request):
        """
        render game
        :param request:
        :return:
        """
        context = RequestContext(request, {
            'rows' : range(0,8),
            'cols' : range(0,8),
        })
        return render(request, 'game/game.html', context_instance=context)


class GameLogin(View):
    def get(self, request):
        """
        login
        :param request:
        :return:
        """
        context = RequestContext(request, {})
        return render(request, 'game/login.html', context_instance=context)

    def post(self, request):
        """
        get user name
        :param request:
        :return:
        """
        username = request.POST.get('user', '')
        if Game.objects.filter(playing=1).exists():
            game = Game.objects.get(playing= 1)
            game.playing = 2
            game.save()
            player = Player.objects.create(name=username, game=game)
            color = Color.objects.create(color='blue', player=player, count=0)
        else:
            game_name = uuid.uuid4()
            game = Game.objects.create(playing=1, game_name=game_name)
            player = Player.objects.create(name=username, game=game)
            color = Color.objects.create(color='red', player=player, count=0)
        messages.add_message(request, messages.INFO, player.id)
        return HttpResponse('/game/'+str(game.game_name)+'/')