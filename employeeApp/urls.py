from django.urls import path
from employeeApp import views

app_name = 'empapp'

urlpatterns = [
    path('',views.index,name='home'),
]