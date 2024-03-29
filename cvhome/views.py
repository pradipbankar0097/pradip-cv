from django.http import HttpRequest
from django.shortcuts import render
from .models import MyDetails,Internship,Project



def index(request:HttpRequest):
    my_data = MyDetails.objects.get(name_id='pradip')
    data = {
        "about_me" : my_data.about_me,
        "number_of_projects":my_data.no_of_projects,
        "number_of_internships":my_data.no_of_internships,
        "skills" : my_data.skills.split(','),
        "experiences": Internship.objects.all(),
        "projects":Project.objects.all(),
    }
    return render(request,'index.html',data)

def work_detail(request,id:int):
    project = Project.objects.get(id=id)
    data = {
        'project':project,
    }
    return render(request,'works-setails.html',data)
