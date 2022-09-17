from django.shortcuts import render, redirect

from .forms import BarForm, CommentForm

# Create your views here.
from .serializers import BarSerializer, CommentSerializer, GameSerializer
from .models import Bar, Comment, Games
from django.http import JsonResponse
from rest_framework import generics

from find import serializers
from django.views.decorators.csrf import csrf_exempt




class BarList(generics.ListCreateAPIView): 
    queryset=Bar.objects.all()
    serializer_class = BarSerializer
    
class BarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bar.objects.all()
    serializer_class=BarSerializer
    
class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class GameList(generics.ListCreateAPIView):
    queryset = Games.objects.all()
    serializer_class = GameSerializer

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Games.objects.all()
    serializer_class = GameSerializer