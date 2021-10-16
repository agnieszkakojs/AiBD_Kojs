Plik, który mówi skąd się co wzięło. 
oryginalne dane -> skrypt do importowania danych -> skypt do wyczyszczenia danych -> itd.
Jesteśmy w stanie prześledzić cała ścieżkę co zostało zrobione.

Ścieżka analizy danych.
1. Importowanie pliku z oryginalnymi danymi, które znajdują się w pliku Original Data, znajduje się w skrypcie Analiza_danych 
w folderze Command Files. 

2. Przetwarzanie danych:
Przetwarzanie danych znajduje się w pliku Analiza_danych.ipynb w folderze Command Files. </br>
- Na samym początku zostały zmienione nazwy column na krótsze i bardziej ogólne. 
- Następnie w kolumnie, która dotyczyła pieniędzy, wartości NaN zostały zmienione na "Prefer not to answer". 
- W kolejnym kroku wszystkie wiersze, w których występował jakikolwiek NaN zostały usunięte. Wszystkie odpowiedzi były 
obiektywne, dlatego nie dało się ich zastąpić żadnymi innymi danymi.
- Na koniec zostały zaktualizowane wszystkie indeksy danych.
- Przetworzone dane zostały zapisane w folderze Analysis Data jako "earthquake_data_clean.csv".

3. Z przetworzonych danych w tym samym pliku Analiza_danych.ipynb została utworzona tabela, która
łączy wiek, płeć i odpowiedź na pytanie ""Do you think the "Big One" will occur in your lifetime?".
Tabela ta jako plik csv została zapisana w folderze Analysis Data jako "earthquake_data_newframe.csv"