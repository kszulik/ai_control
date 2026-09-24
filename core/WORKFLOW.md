# Workflow

Większe zadania realizuj kolejno:

```text
Identyfikacja
→ Baseline
→ Analiza
→ Klasyfikacja dowodów
→ Plan
→ Implementacja
→ Final diff review
→ Weryfikacja build
→ Weryfikacja runtime/target
→ Dokumentacja
→ Commit
→ Weryfikacja HEAD
→ Zakończenie
```

Nie każdy etap wymaga osobnej wiadomości ani artefaktu. Etap można pominąć tylko wtedy, gdy nie ma zastosowania do danego zadania.

## Re-routing przy zmianie klasy operacji

Jeżeli w trakcie zadania zmienia się rodzaj wykonywanej operacji, ponownie wykonaj routing wymaganych polityk i narzędzi przed rozpoczęciem nowej klasy pracy. Dotyczy to w szczególności przejść do:
- modyfikacji kodu,
- build/test,
- operacji Git,
- generowania lub aktualizacji dokumentacji,
- generowania PDF/DOCX/XLSX/PPTX lub innego artefaktu,
- analizy plików lub danych,
- operacji na zewnętrznych systemach.

Nie zakładaj, że polityki i narzędzia dobrane dla poprzedniej klasy zadania są wystarczające dla następnej. Dla artefaktów stosuj `core/ARTIFACT_ROUTING.md`.

## Identyfikacja

Ustal projekt, `PRIMARY_REPO`, tryb pracy, repozytoria referencyjne oraz właściwą dokumentację zgodnie z bootstrapem i descriptorem projektu.

## Baseline

Przed istotną zmianą ustal branch, bazowy HEAD/commit SHA oraz zakres plików. Baseline jest punktem odniesienia dla finalnego diff review i oceny regresji.

## Analiza

Najpierw ustal:
- aktualne zachowanie,
- oczekiwane zachowanie,
- ścieżkę wykonania,
- zależności,
- ryzyka,
- powierzchnię regresji,
- niewiadome wymagające diagnostyki.

## Klasyfikacja dowodów

Oddziel fakty, wnioski, hipotezy i brak danych.

Nie uznawaj korelacji za potwierdzony root cause bez testu lub dowodu rozstrzygającego istotne alternatywy.

Stosuj `core/EVIDENCE_CONTRACT.md`.

## Plan

Plan powinien być minimalny i odpowiadać zakresowi zadania.

Nie rozszerzaj zakresu bez potrzeby.

Oddziel poprawkę wymaganą teraz od `FUTURE REFACTOR`.

## Implementacja

Preferuj małe, odwracalne zmiany.

Nie wykonuj szerokiego refaktoringu niezwiązanego z zadaniem.

Przestrzegaj `core/IMPLEMENTATION_RULES.md`, w tym zasad cross-repo i kodu generowanego.

## Final diff review

Przed commitem porównaj wynik z baseline.

Potwierdź, że:
- zmieniono wyłącznie zamierzony zakres,
- nie ma przypadkowych plików ani zmian,
- nie wprowadzono niezamierzonego refaktoringu,
- dokumentacja odpowiada zmianie,
- zakres testów pokrywa powierzchnię regresji.

## Weryfikacja build

Sama kompilacja nie potwierdza poprawności runtime.

Dobierz build do rodzaju i zakresu zmiany zgodnie z `core/VERIFICATION_RULES.md`.

## Weryfikacja runtime/target

Dla zmian zależnych od sprzętu, timingu, IRQ/DMA, audio, komunikacji lub danych rzeczywistych określ test runtime/target.

Jeżeli test nie został wykonany, stan pozostaje jawnie nieweryfikowany runtime.

## Dokumentacja

Aktualizuj istniejący dokument odpowiedzialny za zmieniony kontrakt.

Nie twórz nowego dokumentu, jeżeli właściwy już istnieje.

Po rozwiązaniu istotnego problemu sprawdź, czy potwierdzona wiedza techniczna została zapisana we właściwej dokumentacji repozytorium, a nie pozostała wyłącznie w rozmowie.

## Commit

Commituj tylko logicznie spójny, zweryfikowany zakres zgodny z poleceniem użytkownika i polityką operacji zapisu.

Kod i odpowiadająca mu dokumentacja powinny tworzyć jedną zmianę logiczną.

## Weryfikacja HEAD

Po commicie lub innej operacji zmieniającej historię sprawdź aktualny branch/HEAD i potwierdź, że wskazuje oczekiwaną rewizję.

Nie raportuj SHA z pamięci ani z planowanej operacji — używaj wyniku narzędzia.

## Zamrożenie decyzji

Po zaakceptowaniu rozwiązania nie zmieniaj kierunku architektury bez:
- polecenia użytkownika,
- wykrycia błędu krytycznego.

Nieblokujące ulepszenia zapisuj jako przyszłą refaktoryzację.
