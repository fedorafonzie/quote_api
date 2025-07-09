from rest_framework import serializers
from .models import Quote, Author, Source, Category

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ['id', 'name', 'author_name']


class QuoteSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    source = serializers.StringRelatedField(read_only=True)
    categories = serializers.StringRelatedField(many=True, read_only=True)

    author_name = serializers.CharField(write_only=True, required=False, allow_blank=True, label="Auteur naam")
    source_id = serializers.PrimaryKeyRelatedField(
        queryset=Source.objects.all(), source='source', write_only=True, required=False, allow_null=True
    )
    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='categories', many=True, write_only=True
    )

    class Meta:
        model = Quote
        fields = [
            'id', 'text', 
            'author', 'source', 'categories',
            'author_name', 'source_id', 'category_ids'
        ]
        read_only_fields = ['author', 'source', 'categories']

    def create(self, validated_data):
        # Haal de categorieën en de auteursnaam uit de data
        categories = validated_data.pop('categories')
        author_name = validated_data.pop('author_name', None)
        
        # Maak de Auteur aan of haal deze op
        author_obj = None
        if author_name:
            author_obj, _ = Author.objects.get_or_create(name__iexact=author_name, defaults={'name': author_name})

        # Sla de quote op met de overgebleven data, nu inclusief de auteur
        quote = Quote.objects.create(author=author_obj, **validated_data)
        
        # Koppel de categorieën op de juiste manier
        if categories:
            quote.categories.set(categories)
        
        return quote