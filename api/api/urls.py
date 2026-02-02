
from django.contrib import admin
from django.urls import path
from myapp.views import student_details,student_Alldetails
urlpatterns = [
    path('admin/', admin.site.urls),
    path('st/<int:pk>',student_details),
    path('st/',student_Alldetails),
]

