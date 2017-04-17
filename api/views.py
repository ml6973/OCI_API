import apiModules.apiAuth as apiAuth
import apiModules.apiEmotion as apiEmotion
import api.models as modelFunctions
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer


# Returns a JSON containing emotional attributes
class Emotion(APIView):
    def get(self, request):
        if apiAuth.auth(request.META.get('HTTP_API_UNAME'),
                        request.META.get('HTTP_API_PASS')) is False:
           print request.META.get('HTTP_API_UNAME') + " " + request.META.get('HTTP_API_PASS')
           return Response(status=status.HTTP_401_UNAUTHORIZED)

        emotionJson = apiEmotion.emotion(request.data)
        return Response(emotionJson)

    def post(self, request):
        pass
