from rest_framework import serializers

from api_v1.models import Quote


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ('id', 'text', 'author_name', 'author_email', 'rating', 'status', 'created_at', 'updated_at')
        read_only_fields = ['rating', 'status']


class UpdateQuoteSerializer(QuoteSerializer):
    class Meta(QuoteSerializer.Meta):
        parent_array = QuoteSerializer.Meta.read_only_fields
        parent_array.pop(-1)

        read_only_fields = parent_array + ['author_name', 'author_email']
