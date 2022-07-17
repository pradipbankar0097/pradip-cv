from datetime import date
from email.policy import default
from django.db import models
from django.utils.timezone import now


class Project(models.Model):
    name = models.CharField(max_length=200, default="project 1")
    domain = models.CharField(max_length=200,default="Machine Learning")
    small_desc = models.TextField(default="small description")
    large_desc = models.TextField(default="large description")
    start_date = models.DateField()
    end_date = models.DateField()
    source_link = models.CharField(max_length=200, default="https://www.google.com")
    deployment_link = models.CharField(max_length=200, default="https://www.google.com")
    tags = models.CharField(max_length=700,default="MySQL,Python,ML,")
    project_banner = models.ImageField(upload_to="uploads/project/banners", default=None)
    screenshot1 = models.ImageField(upload_to="uploads/screenshots",null=True)
    screenshot2 = models.ImageField(upload_to="uploads/screenshots",null=True)
    screenshot3 = models.ImageField(upload_to="uploads/screenshots",null=True)
    screenshot4 = models.ImageField(upload_to="uploads/screenshots",null=True)
    visible_on_resume = models.BooleanField(default=True)
    visible_on_cv = models.BooleanField(default=True)

class MyDetails(models.Model):
    name_id = models.CharField(max_length=50,default='pradip')
    name = models.CharField(max_length=100, default="Pradip Bankar")
    about_me = models.TextField(default="<b>Lorem</b> ipsum dolor sit amet, consectetur adipiscing elit. Duis interdum ante a porta blandit.<input type='text' placeholder='testing'/> Quisque velit tortor, ultricies in quam ut, luctus convallis metus. Nunc vitae felis rutrum, mattis justo quis, bibendum tellus. Integer bibendum eget dolor nec venenatis. Aliquam erat volutpat. Etiam et est vitae turpis accumsan vulputate. Curabitur et vehicula nisl, eu congue dolor. Vivamus nec hendrerit mi Nulla consequat tempor.")
    photo = models.ImageField(upload_to='static/images/profile_pic')
    no_of_projects = models.IntegerField(default=0)
    no_of_internships = models.IntegerField(default=0)
    no_of_academic_projects = models.IntegerField(default=0)
    no_of_paid_projects = models.IntegerField(default=0)
    skills = models.CharField(max_length=1000,default='C/C++,Python,Java,SQL,MongoDB')

class Experience(models.Model):
    role = models.CharField(max_length=200,default='developer')
    start_date = models.DateField(default=now)
    end_date = models.DateField(default=now)
    about = models.TextField(default='learned so many things')
    # comma(,) seperated tags related to the experience
    tags = models.CharField(max_length=1000,default='React,MongoDB')
    company = models.CharField(max_length=200,default='microsoft')
    location = models.CharField(max_length=300,default='Aurangabad, Maharashtra')
    presently_working = models.BooleanField(default=True)
    visible_on_resume = models.BooleanField(default=True)
    visible_on_cv = models.BooleanField(default=True)

class Internship(Experience):
    stipend = models.IntegerField(default=15000)
    
class Job(Experience):
    salary = models.IntegerField(default=30000)
