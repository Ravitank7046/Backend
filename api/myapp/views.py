from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from django.contrib import contenttypes
from django.template.context_processors import request
from .models import Student
from .serializers import StudentSerializer

def student_details(request,pk):
    stu = Student.objects.get(id=pk)
    ser = StudentSerializer(stu)
    return JsonResponse(ser.data)

def student_Alldetails(request):
    stu = Student.objects.all()
    ser = StudentSerializer(stu,many=True)
    return JsonResponse(ser.data) 