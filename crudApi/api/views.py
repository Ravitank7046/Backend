from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from api.models import Student
from api.serializers import StudentSerializers



class LCStudent(GenericAPIView,ListModelMixin,CreateModelMixin):
  queryset = Student.objects.all()
  serializer_class = StudentSerializers

  def get(self,request,*args,**kwargs):
    return self.list(request,*args,**kwargs)
  def post(self,request,*args,**kwargs):
    return self.create(request,*args,**kwargs)
  
class RUDStudent(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
  queryset = Student.objects.all()
  serializer_class = StudentSerializers

  def get(self,request,*args,**kwargs):
    return self.retrieve(request,*args,**kwargs)
  
  def put(self,request,*args,**kwargs):
    return self.retrieve(request,*args,**kwargs) 
  
  def delete(self,request,*args,**kwargs):
    return self.destroy(request,*args,**kwargs) 















  
#   class StudentAPI(APIView):
    # def get(self,request,pk=None,formate=None):
    #     id = pk
    #     if id is not None:
    #         stu = Student.objects.get(id=id)
    #         serializers = StudentSerializers(stu)
    #         return Response(serializers.data)
    #     stu = Student.objects.all()
    #     serializers = StudentSerializers(stu, many=True)
    #     return Response(serializers.data)
    
    # def post(self,request,formate=None):
    #     serializers = StudentSerializers(data=request.data)
    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response({"Message": "Data Create Successfully"},status=status.HTTP_201_CREATED)
    #     return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # def put(self,request,pk=None,formate=None):
    #     id = pk
    #     stu = Student.objects.get(pk=id)
    #     serializers = StudentSerializers(stu, data=request.data)
    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response({"Message": "Data Update Successfully"})
    #     return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    # def patch(self,request,pk=None,formate=None):
    #     id = pk
    #     stu = Student.objects.get(pk=id)
    #     serializers = StudentSerializers(stu, data=request.data,partial=True)
    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response({"Message": "Data Update Successfully"})
    #     return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    

    # def delete(self,request,pk=None,formate=None):
    #     id = pk
    #     stu = Student.objects.get(pk=id)
    #     stu.delete()
    #     return Response({"Message": "Data Delete Successfully"})

# def student_api(request, pk=None):
    # if request.method == 'GET':
    #     id = pk
    #     if id is not None:
    #         stu = Student.objects.get(id=id)
    #         serializers = StudentSerializers(stu)
    #         return Response(serializers.data)
    #     stu = Student.objects.all()
    #     serializers = StudentSerializers(stu, many=True)
    #     return Response(serializers.data)

    # if request.method == "POST":
    #     serializers = StudentSerializers(data=request.data)
    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response({"Message": "Data Create Successfully"},status=status.HTTP_201_CREATED)
    #     return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    # if request.method == "PUT":
    #     id = pk
    #     stu = Student.objects.get(pk=id)
    #     serializers = StudentSerializers(stu, data=request.data,)
    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response({"Message": "Data Update Successfully"})
    #     return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # if request.method == "PATCH":
    #     id = pk
    #     stu = Student.objects.get(pk=id)
    #     serializers = StudentSerializers(stu, data=request.data, partial=True)
    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response({"Message": "Data Update Successfully (Partially)"})
    #     return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    # if request.method == "DELETE":
    #     id = pk
    #     stu = Student.objects.get(pk=id)
    #     stu.delete()
    #     return Response({"Message": "Data Delete Successfully"})
