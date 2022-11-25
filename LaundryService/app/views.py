from django.shortcuts import render, redirect
from .form import *
from .models import *



def home(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        try:
            user = userDataModel.objects.get(username=username, password=password)
            return redirect('home')
        except:
            loginform = userLoginForm()
            error = 'Invalid Credentials'
            return render(request, 'login.html', {'error': error, 'form': loginform})

            
    loginform = userLoginForm()
    return render(request, 'login.html', {'form': loginform})
    
def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']
        data = userDataModel(username=username, name=name, email=email, password=password, phone=phone)
        data.save()
        return redirect('login')
      

    signupform = userSignupForm()
    return render(request,'signup.html', {'form': signupform})