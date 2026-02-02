from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.contrib import contenttypes
from django.template.context_processors import request
from .models import Student
from .serializers import StudentSerializer

def student_details(request,pk):
    stu = Student.objects.get(id=pk)
    ser = StudentSerializer(stu)
    json_data = JSONRenderer().render(ser.data)
    return HttpResponse(json_data,content_type='application/json')


def student_Alldetails(request):
    stu = Student.objects.all()
    ser = StudentSerializer(stu,many=True)
    json = JSONRenderer().render(ser.data)
    return HttpResponse(json,content_type='application/json') 