# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import GPIO
from django.shortcuts import render
from django.http import Http404

def detail_json(request, GPIO_Pin):
    try:
        gpio = GPIO.objects.get(GPIO_Pin=GPIO_Pin)
        data = {
            "GPIO_Pin": gpio.GPIO_Pin,
            "toggle_on": gpio.toggle_on,
            "pub_date": gpio.pub_date
        }
    except GPIO.DoesNotExist:
        raise Http404("GPIO setting does not exist for pin %s" %GPIO_Pin)
    return JsonResponse(data)
def index_json(request):
    gpio_pins = GPIO.objects.all()
    data = {}
    ind = 1
    for gpio in gpio_pins:
        data[ind] = {}
        data[ind]["GPIO_Pin"] = gpio.GPIO_Pin
        data[ind]["toggle_on"] = gpio.toggle_on
        ind+=1
    return JsonResponse(data)
def detail(request, GPIO_Pin):
    try:
        gpio = GPIO.objects.get(GPIO_Pin=GPIO_Pin)
    except GPIO.DoesNotExist:
        raise Http404("GPIO setting does not exist for pin %s" %GPIO_Pin)
    return render(request, 'gpios/detail.html', {'gpio': gpio})
def index(request):
    gpio_pins = GPIO.objects.all()
    context = {
        'gpio_pin_settings': gpio_pins,
    }
    return render(request, 'gpios/index.html', context)