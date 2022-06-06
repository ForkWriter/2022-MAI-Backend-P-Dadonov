from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

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
            <li>/Get</li>
            <li>/GetAll</li>
            <li>/Post</li>
        </ul>
    </html>
    """
    return HttpResponse(http)


def get_tea(request):
    if request.method == "GET":
        tea_id = request.GET.get("tea_id", 1)
        name = request.GET.get("name", "Mate")
        color = request.GET.get("color", "Green")
        country = request.GET.get("country", "Argentina, Paraguay, Uruguay, Brazil")
        return JsonResponse({"tea_id": tea_id, "name": name, "color": color, "country": country})
    else:
        return HttpResponseBadRequest("<h2>Error!</h2>")

def getall_tea(request):
    if request.method == "GET":
        tea_id_1 = request.GET.get("tea_id", 1)
        name_1 = request.GET.get("name", "Mate")
        color_1 = request.GET.get("color", "Green")
        country_1 = request.GET.get("country", "Argentina, Paraguay, Uruguay, Brazil")
        tea_id_2 = request.GET.get("tea_id", 2)
        name_2 = request.GET.get("name", "Oolong")
        color_2 = request.GET.get("color", "Yellow")
        country_2 = request.GET.get("country", "China")
        return JsonResponse({"All teas" : [{"tea_id": tea_id_1, "name": name_1, "color": color_1, "country": country_1},{"tea_id": tea_id_2, "name": name_2, "color": color_2, "country": country_2}]})
    else:
        return HttpResponseBadRequest("<h2>Error!</h2>")

@csrf_exempt
def post_tea(request):
    if request.method == "POST":
        tea_id = request.GET.get("tea_id", 3)
        name = request.GET.get("name", "Karkade")
        color = request.GET.get("color", "Red")
        country = request.GET.get("country", "Egypt")
        return JsonResponse({"tea_id": tea_id, "name": name, "color": color, "country": country})
    else:
        return HttpResponseBadRequest("<h2>Error!</h2>")

