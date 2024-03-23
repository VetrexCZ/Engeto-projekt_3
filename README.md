 # Engeto Python: Projekt 3

Třetí projekt na Python Akademií od Engeta.

## Popis Projektu

Tento projekt je určen k extrahování výsledků z webové stránky zaměřené na parlamentní volby z roku 2017. [Odkaz zde](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)

## Instalace Knihoven

Použité knihovny v kódu jsou uložené v souboru ``requirements.txt``.

Pro instalaci knihoven se dopuručuje používát nové virtualní prostředí a s nainstalovaným manažerem spusťit nasledně:

>1. ``pip --version                   # overim verzi manazeru``
>
>2. ``pip install -r requirements.txt   # nainstaluju knihovny``

## Spuštění Projektu

Spuštění projektu ``projekt_3.py`` v rámci přík. řádku požaduje dva povinné argumenty.

Následně se vám stáhnou výsledky jako soubor s příponou ``.csv``.

V mém případě jsem zadal okres ``Karvina``:

>1. ``argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&|xnumnuts=8103``
>
>2. ``argument: vysledeky_karvina.csv``                                                

Spuštění programu potom vypadá takto:

>``python projekt_3.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8103' 'vysledeky_karvina.csv'``

### Průběh stahování:

>``Downloading data from current URL``
>``Downloading data from current URL``
>``The program finished successfully``
>``Your output file: vysledeky_karvina.csv has been created``

### Častečný výstup:

>``code;location;registered voters;envelopes;valid votes;``
>``598925;Albrechtice;3173;1957;1944;``
>``599051;Bohumín;17613;9040;8973;``
>``...``