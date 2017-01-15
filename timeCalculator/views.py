# -*- coding: utf-8 -*-
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
          result = calculate(distance, isMeters)
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
          result = calculate(distance, isMeters, "ptbr")
        return render(request, 'timeCalculator/indexptbr.html', {'result' : result})
    else:
        form = CalcForm()
    return render(request, 'timeCalculator/indexptbr.html', {'result' : result})


def calculate(distance, isMeters, language="enus"):
    measureUnit = "m"
    distanceText = int(distance)
    hoursText = "Hours"
    minutesText = "minutes"
    secondsText = "seconds"

    if(isMeters == False):
        measureUnit = "km" #Converte os valores para km
        distance = distance * 1000 #Converte a distancia de km para metros

    resultString = ("At a distance of " + str(distanceText) + measureUnit + " the light comes on approximately: ")

    if(language == "ptbr"):
        hoursText = "Horas"
        minutesText = "minutos"
        secondsText = "segundos"
        resultString = ("Em uma distância de " + str(distanceText) + measureUnit + " a luz chega em aproximadamente: ")

    lightSpeed = 299792458.0 #em m/s
    result = distance/lightSpeed

    if(result/60 >= 60):
        minutes = result/60
        hours = minutes/60
        hoursBase60 = minutes//60
        secondsBase60 = result%60
        minutesBase60 = (minutes - (hoursBase60 * 60))
        return(resultString + str(int(hoursBase60)) + " " + hoursText +" " + str(int(minutesBase60))+ " " + minutesText + " " + str(int(secondsBase60)) + " " + secondsText)
    elif(result < 1):
        return(resultString + str(result) + " " + secondsText)
    else:
        minutesBase60 = result//60
        secondsBase60 = result%60
        if(minutesBase60 >= 1):
            return (resultString + str(int(minutesBase60)) + " " + minutesText + " " + str(int(secondsBase60)) + " " + secondsText)
        else:
            return (resultString + str(round(secondsBase60,2)) + " " + secondsText)
