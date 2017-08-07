import apiModules.apiAuth as apiAuth
import api.models as modelFunctions
from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer


# Import your Machine Learning module here


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

	# Change the following line so that it calls your function, ensure your function returns the image as a byte string
	
	# Example:  
	#returnimage, results = getFaces(image)
	
	returnimage = image

	# Use the following line only if you do not need to send addition JSON data back to the client
	results = None
	
	response = HttpResponse(returnimage, status=status.HTTP_200_OK, content_type='application/octet-stream')
	response['Results'] = results
	return response

    def get(self, request):
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
