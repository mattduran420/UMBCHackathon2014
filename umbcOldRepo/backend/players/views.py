from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework.decorators import api_view, authentication_classes,parser_classes

from players.models import *
from players.serializers import *

class PlayerViewSet(viewsets.ModelViewSet):
    model = Player
    serializer = PlayerSerializer


@api_view(['GET','POST'])
@authentication_classes([authentication.TokenAuthentication])
def profile(request):
	user = request.user;
	player = Player.objects.filter(user=user)
	return Response(PlayerSerializer(player[0]).data)