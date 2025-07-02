# quote_api/quotes_app/admin.py

from django.contrib import admin
from .models import Quote, Author, Category, Source

# We maken een custom admin class voor het Quote model
class QuoteAdmin(admin.ModelAdmin):
    # Hier definiëren we op welke velden de zoekbalk moet zoeken.
    # We kunnen zoeken in de tekst, de naam van de auteur, en de naam van de bron.
    search_fields = ['text', 'author__name', 'source__name']

    # Bonus: toon deze velden in de lijstweergave voor een beter overzicht.
    list_display = ('text', 'author', 'source')

    # Maak de lijst filterbaar op categorie en bron
    list_filter = ('categories', 'source')

# Registreer de andere modellen zoals voorheen
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Source)

# Koppel nu het Quote model aan onze nieuwe QuoteAdmin class
admin.site.register(Quote, QuoteAdmin)