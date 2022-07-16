from django.http import HttpRequest
from django.shortcuts import render
from .models import MyDetails



def index(request:HttpRequest):
    my_data = MyDetails.objects.get(name_id='pradip')
    data = {
        "about_me" : my_data.about_me,
        "number_of_projects":my_data.no_of_projects,
        "number_of_internships":my_data.no_of_internships,
        "skills" : my_data.skills.split(',')

    }
    return render(request,'index.html',data)

def work_detail(request):
    return render(request,'works-setails.html')
