from django.shortcuts import render
from .serializers import toDoSerializer, UserSerializer
from .models import User, ToDo
from rest_framework import viewsets


# Create your views here.
class displayToDo(viewsets.ModelViewSet):
  serializer_class = toDoSerializer
  queryset = ToDo.objects.all()
