from django.shortcuts import render, HttpResponse
from core.models import Project, Contact
from core.forms import ContactForm


# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def portfolio(request):
    
    portfolio=Project.objects.all()
    contexto = {"portfolio": portfolio}
    return render( request, "core/portfolio.html",contexto)

def contact(request):
    
    if request.method == 'POST':
        misContactos = ContactForm(request.POST)
        
        if misContactos.is_valid():
            
            dato = misContactos.cleaned_data
            
            contact = Contact(name=dato['name'], email=dato['email'],subject =dato['subject'], message=dato['message'])
            contact.save()
            
            
            return render(request, "core/home.html")
        
    else:
                   
        misContactos = ContactForm()
            
    return render(request, "core/contact.html", {"misContactos":misContactos})
    
    
               
       
  
def javiermmsierra(request):
    return render(request, "core/javiermmsierra.html")