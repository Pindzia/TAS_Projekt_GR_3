-- Przykladowe wpisy w bazie danych

DELETE FROM `tas`.`listaKoszyka` ;
DELETE FROM `tas`.`Koszyk` ;
DELETE FROM `tas`.`Ksiazka` ;

INSERT INTO Ksiazka(autor, tytul, cena, dict_img, kategoria) VALUES
            ("Dostojewski Fiodor", "Idiota", "38.98", "images/covers/idiota.jpg", "Rosyjska literatura"),
            ("Erich Gamma", "Wzorce projektowe", "59.99", "images/covers/wzorce.jpg", "Programowanie"),
            ("Douglas Adams", "W zasadzie niegroznia", "29.99", "images/covers/niegrozna.jpg", "Fantastyka"),
            ("Dukaj Jacek", "Lod", "79.99", "images/covers/lod.jpg", "Fantastyka"),
            ("Nietzsche Friedrich", "Wola mocy", "39.00", "images/covers/nic.jpg", "Filozofia"),
            ("Witkiewicz Stanislaw", "Nienasycenie", "29.99", "images/covers/nienasycenie.jpg", "Powiesc"),
            ("Calvino Italo", "Jesli zimowa noca podrozny", "29.99", "images/covers/podrozny.jpg", "Powiesc");
