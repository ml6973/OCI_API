import apiModules.apiAuth as apiAuth
import apiModules.apiEmotion as apiEmotion
import api.models as modelFunctions
from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer


# Returns a JSON containing emotional attributes
class Image(APIView):
    def post(self, request):
        if apiAuth.auth(request.META.get('HTTP_API_UNAME'),
                        request.META.get('HTTP_API_PASS')) is False:
           return Response(status=status.HTTP_401_UNAUTHORIZED)

	try:
	    image = ContentFile(request.FILES["image"].read())
	except KeyError:
	    return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

	return HttpResponse(image, status=status.HTTP_200_OK, content_type='application/octet-stream')

    def get(self, request):
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
