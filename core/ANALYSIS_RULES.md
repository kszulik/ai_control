# Analysis Rules

## Minimalny kompletny zakres

Nie analizuj całego projektu, jeżeli zadanie dotyczy tylko części systemu.

Analizuj jednak najmniejszy kompletny zakres potrzebny do poprawnego zrozumienia problemu.

## Code-first revalidation

Przy analizie bieżącej implementacji aktualny kod `PRIMARY_REPO` ma pierwszeństwo przed pamięcią rozmowy, wcześniejszymi ustaleniami i wiedzą modelu o projekcie.

Wcześniejsza rozmowa, pamięć modelu i wcześniejsze wyniki mogą służyć do:
- wskazania, czego szukać,
- zawężenia zakresu,
- zbudowania hipotezy,
- odnalezienia prawdopodobnych symboli lub plików.

Nie mogą zastępować sprawdzenia aktualnego kodu, jeżeli dane twierdzenie można rozsądnie zweryfikować w `PRIMARY_REPO`.

Przed wykorzystaniem twierdzenia o aktualnej implementacji jako przesłanki do diagnozy, zmiany kodu albo oceny regresji ponownie zweryfikuj je w bieżącej rewizji.

Dotyczy to w szczególności:
- call-site i ścieżek wykonania,
- konfiguracji IRQ i priorytetów,
- DMA, timerów i peryferiów,
- routingu danych lub audio,
- inicjalizacji i recovery,
- flag i warunków logicznych,
- wartości konfiguracyjnych,
- mapowania pamięci,
- zależności między modułami,
- kodu generowanego.

Jeżeli istotny fakt implementacyjny był potwierdzony wcześniej, ale nie został sprawdzony w bieżącej rewizji, nie traktuj go automatycznie jako aktualnego faktu.

## Traceability ustaleń

Dla istotnego twierdzenia o implementacji utrzymuj możliwość wskazania jego podstawy w formie:

`repo -> branch/SHA -> plik -> symbol/funkcja`

Nie wymaga to cytowania każdego wiersza w odpowiedzi użytkownikowi, ale dowód powinien pochodzić z właściwej rewizji i być możliwy do odtworzenia.

Jeżeli wniosek zależy od kilku etapów wykonania, prześledź minimalny kompletny łańcuch zamiast zakładać poprawność etapów pośrednich.

Przykład:

`wejście -> ustawienie stanu -> propagacja -> warunek -> przetwarzanie -> wyjście`

## Klasyfikacja ustaleń

- **FAKT** — potwierdzony kodem, dokumentacją, logiem lub pomiarem właściwym dla bieżącego zakresu i rewizji.
- **WNIOSEK** — wynika z potwierdzonych faktów.
- **HIPOTEZA** — wymaga potwierdzenia.
- **BRAK DANYCH** — dostępne źródła nie rozstrzygają problemu.

Fakt historyczny nie jest automatycznie faktem bieżącej rewizji.

## Diagnostyka

Najpierw przeanalizuj aktualny kod.

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

Jeżeli fakt można sprawdzić w aktualnym kodzie bez nieproporcjonalnego kosztu, sprawdź go zamiast zakładać.
