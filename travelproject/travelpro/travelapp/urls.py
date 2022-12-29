
from django.urls import path,include

from . import views

urlpatterns = [

    path('',views.tfun,name='tfun')
]