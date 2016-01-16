INSERT INTO Uzytkownik (login, haslo, adres, nr_telefonu, email) VALUES ('TestKosz', 'qwert123', 'testowa 2', '700880774', 'test@lololo.pl');
INSERT INTO Koszyk (idUzytkownik, data_realizacji, zmienna_ses_kosz, status_zamowienia) VALUES (1, '9999-12-31 23:59:59', 0, 0);
INSERT INTO listaKoszyka (idKsiazka, idKoszyk, ilość) VALUES (1, 1, 3);
INSERT INTO listaKoszyka (idKsiazka, idKoszyk, ilość) VALUES (2, 1, 3);
INSERT INTO listaKoszyka (idKsiazka, idKoszyk, ilość) VALUES (5, 1, 3);