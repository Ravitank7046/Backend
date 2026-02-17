from api import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('st/',views.StundentApi.as_view(),name="student_api")
]
