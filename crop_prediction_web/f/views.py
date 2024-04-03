from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here. user-anusha password-123
def HomePage(request):
    return render(request,'home1.html')
def SignUpPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pasw1=request.POST.get('password1')
        pasw2=request.POST.get('password2')
        if pasw1!=pasw2:
            return HttpResponse("Your password and conform password are not same")
        else:
            my_user=User.objects.create_user(uname,email,pasw1)
            my_user.save()
            return redirect('login')
        # print(uname,email,pasw1,pasw2)
    return render(request,'signup.html')
def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
           return HttpResponse("User name or password incorrect")
    return render(request,'login.html')
def LogOutPage(request):
    logout(request)
    return redirect('login')
def getPredictions(N,P,K,temperature,humidity,ph,rainfall):
    import pickle
    model=pickle.load(open(rb"D:\ml dl\crop_detection\crop_prediction_web\crop_prediction_web\crop_model.sav","rb"))
    prediction=model.predict([[N,P,K,temperature,humidity,ph,rainfall]])
    return (prediction)
def index(request):
    return render(request,'index.html')

def result(request):
    N=int(request.GET['N'])
    P=int(request.GET['P'])
    K=int(request.GET['K'])
    temperature=float(request.GET['temperature'])
    humidity=float(request.GET['humidity'])
    ph=float(request.GET['ph'])
    rainfall=float(request.GET['rainfall'])


    result=getPredictions(N,P,K,temperature,humidity,ph,rainfall)
    return render(request,'result.html',{'result':result})
