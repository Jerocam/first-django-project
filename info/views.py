from django.shortcuts import render
from .models import Jobs, Countries, Employees

def jobinfo(request):
    job = Jobs.objects.all()
    cy = Countries.objects.all()
    em = Employees.objects.all()
    return render(request,'jobdetails.html',{'jinfo': job, 'cinfo':cy, 'eminfo':em})
