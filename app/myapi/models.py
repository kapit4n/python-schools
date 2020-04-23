from django.db import models

# Create your models here.

class EmployeeRole(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    role = models.ForeignKey(EmployeeRole, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Contract(models.Model):
    contract_date = models.DateTimeField('')
    salary = models.IntegerField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    def __str__(self):
        return self.salary

class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    lead = models.ForeignKey(Employee, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    def __str__(self):
        return self.team


