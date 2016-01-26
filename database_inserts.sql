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
            ("Calvino Italo", "Jesli zimowa noca podrozny", "29.99", "images/covers/podrozny.jpg", "Powiesc"),
            ("Bernadette McDonald", "Alpjscy wojownicy", "45.99", "images/covers/alpejscy.jpg", "Reportaz"),
            ("Michael Dobbs", "House of Cards. Ostatnie rozdanie", "39.90", "images/covers/house.jpg", "Literatura sensacyjna"),
            ("Arnold Lobel", "Zabek i Ropuch. Przez caly rok", "28.99", "images/covers/zabek.jpg", "Ksiazki dla dzieci"),
            ("Paula Hawkins", "Dziewczyna z pociagu", "32.90", "images/covers/dziewczyna.jpg", "Literatura sensacyjna"),
            ("Rick Riordan", "Greccy Herosi wedlug Percy'ego Jacksona", "49.90", "images/covers/percy.jpg", "Podroze, Ksiazki dla mlodziezy"),
            ("Remigiusz Grzela, Barbara Krafftowna", "Krafftowna w krainie czarow", "39.90", "images/covers/krafft.jpg", "Biografia"),
            ("Krystyna Mirek", "Jabloniowy Sad. Rodzinne sekrety", "36.90", "images/covers/jablon.jpg", "Literatura piekna"),
            ("Lee Child", "Zmus mnie", "32,90", "images/covers/zmus.jpg", "Literatura sensacyjna"),
            ("David Mitchell", "Czasomierze", "55.90", "images/covers/czas.jpg", "Fantastyka"),
            ("Joanna Opiat-Bojarska", "Gdzie jestes, Leno?", "24.90", "images/covers/gdzie.jpg", "Kryminal"),
            ("Alice Milani", "Wislawa Szymborska. Zycie w obrazkach", "49.90", "images/covers/wislawa.jpg", "Literatura piekna"),
            ("Stephen Baxter, Terry Pratchett", "Dluga utopia", "32.49", "images/covers/dluga.jpg", "Fantastyka"),
            ("Mo O'Hara", "Moja zlota rybka zombie", "24.90", "images/covers/moja.jpg", "Ksiazki dla dzieci"),
            ("Jerzy Pilch", "Zawsze nie ma nigdy", "39.90", "images/covers/zawsze.jpg", "Publicystyka"),
            ("John Steibeck", "Zagubiony autobus", "31.99", "images/covers/zagubiony.jpg", "Literatura piekna obca"),
            ("Jolanta Guse", "Opowiem o niej", "29.99", "images/covers/opowiem.jpg", "Literatura piekna polska"),
            ("Leonard Susskind, Art Friedman", "Mechanika kwantowa", "39.90", "images/covers/mechanika.jpg", "Literatura popularnonaukowa"),
            ("Charles M. Schulz", "Fistaszki. Opowiesc filmowa", "19.90", "images/covers/fistaszki.jpg", "Ksiazki dla dzieci"),
            ("Paul Colize", "Dluga chwila ciszy", "38.99", "images/covers/ciszy.jpg", "Kryminal"),
            ("Andrzej Batko", "Haker umyslow", "32.90", "images/covers/haker.jpg", "Psychologia"),
            ("Terry Goodkind", "Serce Wojny", "34.90", "images/covers/serce.jpg", "Fantastyka");

INSERT INTO Tagi(idTag,nazwaTagu) VALUES
            (1, "heheszki"),
            (2, "biografia"),
            (3, "naukowe"),
            (4, "bestseller"),
            (5, "zimne");
SET FOREIGN_KEY_CHECKS=0;
INSERT INTO listaTagu(idKsiazka,idTag) VALUES
            (1, 1),
            (1, 2),
            (1, 4),
            (2, 3),
            (3, 4),
            (4, 5),
            (6, 4),
            (7, 5);
SET FOREIGN_KEY_CHECKS=1;
