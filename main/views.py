from django.shortcuts import render, redirect
from .models import *

def index_view(request):
    context = {
        'banner': Banner.objects.last(),
        'about': About.objects.last(),
        'facts': Facts.objects.last(),
        'skill_r': Skill.objects.all().order_by("-id")[:3],
        'skill_l': Skill.objects.all().order_by("-id")[3:6],
        'resume_r':  Resumeroad.objects.all().order_by("-id")[:3],
        'resum_l':  Resumeroad.objects.all().order_by("-id")[3:6],
        'service_r': Service.objects.all().order_by("-id")[:3],
        'service_l': Service.objects.all().order_by("-id")[3:6],
        'testimonial': Testimonial.objects.all().order_by("-id"),
        'info': Info.objects.last(),
    }
    return render(request, 'index.html', context)


def create_contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
            )
    return redirect('index_url')