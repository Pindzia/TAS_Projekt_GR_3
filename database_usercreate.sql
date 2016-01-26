INSERT INTO Uzytkownik (login, haslo, adres, nr_telefonu, email) VALUES ('TestKosz', 'qwert123', 'testowa 2', '700880774', 'test@lololo.pl');
INSERT INTO Koszyk (idUzytkownik, data_realizacji) VALUES (1, '9999-12-31 23:59:59');
INSERT INTO listaKoszyka (idKsiazka, idKoszyk, ilosc) VALUES (1, 1, 3);
INSERT INTO listaKoszyka (idKsiazka, idKoszyk, ilosc) VALUES (2, 1, 3);
INSERT INTO listaKoszyka (idKsiazka, idKoszyk, ilosc) VALUES (5, 1, 3);