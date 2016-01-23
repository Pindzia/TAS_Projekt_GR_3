    //koszyk

    function usun(nr)
    {

      //usuwanie ksiazki (z bazy też) gdy zmniejszymy ilość do 0
   
      // tworzenie form'a
      var element = document.createElement('form');
      element.id = 'formularz' + String(nr);
      element.method = 'post';
      element.action = 'delete/' + String(nr) + '/';

      var idLi = 'rzad' + String(nr);
      var ksiazka = document.getElementById(idLi);

      ksiazka.appendChild(element);

      //tworzenie inputa z Pythona
      var inputPython = document.createElement('input');
      inputPython.type = 'hidden';
      inputPython.name = 'csrfmiddlewaretoken';

      var stringPython = "{% csrf_token %}";
      var valPos = stringPython.search("value=");
      var valPosEnd = stringPython.lastIndexOf("'");
      var value = [];
      var j = 0;

      for(var i=valPos+7; i<valPosEnd; i++)
      { 
        value[j++] = stringPython[i];
      }

      //z tablicy char do string
      var value1 = value.join('');

      inputPython.value = value1;

      document.getElementById(element.id).appendChild(inputPython);
          
      //tworzenie button'a i usuwanie
      var button = document.createElement('button');
      button.className = "btn";
      button.id = "button" + String(nr);
      button.type = "submit";
      button.title = "usuń";
      button.style.top = "75px";
      button.style.left = "675px";
      button.style.opacity = 0;

      document.getElementById(element.id).appendChild(button);
    }

    function usuwanie(nr)
    {
      var id = 'ilosc' + String(nr);
      
      if(document.getElementById(id).value == 1)
        usun(nr);
      
      if(document.getElementById(id).value > 1)
      {

        var idRzad = 'rzad' + String(nr);
        var idForm = 'formularz' + String(nr);

        var rzad = document.getElementById(idRzad);
        var form = document.getElementById(idForm);

        if(form)
          rzad.removeChild(form);
      }
    }

    function increment(nr)
    {
        var szukaneId = 'ilosc' + String(nr);
        var zwieksz = document.getElementById(szukaneId).value;
        zwieksz++;

        document.getElementById(szukaneId).value = zwieksz;

        usuwanie(nr);
        //do zrobienia
        //lacznaKwota(zwieksz);
    }

    function decrement(nr)
    {
        var szukaneId = 'ilosc' + String(nr);
        var zmniejsz = document.getElementById(szukaneId).value;

        if(zmniejsz > 1)
        {
          zmniejsz--;
          document.getElementById(szukaneId).value = zmniejsz;
        }
        if(zmniejsz == 1) 
        {
          usuwanie(nr);
        }
    }


    function dodajKwote(kasaZaKsiazke)
    {
      var zmienna = document.getElementById('kwota');

      kaska = zmienna.innerHTML;

      kaska = parseFloat(kaska) + parseFloat(kasaZaKsiazke);

      kaska = kaska + ' zł';

      document.getElementById('kwota').innerHTML = kaska;
    }

    //do zrobienia przemnażanie kwoty za dana książkę przez jej ilość
    function lacznaKwota(liczba)
    {
      var suma = 0.00;
      var kwota = String(suma) + ' zł';

      var x = document.getElementById('kwota');

      x.createTextNode(kwota);
    }