from django.contrib import admin


# Admin - tutaj rejestrujemy modele, by pojawily sie w aplikacji admina.

from .models import Book


class BookAdmin(admin.ModelAdmin): # Tworzymy appke dla admina.
    class Meta:
        model = Book



admin.site.register(Book, BookAdmin) # Rejestrujemy model w panelu admina.