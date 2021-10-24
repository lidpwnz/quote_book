from rest_framework import routers
from .views import QuotesViewSet


quotes_router = routers.DefaultRouter()
quotes_router.register(r'quotes', QuotesViewSet)
