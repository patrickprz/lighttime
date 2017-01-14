from django.shortcuts import render
from django.utils import timezone
from .models import Calc
from django.shortcuts import render, get_object_or_404
from .forms import CalcForm
from django.shortcuts import redirect

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


def calcule(distance,isMeters, language="enus"):
    measure = "m"
    distanceShow = int(distance)
    hoursShow = "Hours"
    minutesShow = "minutes"
    secondsShow = "seconds"

    if(isMeters == False):
        measure = "km" #Converte os valores para km
        distance = distance * 1000 #Converte a distancia em km para metros

    resultString = ("At a distance of " + str(distanceShow) + measure + " the light comes on approximately: ")
    if(language == "ptbr"):
        hoursShow = "Horas"
        minutesShow = "minutos"
        secondsShow = "segundos"
        resultString = ("Em uma distancia de " + str(distanceShow) + measure + " a luz chega em aproximadamente: ")

    lightSpeed = 299792458.0 #em m/s
    result = distance/lightSpeed
    if(result/60 >= 60):
        minutes = result/60
        hour = minutes/60
        hourBase60 = minutes//60
        secondsBase60 = result%60
        minutesBase60 = (minutes - (hourBase60 * 60))
        return(resultString + str(int(hourBase60)) + " " + hoursShow +" " + str(int(minutesBase60))+ " " + minutesShow + " " + str(int(secondsBase60)) + " " + secondsShow)
    elif(result < 1):
        return(resultString + str(result) + " seconds")
    else:
        minutesBase60 = result//60
        secondsBase60 = result%60
        if(minutesBase60 >= 1):
            return (resultString + str(int(minutesBase60)) + " " + minutesShow + " " + str(int(secondsBase60)) + " " + secondsShow)
        else:
            return (resultString + str(round(secondsBase60,2)) + " " + secondsShow)
