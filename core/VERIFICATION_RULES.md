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
