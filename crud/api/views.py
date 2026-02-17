from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
from .models import Student
from .serializers import StudentSerializers
from .models import Student
from django.utils.decorators import method_decorator
from django.views import View


@method_decorator(csrf_exempt,name='dispatch')
class StundentApi(View):
    def get(self,request,*args,**kwargs):
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

    def post(self,request,*args,**kwargs):
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
    
    def put(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        ser = StudentSerializers(stu,data=pythondata,partial=True)
        if ser.is_valid():
            ser.save()
            res = {'msg':"Data Updated Successfully"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(ser.errors)
        return HttpResponse(json_data,content_type='application/json') 
    
    def delete(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'Message':"Data Delete Successfully"}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json') 
    
        