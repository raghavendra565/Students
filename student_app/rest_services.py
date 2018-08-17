from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import path
from django.conf.urls import url
from .models import Students, Subjects
from django.http import JsonResponse
from django.db.models import *

from .serializers import StudentSerializer
from .serializers import SubjectSerializer


@api_view(['GET'])
def api_first_record_of_student_database(request):
    obj = Students.objects.first()
    if obj:
    	serializer = StudentSerializer(obj)
    	return Response(serializer.data)
    else:
    	return Response({"Message": 'Record Not Foud'})


@api_view(['GET'])
def api_all_records_of_student_database(request):
    obj = Students.objects.all()
    #obj = Students.objects.get(name = 'student1')
    if obj:
    	serializer = StudentSerializer(obj, many=True)
    	return Response(serializer.data)
    else:
    	return Response({"Message": 'Record Not Foud'})


@api_view(['GET'])
def faculty_heighest_student_count(request):
    obj = Students.objects.filter(marks__gte=90).values("subject").annotate(average = Count('subject')).order_by('-average')[:1]
    sub = obj.values_list('subject', flat=True)
    obj1 = Subjects.objects.filter(subject=sub[0]).values('faculty')
    context = {'Faculty with heighest student count with marks greater than 90 is':{'faculty': list(obj1)}}
    return JsonResponse(context)

@api_view(['POST'])
def api_add_new_student(request):
    name = request.POST.get("name")
    subject = request.POST.get("subject")
    marks = request.POST.get("marks")
    student = Students.objects.create(name=name, subject=subject, marks=marks)

    return Response({'message': 'student {:d} created'.format(student.id)}, status=301)

urlpatterns = [
    #url(r'^(?P<_name>[A-Za-z%]+)/$', e),
    path('first/', api_first_record_of_student_database),
    path('all/', api_all_records_of_student_database),
    path('add/', api_add_new_student),
    path('faculty/', faculty_heighest_student_count),
    #url(r'^(?P<_range>[0-9,-]+)',get_articles_range),
]
