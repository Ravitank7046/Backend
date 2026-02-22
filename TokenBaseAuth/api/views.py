from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from api.models import Student
from api.serializers import StudentSerializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]














  
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
