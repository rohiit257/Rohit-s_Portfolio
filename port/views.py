from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def projects(request):
    return render(request,'projects.html')

def contact(request):
    return render(request,'contact.html')

def forms(request):
    return render(request,'forms.html')




# views.py
