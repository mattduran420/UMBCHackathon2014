from rest_framework import serializers

from players.serializers import *


class QuestionSerializer(serializers.Serializer):
	text = serializers.CharField()


class GameSerializer(serializers.Serializer):
	timeBegin = serializers.DateTimeField()
	channelName = serializers.CharField()
	gameStatus = serializers.CharField()
	gameMembers = PlayerSerializer()
	question = QuestionSerializer()


class GameEndResultSerialzer(serializers.Serializer):
	timeEnd = serializers.DateTimeField()
	position = serializers.IntegerField()
	player = PlayerSerializer()
	game = GameSerializer()


class QuestionUnitTestSerializer(serializers.Serializer):
	firstInput = serializers.CharField()
	secondInput = serializers.CharField()
	result = serializers.CharField()
	question = QuestionSerializer()