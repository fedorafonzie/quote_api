# quote_api/quotes_app/filters.py
from django_filters import rest_framework as filters
from .models import Quote

class QuoteFilter(filters.FilterSet):
    class Meta:
        model = Quote
        fields = ['source'] # Filter op source ID