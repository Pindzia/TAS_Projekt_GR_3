from django import forms
from .models import Book

# Forms - czyli dane, ktore mozemy wprowadzac z poziomu uzytkownika, na stronie.


class BookForm(forms.ModelForm):
    class Meta:
        model = Book # Wskazanie, ktorego modelu uzywamy.