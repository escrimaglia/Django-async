from django.urls import path
from . import views

urlpatterns = [
    path("sync/", views.sync_view, name="sync_view"),
    path("async/", views.async_view, name="async_view"),
    path("sync-to-async/", views.sync_to_async_view, name="sync_to_async_view"),
]
