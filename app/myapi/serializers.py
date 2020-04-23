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
        fields = ('id', 'name', 'description')

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    role = EmployeeRoleSerializer(many=False, read_only=True)

    class Meta:
        model = Employee
        fields = ('id', 'name', 'phone', 'role')

class ContractSerializer(serializers.HyperlinkedModelSerializer):
    employee = EmployeeSerializer(many=False, read_only=True)
    class Meta:
        model = Contract
        fields = ('id', 'salary', 'contract_date', 'employee')

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name', 'description')

class TeamMemberSerializer(serializers.HyperlinkedModelSerializer):
    employee = EmployeeSerializer(many=False, read_only=True)
    team = TeamSerializer(many=False, read_only=True)

    class Meta:
        model = TeamMember
        fields = ('id', 'team', 'employee')

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    lead = EmployeeSerializer(many=False, read_only=True)
    team = TeamSerializer(many=False, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'lead', 'team')

