from django.shortcuts import render,HttpResponse,redirect
from .models import *
from random import randint
from django.core.mail import send_mail

# Create your views here.
def index(request):
    if request.session.has_key('uid'):
        
       return render(request,"index.html")
    else:
        return redirect("loginn")

def Contact(request):
    if request.session.has_key('uid'):
      return render(request,"contact.html")
    else:
        return redirect("loginn") 

def trainer(request):
    if request.session.has_key('uid'):
        return render(request,"trainer.html")
    else:
        return redirect("loginn")
def why(request):
    if request.session.has_key('uid'):
        return render(request,"why.html")
    else:
        return redirect("loginn")
def signn(request):
    if request.method=="POST":
        a=request.POST["nam"]
        b=request.POST["emails"]
        c=request.POST["pass"]
        if not a or not b or not c:
            return HttpResponse("fill all option")
        if Sign.objects.filter(email=b).exists():
          return HttpResponse("email id already exists")
        Sign.objects.create(name=a,email=b,password=c)
        otp=str(randint(2222,9999))
        print(otp)
        send_mail(
             "Welcome to my website",
             f"username {a} and your otp {otp}",
             "shivamsaini80885@gmail.com",
             {b},
             fail_silently=False,
            )
        request.session["otp"]=otp
        request.session["emails"]=b
        
        return redirect("otpp")
    else:
     return render(request,"sign.html")
 
def otp(request):
    if request.method=="POST":
        a=request.POST.get("otp")
        b=request.session.get("otp")
        if a==b:
            return redirect("loginn")
        else:
            return HttpResponse("otp is invalid")
    else:
        return render(request,"otp.html")    
            
     
def login(request):
    if request.method=="POST":
        a=request.POST["nam"]
        c=request.POST["pass"]
        x=Sign.objects.filter(name=a,password=c)
        if x:
            request.session['uid']=request.POST["nam"]
            
            return redirect("indexx")
        else:
            return HttpResponse("name and password does not match")
     
    else:
    
        return render(request,"login.html")
    
def Email(request):
    if request.method=="POST":
        a=request.POST["emails"]
       
        x=Sign.objects.filter(email=a)
        otp=str(randint(2222,9999))
        print(otp)
        send_mail(
             "Welcome to my website",
             f" your otp {otp}",
             "shivamsaini80885@gmail.com",
             {a},
             fail_silently=False,
            )
        request.session["otp"]=otp
        request.session["emails"]=a
        
    
        if x:
            
             return redirect("otpp1")
        else:
             return HttpResponse("email does not match")
     
    else:
    
        return render(request,"email.html")
    
def otp1(request):
    if request.method=="POST":
        a=request.POST.get("otp")
        b=request.session.get("otp")
        if a==b:
            return redirect('upd')
        else:
            return HttpResponse("otp is invalid")
        
    else:
        return render(request,"otp1.html")  

def Update(request):
    
    if request.method=="POST":
        a=request.POST["nam"]
        b=request.POST["pass"]
        Sign(password=b, name=a).save()
        return redirect("loginn")
    else:
        return render(request,"update.html")
    
def logout(request):
    del request.session['uid']
    
    return redirect("loginn")      