# Workflow

Większe zadania realizuj kolejno:

```text
Analiza
→ Plan
→ Implementacja
→ Weryfikacja
→ Dokumentacja
→ Zakończenie
```

## Analiza

Najpierw ustal:
- aktualne zachowanie,
- oczekiwane zachowanie,
- ścieżkę wykonania,
- zależności,
- ryzyka,
- niewiadome wymagające diagnostyki.

## Plan

Plan powinien być minimalny i odpowiadać zakresowi zadania.

Nie rozszerzaj zakresu bez potrzeby.

## Implementacja

Preferuj małe, odwracalne zmiany.

Nie wykonuj szerokiego refaktoringu niezwiązanego z zadaniem.

## Weryfikacja

Sama kompilacja nie potwierdza poprawności runtime.

Dobierz test do rodzaju zmiany.

## Dokumentacja

Aktualizuj istniejący dokument odpowiedzialny za zmieniony kontrakt.

Nie twórz nowego dokumentu, jeżeli właściwy już istnieje.

## Zamrożenie decyzji

Po zaakceptowaniu rozwiązania nie zmieniaj kierunku architektury bez:
- polecenia użytkownika,
- wykrycia błędu krytycznego.

Nieblokujące ulepszenia zapisuj jako przyszłą refaktoryzację.
