# quote_api/quotes_app/urls.py
    
from django.urls import path
from .views import QuoteListView, RandomQuoteView # Voeg RandomQuoteView toe

urlpatterns = [
    # De bestaande URL voor de lijst met alle quotes
    path('', QuoteListView.as_view(), name='quote-list'),
    
    # De nieuwe URL voor een willekeurige quote
    path('random/', RandomQuoteView.as_view(), name='quote-random'),
]