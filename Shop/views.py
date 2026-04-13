from django.shortcuts import render, HttpResponse,redirect
from .models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(redirect_field_name ='/login')
def index(request):
    if not request.user.is_authenticated:
        return request(request,'login.html')
    return render(request,'index.html')

def products(request):
    return render(request,'products.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        emailid = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name, emailid=emailid, phone=phone, message=message)
        contact.save()

        return redirect('/contact')
    data=Contact.objects.filter(message="erfv").all()
    return render(request,'contact.html',{'data':data})

    
def catalog(request):
    return render(request,'catalog.html')

def loginView(request):
    if request.method == "POST":
        username = request.POST.get('userName')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            #A backend authenticated the credentials
            login(request,user)
            return redirect('/home')
    
        else:
                #No backend authenticated the credentials
            return render(request,"login.html",{"error":"Invalid username or password"})    
    return render(request,'login.html')

def signupView(request):
    if request.method == "POST":
        FirstName = request.POST.get('FirstName')
        LastName = request.POST.get('LastName')
        username = request.POST.get('userName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        if password == confirmPassword:
            user=User.objects.create_user(username,email,password)
            user.first_name=FirstName
            user.last_name=LastName
            user.save()
            return redirect('/login')
    return render(request,'signup.html')

def logoutView(request):
    logout(request)
    return redirect('/login')