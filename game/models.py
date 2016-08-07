from django.db import models

# Create your models here.


class Game(models.Model):
    playing = models.IntegerField()
    game_name =  models.CharField(max_length=50)


class Player(models.Model):
    name = models.CharField(max_length=30)
    game = models.ForeignKey(Game)


class Color(models.Model):
    player = models.ForeignKey(Player)
    color = models.CharField(max_length=50)
    count = models.IntegerField()


class GamePlayer(models.Model):
    row = models.IntegerField()
    col = models.IntegerField()
    player = models.ForeignKey(Player)