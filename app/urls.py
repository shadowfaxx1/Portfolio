from . import views
from django.urls import path

app_name = "app"


urlpatterns=  [
    path("",views.home,name='home'),
    path("project/",views.temp,name='project'),
    path("extra",views.temp2,name='extra'),
    path("landing",views.temp3,name='landing'),
    
]

