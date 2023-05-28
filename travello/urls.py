from .views import Index, Registiration, addUser,Home, Add ,All_Place , gorod, infocountry, Newss, eachnews
from django.urls import path

urlpatterns = [
    path('home/',Home,name='home'),
    path('add',Add,name='add'),
    path('',Index, name='index'),
    path('Registiration', Registiration, name='registiration'),
    path('addUser/',addUser,name='addUser'),
    path('All_Place', All_Place, name='allplace'),
    path('gorod',gorod,name='gorod'),
    path('infocountry/<int:country_id>',infocountry,name='infocountry'),
    path('news',Newss,name='news'),
    path('eachnews/<int:news_id>',eachnews,name='eachnews')
]