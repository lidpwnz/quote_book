from api_v1.models import Quote
from api_v1.serializers import QuoteSerializer


class QuotesAttrsMixin:
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    request = None
    all_queryset_perms = {'PUT': 'api_v1.change_quote',
                          'PATCH': 'api_v1.change_quote',
                          'DELETE': 'api_v1.delete_quote',
                          'GET': 'api_v1.view_not_moderated_quotes'}

    def get_queryset(self):
        if self.request.user.has_perm(self.all_queryset_perms.get(self.request.method)) or self.request.method == 'POST':
            return self.queryset
        return self.queryset.filter(status='Moderated')
