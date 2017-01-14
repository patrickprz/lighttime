from django.shortcuts import render
from django.utils import timezone
from .models import Calc
from django.shortcuts import render, get_object_or_404
from .forms import CalcForm
from django.shortcuts import redirect

def calcule(distance,isMeters, language="en"):
    #print isMeters
    measure = "m"
    distanceShow = int(distance)

    if(isMeters == False):
        #print "Valores convertidos de km para metros"
        measure = "km"
        distance = distance*1000 #converte a distancia em km para metros

    resultString = ("At a distance of " + str(distanceShow) + measure + " the light comes on approximately: ")
    if(language == "ptbr"):
        resultString = ("Em uma distancia de " + str(distanceShow) + measure + " a luz chega em aproximadamente: ")



    lightSpeed = 299792458.0 #em m/s
    result = distance/lightSpeed
    if(result/60 >= 60):
        minutes = result/60
        hour = minutes/60
        hourBase60 = minutes//60
        secondsBase60 = result%60
        minutesBase60 = (minutes - (hourBase60 * 60))
        return(resultString + str(int(hourBase60)) + " Hours " + str(int(minutesBase60))+ " minutes and " + str(int(secondsBase60)) + " seconds")
    elif(result < 1):
        return(resultString + str(result) + " seconds")
    else:
        minutesBase60 = result//60
        secondsBase60 = result%60
        if(minutesBase60 >= 1):
            return (resultString + str(int(minutesBase60)) + " minutes and " + str(int(secondsBase60)) + " seconds")
        else:
            return (resultString + str(round(secondsBase60,2)) + " seconds")

def indexptbr(request, result=""):
    if request.method == "POST":
        form = CalcForm(request.POST)
        if form.is_valid():
          data = form.cleaned_data
          distance = data['distance']
          isMeters = data['isMeters']
          result = calcule(distance, isMeters, "ptbr")
        return render(request, 'timeCalculator/indexptbr.html', {'result' : result})
    else:
        form = CalcForm()
    return render(request, 'timeCalculator/indexptbr.html', {'result' : result})


def index(request, result=""):
    if request.method == "POST":
        form = CalcForm(request.POST)
        if form.is_valid():
          data = form.cleaned_data
          distance = data['distance']
          isMeters = data['isMeters']
          result = calcule(distance, isMeters)
        return render(request, 'timeCalculator/index.html', {'result' : result})
    else:
        form = CalcForm()
    return render(request, 'timeCalculator/index.html', {'result' : result})
