# Project descriptor: CDSO_pAudio

## Project

```text
PROJECT = CDSO_pAudio
```

Projekt obejmuje trzy niezależne repozytoria:

- `kszulik/cdso_new` — CDSO z nową komunikacją,
- `kszulik/cdso_old` — aktywna linia CDSO ze starą komunikacją,
- `kszulik/2lg2_AVC` — osobny projekt rozwojowy Auto Volume Control dla 2LG2.

## Routing

Domyślnie:

- nowa komunikacja CDSO → `kszulik/cdso_new`,
- stara komunikacja CDSO → `kszulik/cdso_old`,
- AVC / projekt rozwojowy 2LG2 → `kszulik/2lg2_AVC`.

## Documentation entrypoints

### cdso_new

```text
CDSO/System.org/documentation/README.txt
```

### cdso_old

```text
CDSO/System.org/documentation/README.txt
```

### 2lg2_AVC

```text
documents/README.md
```

## Ograniczenia projektu

- `cdso_old` jest aktywną linią firmware, nie archiwum.
- Nie należy zakładać zgodności implementacji 2LG2 z `2lg2_AVC` z produkcyjnym 2LG2 w repozytoriach CDSO.
- Migracja AVC do CDSO jest zadaniem `CROSS_REPO`.
- Kod z repozytorium referencyjnego służy do porównania i nie określa aktualnego stanu `PRIMARY_REPO`.

## Lokalna wiedza techniczna

Nie przechowuj tutaj:
- parametrów kodeków,
- konfiguracji DMA/I2S,
- aktualnych bugów,
- statusów testów,
- wartości algorytmów,
- szczegółów UI,
- ryzyk technicznych.

Te informacje należą do dokumentacji właściwego repozytorium.


## Model governance

Globalne zasady pracy modelu dla projektu CDSO_pAudio pochodzą z `kszulik/ai_control`.

Repozytoria `cdso_new` i `cdso_old` utrzymują jedynie cienkie adaptery:
- `documentation/project/AI_PROJECT_PROMPT.md`,
- `documentation/project/AI_WORKFLOW.md`,
- `documentation/project/AI_CHECKLIST.md`.

Adaptery nie mogą definiować alternatywnego globalnego workflow.

`2lg2_AVC/documents/README.md` pełni lokalny punkt wejścia technicznego i również nie definiuje globalnych polityk AI.
