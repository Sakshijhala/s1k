from django.shortcuts import render, HttpResponse
from home.models import Contact
# Create your views here.
def home(request):
    #return HttpResponse("This is my homepage(/)")
    context = {'name': 'sakshi', 'course': 'Django'}
    return render(request, 'home.html', context)
def about(request):
    #return HttpResponse("This is my about page(/about)")
    return render(request, 'about.html')
    
def projects(request):
    #return HttpResponse("This is my projects page(/projects)")
    return render(request, 'projects.html')
def contact(request):
    if request.method=="POST":
        print("This is post")
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        #print(name, phone, email)
        contact=Contact(name=name, email=email, phone= phone)
        contact.save()
        print("The data has been written to the db")
        
        
    #return HttpResponse("This is my contact page(/contact)")
    return render(request, 'contact.html')
