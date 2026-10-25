Budżet domowy

Aplikacja internetowa do planowania miesięcznego budżetu domowego. Umożliwia zapisywanie dochodów i planowanych wydatków, zarządzanie nimi oraz sprawdzanie podsumowania finansowego dla wybranego miesiąca.


Funkcjonalności

- Wybór miesiąca, dla którego zarządzany jest budżet.
- Dodawanie źródeł dochodu.
- Dodawanie wydatków z przypisaniem do kategorii.
- Edytowanie i usuwanie dochodów oraz wydatków.
- Obliczanie sumy dochodów i wydatków.
- Wyświetlanie pozostałych środków dla wybranego miesiąca.

Wykorzystane technologie

Python – logika aplikacji.
Flask – obsługa aplikacji internetowej.
Flask-SQLAlchemy – integracja Flaska z bazą danych.
SQLAlchemy ORM – obsługa modeli i operacji na danych.
SQLite – przechowywanie danych.
HTML – struktura stron.
CSS – stylizacja interfejsu.
Bootstrap – formatowanie elementów interfejsu.


Instalacja i uruchomienie

Wymagania:
- Zainstalowany Python.
- Git.

1. Sklonuj repozytorium

git clone <ADRES_REPOZYTORIUM>

2. Przejdź do katalogu projektu

cd budget_analysis

3. Utwórz środowisko wirtualne

python -m venv my_env

4. Aktywuj środowisko wirtualne

W systemie Windows, w wierszu polecenia (CMD), wykonaj:

my_env\Scripts\activate.bat

5. Zainstaluj wymagane biblioteki

python -m pip install -r requirements.txt

6. Uruchom aplikację

python app.py

Następnie otwórz w przeglądarce lokalny adres wyświetlony w terminalu.

Baza danych

Aplikacja wykorzystuje bazę danych SQLite do przechowywania informacji o dochodach i wydatkach. Baza danych jest tworzona lokalnie podczas inicjalizacji aplikacji.
