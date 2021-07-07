from django.urls import path
from . import views
from .views import BookCreateView


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('add', BookCreateView.as_view(), name='add'),
]