from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def display(request):
  return render(request,'index.html')

def docancel(request):
  return render(request,'cancel.html')

def receive(request):
 if request.method=='POST':
    name=request.POST.get('hname')
    email=request.POST.get('hmail')
    msg=request.POST.get('msg')
    z=Help(myName=name,myEmail=email,msg=msg)
    z.save()
    return HttpResponse("<center><h1>Thanks!!!Your Query Will Be Answered Soon.....</h1></center>")
 else:
    return HttpResponse("Invalid Request")

def doLogin(request):
 if request.method=='POST':
    email=request.POST.get('myemail')
    password=request.POST.get('mypwd')
    z=Login(email=email,password=password)
    z.save()
    return HttpResponse("<center><h1>You Are Logged In....,...</h1></center>")
 else:
    return HttpResponse("Invalid Request")

def feedback(request):
 if request.method=='POST':
    email=request.POST.get('e')
    feedback=request.POST.get('f')
    z=Feedback(email=email,feedback=feedback)
    z.save()
    return HttpResponse("<center><h1>Thanks For Sharing Your Feedback...</h1></center>")
 else:
    return HttpResponse("Invalid Request")

#Displaying Data Of Tables
def showfeedback(request):
   f=Feedback.objects.all()
   return render(request,'app1/results.html',{'f':f})

def showlogin(request):
   l=Login.objects.all()
   return render(request,'app1/results.html',{'l':l})


def showhelp(request):
   h=Help.objects.all()
   return render(request,'app1/results.html',{'h':h})

def showorder(request):
   ord=Order.objects.all()
   return render(request,'app1/results.html',{'ord':ord})

def showproduct(request):
   prd=Product.objects.all()
   return render(request,'app1/results.html',{'prd':prd})


def mypaneer(request):
  return render(request,'paneer.html')

def mydosa(request):
  return render(request,'dosa.html')

def myidli(request):
  return render(request,'idli.html')

def mymanchurian(request):
  return render(request,'manchurian.html')

def paneer(request):
 if request.method=="POST":
   orderid=request.POST.get('oid')
   productid=request.POST.get('pid')
   customer=request.POST.get('cus')
   z=Order(orderid=orderid,productId=productid,customer=customer)
   z.save()
   return HttpResponse("<h1>Order Successfully Received...</h1>")
 else:
   return HttpResponse("<h1>Invalid Request...</h1>")   
   



   


















