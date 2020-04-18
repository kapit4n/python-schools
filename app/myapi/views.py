from django.shortcuts import render
from rest_framework import viewsets

from .serializers import HeroSerializer
from .serializers import ProjectSerializer
from .models import Hero
from .models import Project
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class HeroViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('name')
    serializer_class = ProjectSerializer