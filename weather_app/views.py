from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
import json
import urllib.request

# Create your views here.

def index(request):
    
    if request.method == "POST":
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=5b1ae454cf0f59dbb96189f6243c81e8').read()
        json_data = json.loads(res)
        data = {
            "country": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp'])+'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }
        
    else: 
        city = ''
        data = {}
    return render(request, 'index.html', {"city":city, "data":data})    
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
        
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')    
        
    

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        
        if password == password:
            if User.objects.filter(email=email,).exists():
                messages.info(request, 'The email has already been used')
                return redirect('signup')
            else:
                user = User.objects.create_user(email=email, username=username, password=password)
                user.save();
                messages.info(request, 'You have successfuly created an account. Go back to login')
                return redirect('signup')
    else: 
        return render(request, 'signup.html')
            
                
                
                
                
            
        
            
        

