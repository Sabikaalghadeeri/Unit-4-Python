from django.shortcuts import render
from django.http import HttpResponse
# main_app/views.py
from .models import Finch
from django.views.generic.edit import CreateView, UpdateView, DeleteView



class FinchUpdate(UpdateView):
  model = Finch
  fields = ['breed','description', 'age']
  
  
class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finchs/'

  
  
class FinchCreate(CreateView):
  model = Finch
  fields = '__all__' 
  success_url = '/finchs/'
  
  
  

def finchs_detail(request, finch_id):
  finch = Finch.objects.get(id = finch_id)
  return render (request, 'detail.html', {'finch': finch})


def finchs_index(request):
    finchs_list = Finch.objects.all()
    return render(request, 'finchs/index.html', {'Finchs': finchs_list})

def about(request):
  return render(request, 'about.html')
# Define the home view
def home(request):
    return render(request, 'home.html')
  
  # return HttpResponse('<h1>Hello Finch Bird</h1>')

# def about(request):
#     return HttpResponse('<h1>About My Finchs</h1>') 