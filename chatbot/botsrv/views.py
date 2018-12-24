import json
from rest_framework import authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.ext.django_chatterbot import settings


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening

class Chat(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    #permission_classes = (permissions.IsAdminUser,)
    chatterbot = ChatBot(**settings.CHATTERBOT)

    #@api_view(['POST'])
    #@schema(None)
    def post(self, request, format=None): 
      # Get a response to an input statement
      input_data = json.loads(request.body.decode('utf-8'))
      
      response = self.chatterbot.get_response(input_data)
      response_data = response.serialize()
      return Response(response_data)