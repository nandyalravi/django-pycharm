from django.shortcuts import render
from MyApps1.models import Student

from django.urls import reverse_lazy	#new-lib
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
# Create your views here.
class StudentListView(ListView):
    model = Student

class StudentDetailView(DetailView):
    model = Student

class StudentCreateView(CreateView):
    model =Student
    #fields=('rollno', 'name','dob', 'marks', 'email', 'phonenumber', 'address')
    fields = '__all__'

class StudentUpdateView(UpdateView):
    model = Student
    fields = ('name','dob', 'marks', 'email', 'phonenumber', 'address')

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('home')