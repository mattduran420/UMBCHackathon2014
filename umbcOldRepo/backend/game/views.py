from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework.decorators import api_view, authentication_classes,parser_classes

from players.models import *
from players.serializers import *
from game.models import *
from game.serializers import *

from random import randrange


class GameViewSet(viewsets.ModelViewSet):
    model = Game
    serializer = GameSerializer


@api_view(['GET','POST'])
@authentication_classes([authentication.TokenAuthentication])
def game(request):
	return Response("HELLO!")


@api_view(['GET','POST'])
@authentication_classes([authentication.TokenAuthentication])
def searchGame(request):
	notFull = Game.objects.filter(gameStatus="notFull")
	pending = Game.objects.filter(gameStatus="pending")
	games = notFull | pending
	availableGames = []
	chosenGame = None
	CurrentMinGameSize = 0
	for game in games:
		gameObject = game
		game = GameSerializer(game).data
		availableGames.append(game)
		if(len(game['gameMembers']) > CurrentMinGameSize):
			isInArray = False
			for user in game['gameMembers']:
				if(request.user.id == user['user']['id']):
					isInArray = True
					unitTests = QuestionUnitTest.objects.filter(question=gameObject.question)
					game['unitTests'] = [QuestionUnitTestSerializer(unitTests[0]).data]
					return Response(game)
			if(isInArray == False):
				CurrentMinGameSize = len(game['gameMembers'])
				unitTests = QuestionUnitTest.objects.filter(question=gameObject.question)
				game['unitTests'] = [QuestionUnitTestSerializer(unitTests[0]).data]
				chosenGame = game
				unitTests = QuestionUnitTest.objects.filter(question=gameObject.question)
				gameObject.gameMembers.add(Player.objects.filter(user=request.user)[0])
			return Response(chosenGame)
	if(chosenGame == None):
		chosenQuestion = Question.objects.all()
		#return Response(chosenQuestion)
		generated = 1
		if(len(chosenQuestion) > 1):
			generated = randrange(0,len(chosenQuestion))

		chosenQuestion = Question.objects.filter(pk=generated + 1)[0]
		chosenGame = Game(
			channelName = 'umbcHack_' + str(randrange(1000,9999)),
			gameStatus = "notFull",
			question = chosenQuestion,
			)
		chosenGame.save()
		chosenGame.gameMembers.add(Player.objects.filter(user=request.user)[0])

		unitTests = QuestionUnitTest.objects.filter(question=chosenGame.question)
		game = GameSerializer(chosenGame).data
		game['unitTests'] = [QuestionUnitTestSerializer(unitTests[0]).data]
	return Response(game)


@api_view(['GET','POST'])
@authentication_classes([authentication.TokenAuthentication])
def addToGame(request):
	return Response("HELLO!")


@api_view(['GET','POST'])
@authentication_classes([authentication.TokenAuthentication])
def SendGameStatus(request):
	data = request.DATA
	game = Game.objects.filter(channelName=data['channelName'])[0]
	game.gameStatus = data['status']
	game.save()
	return Response(game.gameStatus)


