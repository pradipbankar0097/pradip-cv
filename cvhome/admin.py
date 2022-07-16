from django.contrib import admin
from .models import *
from tinymce.widgets import TinyMCE
from django.db import models


class ProjectAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

class MyDetailsAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

class InternshipAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

class JobAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }




admin.site.register(Project,ProjectAdmin)
admin.site.register(MyDetails,MyDetailsAdmin)
admin.site.register(Internship,InternshipAdmin)
admin.site.register(Job,JobAdmin)
