from django.conf.urls import url
from . import views
from django.urls import path
from .rest_services import api_all_records_of_student_database, api_first_record_of_student_database
from .rest_services import faculty_heighest_student_count

urlpatterns = [
    url(r'^$', views.index),
    path('greet/', views.greetings),
    path('maximum/', views.maximum_mathematics),
    path('average/', views.average_of_each_subject),
    path('heighest/', views.heighest_pass_percentage),
    path('top_student/', views.top_student),
    path('least_student/', views.least_student),
    path('least_faculty/', views.least_pass_percentage),
    path('student_count/', views.faculty_heighest_student_count),
]
