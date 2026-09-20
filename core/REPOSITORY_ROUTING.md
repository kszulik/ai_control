# Repository Routing

## Kontekst zadania

Przed analizą ustal:

```text
PROJECT
PRIMARY_REPO
MODE = SINGLE_REPO | CROSS_REPO
REFERENCE_REPOS
```

## SINGLE_REPO

Domyślny tryb.

Używaj, gdy zadanie dotyczy jednego repozytorium.

Nie pobieraj zachowania z innych repozytoriów tylko dlatego, że kod jest podobny.

## CROSS_REPO

Używaj wyłącznie, gdy zadanie wymaga:
- porównania,
- migracji,
- analizy zależności,
- synchronizacji zachowania między repozytoriami.

W CROSS_REPO:
- jedno repozytorium pozostaje `PRIMARY_REPO`,
- pozostałe są `REFERENCE_REPOS`,
- każdy fakt i każda zmiana muszą wskazywać repozytorium, którego dotyczą,
- każda zmiana zapisana do innego repozytorium powinna tworzyć osobny logiczny commit.

## Dodawanie projektów

Nowy projekt należy zarejestrować przez descriptor w `projects/`.

Descriptor powinien zawierać:
- nazwę projektu,
- listę repozytoriów,
- reguły routingu,
- punkt wejścia dokumentacji każdego repozytorium,
- lokalne ograniczenia, których nie da się ująć globalnie.
