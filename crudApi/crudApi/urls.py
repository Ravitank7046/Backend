from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentApi/',views.LCStudent.as_view(),name="student_api"),
    path('studentApi/<int:pk>',views.RUDStudent.as_view(),name="student_api")

]
