from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
from .models import Student
from .serializers import StudentSerializers

@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        id = pythonData.get('id',None)
        if id is not None:
            stu = Student.objects.get(id=id)
            ser = StudentSerializers(stu)
            json_data = JSONRenderer().render(ser.data)
            return HttpResponse(json_data,content_type='application/json')
        stu = Student.objects.all()
        ser = StudentSerializers(stu,many=True)
        json_data = JSONRenderer().render(ser.data)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        serializer = StudentSerializers(data=pythonData)
        if serializer.is_valid():
            serializer.save()
            res = {'message':'Data Create Successfully'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json') 