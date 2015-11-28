-- Przykladowe wpisy w bazie danych

DELETE FROM `tas`.`listaKoszyka` ;
DELETE FROM `tas`.`Koszyk` ;
DELETE FROM `tas`.`Ksiazka` ;

INSERT INTO Ksiazka(autor, tytul, cena, dict_img, kategoria) VALUES
            ("Dostojewski Fiodor", "Idiota", "38,99", "", "Rosyjska literatura"),
            ("Erich Gamma", "Wzorce projektowe", "59,99", "", "Programowanie"),
            ("W zasadzie niegroznia", "Douglas Adams", "29,99", "", "Fantastyka"),
            ("Lod", "Dukaj Jacek", "79,99", "", "Fantastyka"),
            ("Wola mocy", "Nietzsche Friedrich", "39,00", "", "Filozofia"),
            ("Nienasycenie", "Witkiewicz Stanislaw", "29,99", "", "Powiesc"),
            ("Jesli zimowa noca podrozny", "Calvino Italo", "29,99", "", "Powiesc");
