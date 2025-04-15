# Engeto Python: Projekt 3

Třetí projekt na Python Akademií od Engeta.

## Popis Projektu

Tento projekt je určen k extrahování výsledků z webové stránky zaměřené na parlamentní volby z roku 2017. [Odkaz zde](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)

## Instalace Knihoven

Použité knihovny v kódu jsou uložené v souboru `requirements.txt`.

## Použité technologie:

>request: HTTP požadavky

>BeautifulSoup: parsování HTML

>csv: práce s CSV soubory

>sys: Zpracovávání argumentů příkazové rádky

## Instalace

Pro instalaci knihoven se dopuručuje používát nové virtualní prostředí a s nainstalovaným manažerem spusťit nasledně:

```bash
pip --version
pip install -r requirements.txt
```

## Spuštění Projektu

Spuštění projektu `projekt_3.py` v rámci přík. řádku požaduje dva povinné argumenty(URL a název výstupního souboru)

Následně se vám stáhnou výsledky jako soubor s příponou `.csv`.

V mém případě jsem zadal okres `Karvina`:

```
argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&|xnumnuts=8103

argument: vysledeky_karvina.csv
```
Spuštění programu potom vypadá takto:

```bash
python projekt_3.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8103' 'vysledeky_karvina.csv'
```
## Průběh stahování

```
Downloading data from current URL
```
```
The program finished successfully
```
```
Your output file: vysledeky_karvina.csv has been created
```


## Částečný výstup

| Kód obce | Lokace      | Registrovaní voliči | Vydané obálky | Platné hlasy |
|----------|-------------|---------------------|---------------|--------------|
| 598925   | Albrechtice | 3173                | 1957          | 1944         |
| 599051   | Bohumín     | 17613               | 9040          | 8973         |
| 598933   | Český Těšín | 19635               | 10429         | 10361        |
| 598941   | Dětmarovice | 3507                | 2061          | 2048         |
| ...      | ...         | ...                 | ...           | ...          |
