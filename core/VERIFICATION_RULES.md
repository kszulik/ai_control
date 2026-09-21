# Verification Rules

## Zasada

Weryfikacja musi odpowiadać rodzajowi zmiany.

## Poziomy

Możliwe poziomy:
- analiza statyczna,
- build,
- clean build,
- test jednostkowy,
- test integracyjny,
- test runtime,
- pomiar sprzętowy,
- test regresyjny,
- telemetria.

## Build

Po każdej zmianie kodu należy wykonać i zweryfikować build odpowiedniego targetu przed uznaniem zadania za zakończone.

Domyślnie wykonuj clean build, aby wyeliminować wpływ nieaktualnych obiektów pośrednich.

Jeżeli zmiana dotyczy warstwy współdzielonej, należy:
- zidentyfikować wszystkie zależne targety,
- wykonać build wymaganych targetów albo jednoznacznie wskazać, których nie zweryfikowano.

Jeżeli dla danego targetu nie istnieje działające środowisko lub automatyzacja builda:
- skonfiguruj możliwość powtarzalnego wykonania builda w repozytorium, preferencyjnie CI,
- dopiero następnie wykonaj i zweryfikuj build,
- nie uznawaj samej analizy statycznej za zastępstwo dla builda.

Każdy raport po zmianie kodu musi podać:
- target,
- commit/branch,
- wariant builda,
- toolchain,
- wynik,
- liczbę błędów i warningów,
- targety wymagane, ale nieweryfikowane.

Build potwierdza wyłącznie możliwość kompilacji/linkowania.

Nie potwierdza:
- poprawności czasowej,
- poprawności sprzętowej,
- zachowania ISR/DMA,
- jakości audio,
- działania algorytmu na danych rzeczywistych.

## Raport

Zawsze rozdziel:
- wykonane testy,
- testy niewykonane,
- znane ograniczenia,
- wynik dla każdego zweryfikowanego zakresu.
