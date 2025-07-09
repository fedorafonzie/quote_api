# quote_api/quotes_app/urls.py
from django.urls import path
from .views import QuoteListView, RandomQuoteView, SourceListView, QuoteDetailView
from .views import QuoteListView, RandomQuoteView, SourceListView, QuoteSubmitView


urlpatterns = [
    path('quotes/', QuoteListView.as_view(), name='quote-list'),
    path('quotes/random/', RandomQuoteView.as_view(), name='quote-random'),
    path('quotes/<int:pk>/', QuoteDetailView.as_view(), name='quote-detail'),
    path('sources/', SourceListView.as_view(), name='source-list'),
    path('submit/', QuoteSubmitView.as_view(), name='quote-submit'),
]