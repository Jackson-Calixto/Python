from django.shortcuts import render

def home(request):
    return render(request, "myMsgApp/home.html", {'h1Text':'MessageBox', 'pText':'Welcome to the MessageBox App! Click the LOGIN button below to begin:'})
