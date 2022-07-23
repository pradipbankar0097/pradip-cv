from django.http import HttpRequest
from django.shortcuts import render
from cvhome.models import MyDetails, Internship, Education

def index(request:HttpRequest):
    my_data = MyDetails.objects.get(name_id='pradip')
    experiences = Internship.objects.all()
    all_edu = Education.objects.all()
    print(my_data)
    return render(request,'resume_base.html',{
        'my_data' : my_data,
        'experiences' : experiences,
        'all_edu':all_edu,
    })

