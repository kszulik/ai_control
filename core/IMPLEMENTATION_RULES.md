# Implementation Rules

## Baseline przed zmianą

Przed istotną zmianą kodu ustal i zachowaj punkt odniesienia:

- `PRIMARY_REPO`,
- branch,
- HEAD/bazowy commit SHA,
- pliki objęte planowaną zmianą,
- aktualne zachowanie istotne dla zadania.

Baseline musi pochodzić z bieżącego repozytorium i rewizji. Nie odtwarzaj go z pamięci rozmowy, jeżeli można sprawdzić repozytorium.

Przed zmianą kodu:
- przeanalizuj aktualną implementację,
- określ pliki wymagające zmiany,
- wskaż zależności,
- oceń powierzchnię regresji,
- wskaż testy,
- wskaż dokumentację wymagającą aktualizacji.

## Zakres zmiany

Bieżące polecenie użytkownika określa zakres mutacji.

Polecenie „sprawdź”, „przeanalizuj”, „porównaj” lub równoważne nie jest zgodą na zapis do repozytorium.

Polecenie „popraw” lub równoważne pozwala zmienić kod w zakresie koniecznym do rozwiązania wskazanego problemu, ale nie oznacza automatycznej zgody na:
- niezwiązany refactoring,
- zmiany w innych repozytoriach,
- merge,
- usuwanie branchy,
- cofanie niezwiązanych commitów.

Preferuj:
- małe zmiany,
- odwracalne zmiany,
- zachowanie istniejących kontraktów,
- poprawę we właściwej warstwie zamiast lokalnego obejścia.

Nie:
- refaktoryzuj szeroko bez związku z zadaniem,
- kopiuj mechanizmu między repozytoriami bez analizy różnic,
- zmieniaj architektury po jej zaakceptowaniu bez istotnego powodu.

Nieblokujące ulepszenie niezwiązane bezpośrednio z naprawą oznacz jako `FUTURE REFACTOR` i nie włączaj go do bieżącej poprawki bez potrzeby.

## Cross-repo

Przeniesienie rozwiązania pomiędzy repozytoriami wymaga jawnego porównania istotnych kontraktów, zależności i różnic implementacyjnych.

Podobna nazwa pliku, modułu, karty lub funkcji nie jest dowodem zgodności.

Kod z repozytorium referencyjnego może służyć jako wzorzec, ale nie określa automatycznie poprawnej implementacji w `PRIMARY_REPO`.

## Kod generowany

Przed zmianą pliku ustal, czy jest:
- źródłem utrzymywanym ręcznie,
- plikiem generowanym,
- plikiem częściowo generowanym z chronionymi sekcjami użytkownika.

Nie umieszczaj trwałej poprawki w kodzie, który zostanie nadpisany przez generator, jeżeli istnieje właściwe źródło konfiguracji, template, sekcja user-code albo warstwa rozszerzenia.

Jeżeli konieczna jest zmiana kodu generowanego, wskaż ryzyko regeneracji i źródło, z którego plik powstaje.

## Powierzchnia regresji

Dla zmiany zidentyfikuj funkcje, targety i mechanizmy, na które może ona wpłynąć pośrednio.

W szczególności zmiany w warstwach współdzielonych, schedulerze, IRQ, DMA, timerach, komunikacji, routingu, pamięci lub synchronizacji wymagają oceny zależnych ścieżek.

Zmiana warstwy współdzielonej wymaga identyfikacji wszystkich zależnych targetów/modułów w `PRIMARY_REPO`.

## Final diff review

Po implementacji, a przed uznaniem zmiany za gotową do commitu:

1. porównaj finalny stan z baseline,
2. sprawdź listę zmienionych plików,
3. sprawdź, czy każda zmiana należy do zakresu zadania,
4. wykryj przypadkowe zmiany, artefakty generatorów i niezamierzone formatowanie,
5. sprawdź zgodność kodu z dokumentacją,
6. sprawdź, czy powierzchnia regresji nadal odpowiada planowi.

Build nie zastępuje final diff review.

## Granularnosc commitow

Zmiana kodu i odpowiadajaca jej aktualizacja dokumentacji stanowia jedna zmiane logiczna i powinny trafic do tego samego commitu.

Nie tworz osobnego commitu tylko dla dokumentacji, jezeli dokumentacja opisuje zmiane kodu wykonywana w tym samym zadaniu.

Osobny commit dokumentacyjny jest uzasadniony tylko wtedy, gdy:
- zmiana dotyczy wyłącznie dokumentacji,
- dokumentacja opisuje osobny zakres niezwiązany z bieżącą zmianą kodu,
- wymagane jest historyczne lub administracyjne uporządkowanie dokumentacji.
