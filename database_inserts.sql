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

INSERT INTO Tagi(id_Tag,nazwaTagu) VALUES
            (1, "heheszki"),
            (2, "biografia"),
            (3, "naukowe"),
            (4, "bestseller"),
            (5, "zimne");
SET FOREIGN_KEY_CHECKS=0;
INSERT INTO listaTagu(idKsiazka,id_Tag) VALUES
            (1, 1),
            (1, 2),
            (1, 4),
            (2, 3),
            (3, 4),
            (4, 5),
            (6, 4),
            (7, 5);
SET FOREIGN_KEY_CHECKS=1;
