from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from tea_app.models import Colors, Teas
from tea_app.serializers  import ColorSerializer, TeaSerializer
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework import status, viewsets
from rest_framework.response import Response

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
            <li>/restapi/tea/</li>
            <li>/restapi/color/</li>
        </ul>
    </html>
    """
    return HttpResponse(http)

class ColorViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Colors.objects.all()
        serializer = ColorSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ColorSerializer(data=request.data)
        
        if serializer.is_valid():
            color = Colors()
            color.name = serializer.validated_data["name"]
            color.save()
            return Response({"status": "OK"})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        queryset = Colors.objects.all()
        
        color = None
        try:
            color = get_object_or_404(queryset, pk=pk)
        except:
            pass
        serializer = ColorSerializer(color)
        return Response(serializer.data)

class TeaViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Teas.objects.all()
        serializer = TeaSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = TeaSerializer(data=request.data)
        
        if serializer.is_valid():
            tea = Teas()
            tea.name = serializer.validated_data["name"]
            tea.color = serializer.validated_data["color"]
            tea.countries = serializer.validated_data["countries"]
            tea.description = serializer.validated_data["description"]
            tea.save()
            return Response({"status": "OK"})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        queryset = Teas.objects.all()
        
        tea = None
        try:
            tea = get_object_or_404(queryset, pk=pk)
        except:
            pass
        serializer = TeaSerializer(tea)
        return Response(serializer.data)

