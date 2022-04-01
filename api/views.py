from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import HabitSerializer, UserSerializer, ResultSerializer, HabitResultSerializer
from habit.models import Habit, Result, User
from rest_framework import generics

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'habit': reverse('habit-list', request=request, format=format),
        'result': reverse('result-list', request=request, format=format)
    })


class HabitList(generics.ListCreateAPIView): 
	queryset = Habit.objects.all()
	serializer_class = HabitSerializer


class HabitDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Habit.objects.all()
	serializer_class = HabitSerializer

class HabitResultDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Habit.objects.all()
	queryset2 = Result.objects.all()
	serializer_class = HabitResultSerializer

class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class ResultList(generics.ListCreateAPIView): 
	queryset = Result.objects.all()
	serializer_class = ResultSerializer

class ResultDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Result.objects.all()
	serializer_class = ResultSerializer
