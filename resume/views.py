from django.shortcuts import render
from .models import ClientProfile


# Create your views here.
def resume_generator(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('number', '')
        objective = request.POST.get('objective')
        school = request.POST.get('school')
        university = request.POST.get('university')
        experience = request.POST.get('experience')
        experience2 = request.POST.get('experience2')
        experience3 = request.POST.get('experience3')
        skills = request.POST.get('skills')
        print(name)
        print(email)
        print(phone)
        print(objective)

        profile = ClientProfile(name=name, email=email, phone=phone, objective=objective, school=school,
                                university=university, experience=experience, experience2=experience2,
                                experience3=experience3, skills=skills)
        profile.save()
    return render(request, 'resume/form.html')
