from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.db.models import *
from django.db.models.functions import Cast
# Create your views here.
from .models import Subjects, Students

def greetings(request):
    return HttpResponse('<h1>hi this is raghavendra</h1>')


def index(request):
    return render(request, 'index.html')

# Function to find Faculty with heighest student count who got more than 90 marks
def faculty_heighest_student_count(request):
    obj = Students.objects.filter(marks__gte=90).values("subject").annotate(average = Count('subject')).order_by('-average')[:1]
    sub = obj.values_list('subject', flat=True)
    obj1 = Subjects.objects.filter(subject=sub[0]).values('faculty')
    if obj1:
        context = {
        'heighest_count' : obj1
        }
        return render(request, 'frontpage.html', context)
    else :
        return HttpResponseNotFound("record not found")

# Function to find Maximum marks in Mathematics
def maximum_mathematics(request):
    obj = Students.objects.filter(subject = 'Mathematics').order_by('-marks')[:1]
    obj = obj.values_list('name', flat=True)
    #obj = Students.objects.get(name = 'student1')
    if obj:
        context = {
        'all_rows' : obj
        }
        return render(request, 'frontpage.html', context)
    else :
        return HttpResponseNotFound("record not found")

# Function to find Average percentage of each subject
def average_of_each_subject(request):
    obj = Students.objects.filter(marks__gte=0).values("subject").annotate(average = Cast(Sum('marks')/Count('subject'), FloatField()))
    #obj = Students.objects.get(name = 'student1')
    if obj:
        context = {
        'all_averages' : [obj]
        }
        return render(request, 'frontpage.html', context)
    else :
        return HttpResponseNotFound("record not found")

# Function to find faculty with heighest pass percentage
def heighest_pass_percentage(request):
    obj = Students.objects.filter(marks__gte=40).values("subject").annotate(average = Count('subject')).order_by('-average')[:1]
    sub = obj.values_list('subject', flat=True)
    obj1 = Subjects.objects.filter(subject=sub[0]).values('faculty')
    if obj1:
        context = {
        'heighest_faculty' : obj1
        }
        return render(request, 'frontpage.html', context)
    else :
        return HttpResponseNotFound("record not found")

# Function to find faculty with least pass percentage
def least_pass_percentage(request):
    obj = Students.objects.filter(marks__gte=40).values("subject").annotate(average = Count('subject')).order_by('average')[:1]
    sub = obj.values_list('subject', flat=True)
    obj1 = Subjects.objects.filter(subject=sub[0]).values('faculty')
    if obj1:
        context = {
        'least_faculty' : obj1
        }
        return render(request, 'frontpage.html', context)
    else :
        return HttpResponseNotFound("record not found")

#Function to find student with maximum total
def top_student(request):
    obj = Students.objects.filter(marks__gte=40).values("name").annotate(total = Sum('marks')).order_by('-total')[:1]
    #obj = Students.objects.get(name = 'student1')
    if obj:
        context = {
        'top_student' : obj
        }
        return render(request, 'frontpage.html', context)
    else :
        return HttpResponseNotFound("record not found")

# Function to find the student with Least marks
def least_student(request):
    obj = Students.objects.filter(marks__gte=0).values("name").annotate(total = Sum('marks')).order_by('total')[:1]
    #obj = Students.objects.get(name = 'student1')
    if obj:
        context = {
        'least_student' : obj
        }
        return render(request, 'frontpage.html', context)
    else :
        return HttpResponseNotFound("record not found")
