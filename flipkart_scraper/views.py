from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from bs4 import BeautifulSoup
import requests


# Create your views here.

class ScrapingView(APIView):
    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            return Response({"error": "User not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
        
        url = request.data.get('url')
        if not url:
            return Response({"error": "URL not provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        response = requests.get(url)
        if response.status_code != 200:
            return Response({"error": "Invalid URL"}, status=status.HTTP_400_BAD_REQUEST)
        
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract necessary data from the HTML using BeautifulSoup
        
        product_data = {
            # Populate the fields based on the scraped data
        }
        
        serializer = ProductSerializer(data={**product_data, "user": user.id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)