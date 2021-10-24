from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api_v1.models import Quote
from api_v1.serializers import UpdateQuoteSerializer
from .helpers import QuotesAttrsMixin


class Index(TemplateView):
    template_name = 'index.html'


class QuotesViewSet(QuotesAttrsMixin, ModelViewSet):
    def get_serializer_class(self):
        base_serializer = super().get_serializer_class()
        if self.request.method in ['PUT', 'PATCH']:
            return UpdateQuoteSerializer
        return base_serializer

    def post(self, request, *args, **kwargs):
        if self.request.data:
            return self.create(request, *args, **kwargs)
        return self.set_like(request, *args, **kwargs)

    def set_like(self, request, *args, **kwargs):
        quote: Quote = self.get_object()
        if not self.request.session.get('is_likes'):
            quote.increment_rating()
            self.request.session['is_likes'] = True
        else:
            quote.decrement_rating()
            self.request.session['is_likes'] = False

        serializer = self.serializer_class(quote)
        return Response(serializer.data, status=status.HTTP_200_OK)
