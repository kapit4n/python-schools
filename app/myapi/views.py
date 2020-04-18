from django.shortcuts import render
from rest_framework import viewsets

from .serializers import HeroSerializer
from .serializers import ProjectSerializer
from .serializers import EmployeeRoleSerializer
from .serializers import EmployeeSerializer
from .serializers import TeamSerializer
from .serializers import TeamMemberSerializer

from .models import Hero
from .models import Project
from .models import EmployeeRole
from .models import Employee
from .models import Team
from .models import TeamMember
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class HeroViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('name')
    serializer_class = ProjectSerializer

class EmployeeRoleViewSet(viewsets.ModelViewSet):
    queryset = EmployeeRole.objects.all()
    serializer_class = EmployeeRoleSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('name')
    serializer_class = EmployeeSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all().order_by('name')
    serializer_class = TeamSerializer

class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
