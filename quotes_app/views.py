# quote_api/quotes_app/views.py
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Quote, Source, Author, Category # Zorg dat alles geïmporteerd is
from .serializers import QuoteSerializer, SourceSerializer # Zorg dat beide serializers geïmporteerd zijn
import random
import requests
from django.shortcuts import get_object_or_404
from .pagination import StandardResultsSetPagination # Importeer
from .filters import QuoteFilter


# View voor de volledige lijst + zoeken + filteren
#class QuoteListView(generics.ListAPIView):
 #   queryset = Quote.objects.all().order_by('id')
 #   serializer_class = QuoteSerializer
    # DE FIX: Voeg de filter backend en de juiste veld-configuratie toe
 #   filter_backends = [DjangoFilterBackend, filters.SearchFilter]
 #   filterset_fields = ['source'] # Dit filtert op de ID van de source
 #   search_fields = ['text', 'author__name']
    
class QuoteListView(generics.ListAPIView):
    queryset = Quote.objects.all().order_by('id')
    serializer_class = QuoteSerializer
    pagination_class = StandardResultsSetPagination # <-- VOEG DEZE REGEL TOE
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['source']
    search_fields = ['text', 'author__name']    

# View voor de lijst met alle bronnen/categorieën
class SourceListView(generics.ListAPIView):
    queryset = Source.objects.all().order_by('name')
    serializer_class = SourceSerializer

# View voor een willekeurige quote
class RandomQuoteView(generics.RetrieveAPIView):
    serializer_class = QuoteSerializer

    def get_object(self):
        all_quote_ids = Quote.objects.values_list('id', flat=True)
        if not all_quote_ids:
            return None
        random_id = random.choice(list(all_quote_ids))
        return get_object_or_404(Quote, pk=random_id)
        
class QuoteDetailView(generics.RetrieveAPIView):
    """
    Deze view toont één specifieke quote op basis van zijn ID.
    """
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

# --- VIEW VOOR INZENDINGEN ---
class QuoteSubmitView(generics.CreateAPIView):
    serializer_class = QuoteSerializer

    def create(self, request, *args, **kwargs):
        # 1. Valideer de reCAPTCHA token
        recaptcha_response = request.data.get('g-recaptcha-response')
        if not recaptcha_response:
            return Response({"error": "reCAPTCHA token is missing."}, status=status.HTTP_400_BAD_REQUEST)

        data = {
            'secret': 'UW_SECRET_KEY_HIER', # Gebruik dezelfde Secret Key als in settings.py
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()

        if not result.get('success'):
            return Response({"error": "Invalid reCAPTCHA. Please try again."}, status=status.HTTP_400_BAD_REQUEST)

        # 2. Als reCAPTCHA geldig is, ga verder met het opslaan van de quote
        return super().create(request, *args, **kwargs)