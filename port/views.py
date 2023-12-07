from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt


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



from .models import ContactForm


@csrf_exempt

def submit_form(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        ContactForm.objects.create(name=name, email=email, message=message)

        return HttpResponse('Form submitted successfully!')
    else:
        return render(request, 'forms.html')

