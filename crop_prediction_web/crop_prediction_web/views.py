from django.shortcuts import render

def home(request):
    return render(request,'home1.html')

def getPredictions(N,P,K,temperature,humidity,ph,rainfall):
    import pickle
    model=pickle.load(open(rb"D:\ml dl\crop_detection\crop_prediction_web\crop_prediction_web\crop_model.sav","rb"))
    prediction=model.predict([[N,P,K,temperature,humidity,ph,rainfall]])
    return (prediction)
# def index(request):
#     return render(request,'index.html')

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
