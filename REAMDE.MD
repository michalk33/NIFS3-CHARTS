### NIFS3 CHARTS
Aplikacja służy do wyznaczania naturalnej interpolacyjnej funkcji sklejanej trzeciego stopnia dla dowolnej krzywej zapisanej jako ciąg współrzędnych X i Y jej punktów (w formacie 'csv'). Dzięki temu można wyznaczyć krzywą interpolującą z dowolną precyzją (w aplikacji ograniczenie dolne to 5 punktów).

# Obsługa
Aby utworzyć nowy projekt, należy w zakładce *New project* dokonać wyboru pliku, w którym znajdują się dane dotyczące krzywej, oraz wpisać nazwę nowego projektu. Listę już utworzonych projektów można zobaczyć w zakładce *List of projects*. Dla każdego już utworzonego projektu można w zakładce *New chart* wyznaczyć krzywą interpolującą, poprzez wpisanie nazwy projektu oraz oczekiwanej liczby punktów. Wciskając *Save chart* dokonuje się wyboru lokalizacji pliku graficznego będącego wizualizacją nowej krzywej (format `png`), natomiast wciskając *Save chart data* dokonuje się wyboru miejsca zapisu współrzędnych punktów nowej krzywej (w formacie `csv`).
Aby uruchomić aplikację, należy wywołać w katalogu *src* `python3 main.py`. Jeżeli podczas użytkowania wystąpią błędy, najlepiej uruchomić jeszcze raz `sudo python3 main.py`.
Do poprawnego działania, wymagane jest istnienie katalogów *data* oraz *projects* z plikiem `projects.csv` (początkowo pustym).

# Testy
Aby uruchomić testy, należy w katalogu *tests* wywołać `python3 test1.py`.

# Dokumentacja
Do wygenerowania dokumentacji zostało użyte polcenie `pydoctor --docformat=numpy src/` (wywołane w katalogu głównym projektu).

# Przykładowe pliki
W katalogu *examples* znajdują się przykładowe wykresy oraz dane krzywych.
