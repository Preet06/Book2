from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Book

from django.views.generic.base import TemplateView
# Create your views here.


def home_page(request):
      if request.method == 'GET':
          Language = request.GET.getlist('Language')
          Genre = request.GET.getlist('Genre')
          data = Book.objects.all()
          lan = Book.objects.values('Language').distinct() 
          print(lan)
          gen = Book.objects.values('Genre').distinct() 
          print(gen)
          if len(Language)!=0:
                  print(Language)
                  data=data.filter(Language__in=Language)
          if len(Genre)!=0:
                  print(Genre)
                  data=data.filter(Genre__in=Genre)           
          stu = {
            "data": data
          }
          return render(request, 'home.html',{"data": data  , "lan":lan  ,"gen":gen  })
      else:
          data = Book.objects.all()
          lan = Book.objects.values('Language').distinct()
          gen = Book.objects.values('Genre').distinct()    
          stu = {
            "data": data
          }
          return render(request, 'home.html',{"data": data  , "lan":lan  ,"gen":gen  })




class BookCreateView(CreateView):
    model = Book
    template_name = 'add.html'
    fields = ['Book_Name', 'Author', 'Genre','Language']


   
class Intro(TemplateView):
    template_name = 'home.html'
    def get_context_data(self,*args, **kwargs):
        context = super(Intro, self).get_context_data(*args,**kwargs)
        context['users'] = Book.objects.values('Language').distinct() 
        return context