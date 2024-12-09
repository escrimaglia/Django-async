# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import asyncio
from asgiref.sync import sync_to_async

# Sync view
def sync_view(request):
    return JsonResponse({'message': 'Hola, proceso sincronico'})

# Async view
async def async_view(request):
    await asyncio.sleep(4)
    return JsonResponse({'message': 'Hola, proceso asincronico'})

# Sync to async view
async def sync_to_async_view(request):
    response = await sync_to_async(espera)()
    return JsonResponse(response)

# funcion Sync para convertir a Async
def espera():
    import time
    time.sleep(4)
    return {'message': 'Hola, proceso sync to async'}