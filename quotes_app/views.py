# quote_api/quotes_app/views.py

from rest_framework import generics, filters # Voeg 'filters' toe
from .models import Quote
from .serializers import QuoteSerializer
import random
from django.shortcuts import get_object_or_404

class QuoteListView(generics.ListAPIView):
    """
    This view displays a list of all quotes.
    It supports searching on the 'text' and 'author' fields.
    """
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    
    # --- DIT BLOK TOEVOEGEN VOOR DE ZOEKFUNCTIE ---
    filter_backends = [filters.SearchFilter]
    search_fields = ['text', 'author__name']
    # --- EINDE TOEVOEGING ---


class RandomQuoteView(generics.RetrieveAPIView):
    """
    This view returns a single, randomly selected quote.
    """
    serializer_class = QuoteSerializer

    def get_object(self):
        """
        Return a single random Quote object.
        """
        all_quote_ids = Quote.objects.values_list('id', flat=True)
        if not all_quote_ids:
            return None
        
        random_id = random.choice(list(all_quote_ids))
        return get_object_or_404(Quote, pk=random_id)