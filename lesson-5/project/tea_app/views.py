
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from tea_app import models

# Create your views here.
def index(request):
    http = \
    """
    <html lang="ru">
    <head>
        <title>Веб-сервер</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></meta>
        <h1>Hello from Django!</h1>
    </head>
    <body>
        <h4>Here you can learn more about tea.</h1>
        <ul>
            <li>/Get?tea_id=n</li>
            <li>/GetAll</li>
            <li>/Post</li>
        </ul>
    </html>
    """
    return HttpResponse(http)


def get_tea(request):
    if request.method == "GET":
        tea_id = request.GET.get("tea_id", -1)
        try:
            tea = models.Teas.objects.get(tea_id=tea_id)
            return JsonResponse({"tea_id": tea.tea_id, "name": tea.name, "description": tea.description, "countries": tea.countries, "color": tea.color.name})
        except models.Teas.DoesNotExist:
            return HttpResponse("<h2>Empty response</h2>")
    else:
        return HttpResponseBadRequest("<h2>Error!</h2>")

def getall_tea(request):
    if request.method == "GET":
        try:
            teas = models.Teas.objects.all()
            list=[]
            for tea in teas:
                list.append({"tea_id": tea.tea_id, "name": tea.name, "description": tea.description, "countries": tea.countries, "color": tea.color.name})
            
            return JsonResponse({"All teas" : [list]})
        except models.Teas.DoesNotExist:
            return HttpResponse("<h2>Empty response</h2>")

    else:
        return HttpResponseBadRequest("<h2>Error!</h2>")


@csrf_exempt
def post_tea(request):
    if request.method == "POST":
        name = request.GET.get("name", None)
        if not name:
            return HttpResponse("<h2>Empty name</h2>")
        description = request.GET.get("description", None)
        countries = request.GET.get("countries", None)
        color = request.GET.get("color", None)
        
        # Сохраняем в базу данных
        try:
            tea = models.Teas()
            tea.name = name
            tea.description = description
            tea.countries = countries
            tea.color = models.Colors.objects.get(name=str(color))
            tea.save()
            return HttpResponse("<h2>Successful</h2>")
        except:
            return HttpResponse("<h2>Unsuccessful</h2>")
    else:
        return HttpResponseBadRequest("<h2>Error!</h2>")