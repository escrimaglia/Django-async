# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import asyncio

# Sync view
def sync_view(request):
    return JsonResponse({'message': 'Hola, proceso sincronico'})

async def async_view(request):
    await asyncio.sleep(10)
    return JsonResponse({'message': 'Hola, proceso asincronico'})
