# coding=utf-8
__author__ = 's396408'
import re
from Crypto.Hash import SHA256


def check(arg):
    p = re.compile(ur'^[\w@. ]{6,100}$')
    test_re = str(arg)

    if re.search(p, test_re) is not None:
        return True
    else:
        return False


def registry(login, password, password_2, adres, nr_Telefonu, e_Mail, rows):
    list = [login, password, password_2, adres, nr_Telefonu, e_Mail]
    list_num = ['Login', 'Haslo', 'Haslo ponowne', 'Adres', 'Numer Telefonu', 'E-mail']
    for e, nazwa in zip(list, list_num):
        if e is None:
            return "Pole %s jest puste" % nazwa

    if list[1] != list[2]:
        return "Hasla sie roznia"
    for l, nazwa in zip(list, list_num):
        if not check(l):
            return "Podane pole %s jest nieautoryzowane przez serwer" % nazwa


    if (mysql.get("SELECT Count(login) FROM Uzytkownik WHERE login = %s ;", rows) % list[0]) == 1:
        return "Uzytkownik o podanym Loginie jest juz zajety"
    
    cryptedpwd = SHA256.new()
    cryptedpwd.update(list[1])

    mystring = 'INSERT INTO Uzytkownik (login, haslo, adres, nr_telefonu, email) VALUES (\'' + list[0] + '\', \'' + cryptedpwd.hexdigest() + '\', \'' + \
               list[3] + '\', ' + str(list[4]) + '\', \'' + str(list[5]) + '\')'
    mysql.add(mystring)
    Sukces = 'Gratulujemy Pomyslnej Rejestracji.Prosimy o zalogowanie na stronie'
    return Sukces




def logowanie(self, login, haslo):
    if not check(login) and not check(haslo):
        return "Podany login lub hasło nie są autoryzowane przez serwer"
    cryptedcheckpwd = SHA256.new()
    cryptedcheckpwd.update(haslo)
    mystr = "SELECT login from Uzytkownik WHERE login = \'" + login + "\' AND \'" +  "haslo = \'"+ cryptedcheckpwd.hexdigest() + "\'"
    if (mysql.get(mystr)) is not None:
    #miejsce na ustawienie zmiennej sesyjnej
    

def main():
    #print registry('Pindzia', 'jawaleee', 'jawaleee', 'adresiwo', 7000000, 'olol@gmail.com', 20)
    print logowanie('Pindzia', 'jpjpjpna100')


if __name__ == "__main__":
    main()
