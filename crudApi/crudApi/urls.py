from django.contrib import admin
from django.urls import path
from api.views import student_api
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentApi/',student_api,name="student_api"),
    path('studentApi/<int:pk>',student_api,name="student_api")

]
