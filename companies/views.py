from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import stock
from .serializers import stockSerializer


# Create your views here.
#list all stocks or create a new one
class stockList(APIView):
	
	def get(self,request):
		stocks=stock.objects.all()
		serializer=stockSerializer(stocks,many=True)
		return Response(serializer.data)

	def post(self):
		pass
