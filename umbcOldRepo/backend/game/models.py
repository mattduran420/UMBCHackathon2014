from django.db import models
from game.models import *
from players.models import *


class Question(models.Model):
	text = models.TextField()

	def __unicode__(self):
		return self.text

class Game(models.Model):
	timeBegin = models.DateTimeField(auto_now_add=True)
	channelName = models.CharField(max_length=100)
	gameStatus = models.CharField(max_length=50)
	gameMembers = models.ManyToManyField(Player)
	question = models.ForeignKey(Question)

	def __unicode__(self):
		return self.channelName

class GameEndResult(models.Model):
	time_end = models.DateTimeField(auto_now_add=True)
	position = models.IntegerField()
	player = models.ForeignKey(Player)
	game = models.ForeignKey(Game)

	def __unicode__(self):
		return str(self.position) + " | " + self.game.__unicode__() + " | " + self.player.__unicode__()


class QuestionUnitTest(models.Model):
	firstInput = models.CharField(max_length=50)
	secondInput = models.CharField(max_length=50)
	result = models.CharField(max_length=300)
	question = models.ForeignKey(Question)

	def __unicode__(self):
		return self.firstInput + " | " + self.secondInput + " | " + self.result + " | " + self.question.__unicode__()