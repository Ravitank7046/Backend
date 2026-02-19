from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from api.models import Student
from api.serializers import StudentSerializers


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_api(request):
  if request.method == 'GET':
    id = request.data.get('id')
    if id is not None:
      stu = Student.objects.get(id=id)
      serializers = StudentSerializers(stu)
      return Response(serializers.data)
    stu = Student.objects.all()
    serializers = StudentSerializers(stu, many=True)
    return Response(serializers.data)

  if request.method == "POST":
    serializers = StudentSerializers(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response({"Message": "Data Create Successfully"})
    return Response(serializers.errors)

  if request.method == "PUT":
    id = request.data.get('id')
    stu = Student.objects.get(pk=id)
    serializers = StudentSerializers(stu, data=request.data, partial=True)
    if serializers.is_valid():
      serializers.save()
      return Response({"Message": "Data Update Successfully"})
    return Response(serializers.errors)

  if request.method == "DELETE":
    id = request.data.get('id')
    stu = Student.objects.get(pk=id)
    stu.delete()
    return Response({"Message":"Data Delete Successfully"})