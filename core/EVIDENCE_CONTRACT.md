# Evidence Contract

## Cel

Ta polityka definiuje minimalny poziom dowodu wymagany do stwierdzenia, że stan repozytorium, build, test lub operacja zapisu zostały rzeczywiście sprawdzone albo wykonane.

Jej celem jest wyeliminowanie deklarowania wyników, których nie potwierdza wynik narzędzia lub inne źródło dowodowe z bieżącego zadania.

## 1. Kontekst repozytorium

Przed większą analizą repozytorium ustal:

- `PROJECT`,
- `PRIMARY_REPO`,
- `MODE = SINGLE_REPO | CROSS_REPO`,
- `REFERENCE_REPOS`,
- branch,
- bazowy commit SHA, jeżeli zakres zadania wymaga pracy na konkretnej rewizji.

Nie przenoś ustaleń pomiędzy repozytoriami, branchami ani rewizjami bez jawnego porównania.

Kod z `REFERENCE_REPOS` nie potwierdza stanu `PRIMARY_REPO`.

## 2. Dowód musi odpowiadać twierdzeniu

Twierdzenie o stanie repozytorium lub wykonanej operacji musi wynikać bezpośrednio z odpowiedniego dowodu.

Nie deklaruj jako sprawdzonych ani wykonanych:

- branchu lub commit SHA,
- zawartości commita lub diffu,
- utworzenia, aktualizacji albo usunięcia pliku,
- commita, pusha, merge lub Pull Requesta,
- wyniku kompilacji,
- liczby warningów lub błędów,
- rozmiarów sekcji lub artefaktów builda,
- wyniku testu,
- zachowania firmware na urządzeniu,

jeżeli nie istnieje dowód odpowiadający dokładnie temu twierdzeniu.

Brak wyniku narzędzia nie może być uzupełniony wynikiem prawdopodobnym, oczekiwanym ani zapamiętanym z wcześniejszej rozmowy.

## 3. Poziomy weryfikacji

Stosuj następujące znaczenia:

- **VERIFIED** — właściwe repozytorium, branch lub rewizja i dana właściwość zostały bezpośrednio sprawdzone.
- **BUILD VERIFIED** — build został rzeczywiście uruchomiony dla wskazanej rewizji i jego wynik jest dostępny.
- **RUNTIME VERIFIED** — zachowanie zostało potwierdzone na właściwej wersji firmware testem runtime, pomiarem, debuggerem, logiem albo telemetrią.
- **RUNTIME UNVERIFIED** — kod lub build został sprawdzony, ale zachowanie na urządzeniu nie zostało potwierdzone.
- **HYPOTHESIS** — proponowane wyjaśnienie wymagające dalszego dowodu.
- **BRAK DANYCH** — dostępne źródła nie pozwalają potwierdzić twierdzenia.

`BUILD VERIFIED` nie oznacza `RUNTIME VERIFIED`.

Analiza kodu nie może być przedstawiana jako wynik testu sprzętowego.

## 4. Operacje zapisu

Po operacji zapisu raportuj sukces dopiero po otrzymaniu potwierdzenia z narzędzia.

Jeżeli narzędzie zwraca commit SHA, branch, identyfikator PR albo inną wartość wynikową, raportuj dokładnie tę wartość.

Nie wymyślaj:

- SHA,
- nazw branchy,
- numerów PR,
- wyników builda,
- warningów,
- wyników testów,
- danych pomiarowych,
- innych wartości wyglądających jak wynik wykonanej operacji.

Nie używaj słów takich jak „wykonane”, „zacommitowane”, „wypchnięte”, „build przeszedł” lub „potwierdzone”, jeśli odpowiadająca im operacja nie została potwierdzona.

Jeżeli zapis się nie powiódł, powiedz wprost, że zmiana nie została zapisana.

## 5. Build

Przed oznaczeniem stanu jako **BUILD VERIFIED** ustal co najmniej:

- repozytorium,
- branch lub commit SHA,
- użyty punkt wejścia builda,
- wynik procesu build.

Jeżeli build nie został uruchomiony, nie podawaj jako faktu liczby warningów, błędów, rozmiaru kodu ani wygenerowanych artefaktów.

Clean build jest wymagany, jeżeli polityka projektu lub bieżące zadanie tego wymaga.

## 6. Runtime

Zmiana firmware pozostaje **RUNTIME UNVERIFIED**, dopóki zachowanie nie zostanie potwierdzone na urządzeniu lub przez wiarygodny test wykonawczy odpowiadający danemu przypadkowi.

Wynik runtime powinien być przypisany do konkretnej wersji firmware, jeżeli jest to możliwe.

## 7. Hipoteza i root cause

Nie przechodź bez dowodu z:

`obserwacja -> hipoteza`

do:

`potwierdzona przyczyna`.

Dla diagnostyki stosuj kolejność:

`obserwacja -> fakty z kodu -> hipoteza -> test rozstrzygający -> wynik -> wniosek`.

Root cause jest potwierdzony dopiero wtedy, gdy dostępne dane rozstrzygają go względem istotnych alternatyw.

## 8. Zasada rewizji

Dowód obowiązuje dla rewizji, której dotyczy.

Jeżeli branch zmienił HEAD po analizie, wcześniejsze ustalenia nie potwierdzają automatycznie nowego stanu.

Przed operacją destrukcyjną, cofnięciem, merge albo oceną zakresu commitów ponownie sprawdź właściwy branch i SHA.

## 9. Raport końcowy

Dla większych zadań repozytoryjnych końcowy raport powinien rozróżniać, zależnie od zakresu:

- co zostało **VERIFIED**,
- co jest **BUILD VERIFIED**,
- co jest **RUNTIME VERIFIED**,
- co pozostaje **RUNTIME UNVERIFIED**,
- które elementy są nadal **HYPOTHESIS** lub **BRAK DANYCH**.

Nie twórz pozoru pełnej weryfikacji przez przemilczenie brakującego poziomu dowodu.
