from django.shortcuts import render, HttpResponse
import random
# request - запрос 
# respone - ответ 

def test(request):
    x = random.randint(1, 1000)
    a = random.randint(1, 1000)
    s = x - a
    return HttpResponse(f"имран {x} - {s} = {s}")

def test2(request):
    return HttpResponse("привет 33324231")
