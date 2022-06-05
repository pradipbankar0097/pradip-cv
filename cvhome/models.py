from datetime import date
from django.db import models
from django.forms import CharField
from django.utils import timezone

class Project(models.Model):
    name = models.CharField(max_length=200, default="project 1")
    domain = models.CharField(max_length=200,default="Machine Learning")
    small_desc = models.CharField(max_length=500, default="small description")
    large_desc = models.CharField(max_length=1500, default="large description")
    start_date = models.DateField()
    end_date = models.DateField()
    source_link = models.CharField(max_length=200, default="https://www.google.com")
    deployment_link = models.CharField(max_length=200, default="https://www.google.com")
    tags = models.CharField(max_length=700,default="MySQL,Python,ML,")
    screenshot1 = models.ImageField(upload_to="uploads/screenshots")
    screenshot2 = models.ImageField(upload_to="uploads/screenshots")
    screenshot3 = models.ImageField(upload_to="uploads/screenshots")
    screenshot4 = models.ImageField(upload_to="uploads/screenshots")

class MyDetails(models.Model):
    name_id = models.CharField(max_length=50,default='pradip')
    name = models.CharField(max_length=100, default="Pradip Bankar")
    photo = models.ImageField()

