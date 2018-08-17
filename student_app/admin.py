from django.contrib import admin


# Register your models here.
from .models import Students, Subjects

class StudentDetails(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject', 'marks')
    search_fields = ('name', 'subject')

admin.site.register(Students, StudentDetails)

class FacultyDetails(admin.ModelAdmin):
    list_display = ('id', 'subject', 'faculty')
    search_fields = ('faculty', 'subject')

admin.site.register(Subjects, FacultyDetails)
