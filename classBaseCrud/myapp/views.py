from django.views.generic import (
    CreateView, ListView, DetailView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from myapp.models import Student


class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'email', 'roll']
    template_name = "myapp/student_form.html"
    success_url = reverse_lazy('student_list')


class StudentListView(ListView):
    model = Student
    template_name = "myapp/student_list.html"
    context_object_name = "students"


class StudentDetailView(DetailView):
    model = Student
    template_name = "myapp/student_detail.html"
    context_object_name = "student"


class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'email', 'roll']
    template_name = "myapp/student_form.html"
    success_url = reverse_lazy('student_list')


class StudentDeleteView(DeleteView):
    model = Student
    template_name = "myapp/student_confirm_delete.html"
    success_url = reverse_lazy('student_list')
