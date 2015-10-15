from django.db import models

# Modele - w skrocie definicja naszej bazy danych.


class Book(models.Model):
    title = models.CharField(max_length = 50)  # Tytul ksiazki.
    author = models.CharField(max_length = 50)  # Autor ksiazki.

    # I co tam jeszcze chcemy. Pamietajmy, ze po kazdej modyfikacji tabeli, ktore sa juz w bazie musimy uzyc Southa albo usunac baze danych.

    def __unicode__(self):
        return "%s, %s" % (self.title, self.author) # Nazwa poszczegolnych pozycji.

