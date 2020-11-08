from django.urls import path
from .views import resume_generator

urlpatterns = [
    path('', resume_generator,name='resume_generator'),
]
