# Implementation Rules

Przed zmianą kodu:
- przeanalizuj aktualną implementację,
- określ pliki wymagające zmiany,
- wskaż zależności,
- oceń regresję,
- wskaż testy,
- wskaż dokumentację wymagającą aktualizacji.

Preferuj:
- małe zmiany,
- odwracalne zmiany,
- zachowanie istniejących kontraktów,
- poprawę we właściwej warstwie zamiast lokalnego obejścia.

Nie:
- refaktoryzuj szeroko bez związku z zadaniem,
- kopiuj mechanizmu między repozytoriami bez analizy różnic,
- zmieniaj architektury po jej zaakceptowaniu bez istotnego powodu.

Zmiana warstwy współdzielonej wymaga identyfikacji wszystkich zależnych targetów/modułów w `PRIMARY_REPO`.
