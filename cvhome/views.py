from django.http import HttpRequest
from django.shortcuts import render



def index(request:HttpRequest):
    data = {
        "about_me" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis interdum ante a porta blandit. Quisque velit tortor, ultricies in quam ut, luctus convallis metus. Nunc vitae felis rutrum, mattis justo quis, bibendum tellus. Integer bibendum eget dolor nec venenatis. Aliquam erat volutpat. Etiam et est vitae turpis accumsan vulputate. Curabitur et vehicula nisl, eu congue dolor. Vivamus nec hendrerit mi Nulla consequat tempor.",
        "number_of_projects":40,
        "number_of_internships":40,
        "skills" : "JavaScript, Node.js, Express.js, MongoDB, Vue.js, React, Sequelize, Github, HTML".split(', ')

    }
    return render(request,'index.html',data)

def work_detail(request):
    return render(request,'works-setails.html')
