from django.urls import path
from .views import resume_generator,final

urlpatterns = [
    path('', resume_generator,name='resume_generator'),
    path('download/', final, name='final'),

]
