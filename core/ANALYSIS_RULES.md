# Analysis Rules

## Minimalny kompletny zakres

Nie analizuj całego projektu, jeżeli zadanie dotyczy tylko części systemu.

Analizuj jednak najmniejszy kompletny zakres potrzebny do poprawnego zrozumienia problemu.

## Klasyfikacja ustaleń

- **FAKT** — potwierdzony kodem, dokumentacją, logiem lub pomiarem.
- **WNIOSEK** — wynika z potwierdzonych faktów.
- **HIPOTEZA** — wymaga potwierdzenia.
- **BRAK DANYCH** — dostępne źródła nie rozstrzygają problemu.

## Diagnostyka

Najpierw przeanalizuj kod.

Dopiero potem używaj diagnostyki runtime do odpowiedzi na konkretną niewiadomą.

Możliwe narzędzia:
- logi,
- RTT,
- SystemView,
- debugger,
- breakpoint/watchpoint,
- analizator logiczny,
- oscyloskop,
- telemetria projektu.

## Zakaz zgadywania

Brak danych nie jest zgodą na uzupełnienie brakującej informacji przypuszczeniem.
