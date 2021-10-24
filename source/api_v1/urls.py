from django.urls import path, include
from .dependencies import quotes_router

urlpatterns = [
    path('', include(quotes_router.urls))
]
