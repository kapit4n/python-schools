# serializers.py
from rest_framework import serializers

from .models import Project
from .models import EmployeeRole
from .models import Employee
from .models import Contract
from .models import Team
from .models import TeamMember

class EmployeeRoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmployeeRole
        fields = ('name', 'description')

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('name', 'phone', 'role')

class ContractSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contract
        fields = ('salary', 'contract_date', 'employee')

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('name', 'description')

class TeamMemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeamMember
        fields = ('team', 'employee')

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'description', 'lead', 'team')

