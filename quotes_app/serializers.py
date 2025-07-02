# quote_api/quotes_app/serializers.py

from rest_framework import serializers
from .models import Quote, Author, Source, Category

class QuoteSerializer(serializers.ModelSerializer):
    """
    Deze serializer bepaalt hoe een Quote object wordt omgezet naar JSON.
    """
    # We willen de naam van de gerelateerde objecten tonen, niet hun ID.
    author = serializers.StringRelatedField()
    source = serializers.StringRelatedField()
    categories = serializers.StringRelatedField(many=True)

    class Meta:
        model = Quote
        # Definieer de velden die we willen zien in de API output.
        fields = ['id', 'text', 'author', 'source', 'categories']