from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,JsonResponse
# Create your views here.

def pagina(request):
    return render(request, 'HomePage.html')