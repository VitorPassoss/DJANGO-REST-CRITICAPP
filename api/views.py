from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (Films,Review,TokensUser)
from .serializers import (FilmsSerializer,ReviewSeriaizer)
from rest_framework import generics,status
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from datetime import datetime, timedelta
from django.utils.timezone import make_aware
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import TokenObtainPairSerializer

class FilmView(APIView):
    #permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        try:
            all_films = Films.objects.all()
            serializer = FilmsSerializer(all_films, many=True)
            return Response({'films': serializer.data})
        except:
            return Response({'notification': "sem filmes registrados"})

    def post(self, request, format=None):
            serializer = FilmsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FilmDetail(APIView):
    #permission_classes = [IsAuthenticated]
    def get(self, request, id, format=None):
        film = Films.objects.get(pk=id)
        reviews = Review.objects.filter(books=film)
        film_serializer = FilmsSerializer(film)
        reviews_serializer = ReviewSeriaizer(reviews, many=True)
        return Response({'films': film_serializer.data, 'reviews': reviews_serializer.data})


         
class UserRegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class Reviews(APIView):
    def get(self,request,format=None):
        try:
            all_reviews = Review.objects.all()
            reviews_serializer = ReviewSeriaizer(all_reviews, many=True)
            return Response({'reviews': reviews_serializer.data})
        except:
            return Response({'notification': "Nenhum review criado."})

    def post(self, request, format=None):
            serializer = ReviewSeriaizer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class ReviewDelete(APIView):
    def get(self,request,id):
        try:
            Review.objects.get(pk=id).delete()
            return Response({'notification': "True"})
        except:
            return Response({'notification': "False"})

    


class ReviewDetail(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    def post(self,request,id):
        try:
            review = Review.objects.get(pk=id)
            serializer = ReviewSeriaizer(review, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'notification': "Error"})
        


class GetToken(TokenObtainPairView):
    def get_serializer_class(self):
        return TokenObtainPairSerializer