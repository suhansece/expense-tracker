from django.shortcuts import redirect,render
from django.shortcuts import render
from django.contrib.auth.models import User

from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate ,login ,logout




def home(request):
            
   

        
    
    if request.method=="POST":
        if request.POST.get('cramount'):
            cramount=request.POST['cramount']
            crdiscription=request.POST['crdiscription']
            crdate=request.POST['crdate']
            
            savecr=Credit()
            savecr.cramounts=cramount
            savecr.crdescriptions=crdiscription
            savecr.crdates=crdate
            savecr.deamounts=0

            savecr.save()
            messages.success(request," Added success fully")
            
        if request.POST.get('deamount'):
            cramount=request.POST['deamount']
            crdiscription=request.POST['dediscription']
            crdate=request.POST['dedate']
            
            savecr=Credit()
            savecr.deamounts=cramount
            savecr.crdescriptions=crdiscription
            savecr.crdates=crdate
            savecr.cramounts=0
            

            savecr.save()
            messages.success(request," Added success fully")
           
            
    if request.user.is_authenticated:
        items = Credit.objects.all()
        context= {'items': items}
        return render(request,"expence/index.html",context)
    
        
    return render(request,"expence/index.html")

def signup(request):
    if(request.method=="POST"):
        
        username =request.POST.get('username')
        fname = request.POST['firstname']
        lname =request.POST['lastname']
        email =request.POST['emailid']
        password =request.POST['password']
        

        myuser= User.objects.create_user(username,email,password)
        myuser.first_name=fname
        myuser.last_name=lname

        myuser.save()
        messages.success(request,"Your has been created success fully")

        return redirect('signin')

    return render(request,"expence/signup.html")

def signin(request):
    if request.method=="POST":
        username1 =request.POST.get('username')
        pass1 =request.POST['password']
       
        user=authenticate(username=username1,password=pass1)

        if user is not None:
            login(request,user)
            fname=user.first_name
            
            return redirect('home')

        else :
            messages.error(request,"Bad Credentials!")
            

        return redirect('home')


    return render(request,"expence/signin.html")

def signout(request):
     logout(request)
     return redirect(home)

def deleteStatement(request,pk):
    products=Credit.objects.get(id=pk)
    products.delete()
    return redirect('home')