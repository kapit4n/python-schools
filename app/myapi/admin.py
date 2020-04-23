from django.contrib import admin
from .models import EmployeeRole
from .models import Employee
from .models import Contract
from .models import Team
from .models import TeamMember
from .models import Project

# Register your models here.
admin.site.register(EmployeeRole)
admin.site.register(Employee)
admin.site.register(Contract)
admin.site.register(Team)
admin.site.register(TeamMember)
admin.site.register(Project)
