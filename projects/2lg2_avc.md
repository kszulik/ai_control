# Project Descriptor — 2LG2_AVC

## PROJECT

```text
PROJECT = 2LG2_AVC
```

## Repozytoria

```text
PRIMARY_REPO = kszulik/2lg2_AVC
MODE = SINGLE_REPO
REFERENCE_REPOS = []
```

## Routing

Ten descriptor obowiązuje dla zadań dotyczących niezależnego projektu AVC
rozwijanego w repozytorium `kszulik/2lg2_AVC`.

Nie traktuj produkcyjnych repozytoriów CDSO jako źródła bieżącego stanu tego
projektu.

Migracja AVC do CDSO jest osobnym zadaniem CROSS_REPO i wymaga jawnego
przełączenia projektu/descriptoru.

## Documentation entrypoint

Pierwszy dokument do odczytu:

```text
documents/README.md
```

Następnie, zależnie od zadania:
- `documents/AVC_STATUS.md`,
- `documents/2LG2_AVC_telemetria_instrukcja_testow.md`.

Materiały historyczne/checklistowe nie zastępują bieżącego kodu ani aktywnego
statusu.

## Build

Podstawowy build repozytorium:

```text
make clean
make
```

Build nie zastępuje testów runtime/telemetrii wymaganych dla zmian AVC.

## ACCESS_BACKEND

Domyślnie:

```text
ACCESS_BACKEND = GITHUB
```

Dla lokalnego checkoutu może zostać jawnie użyty:

```text
ACCESS_BACKEND = LOCAL_MCP
LOCAL_MCP_PROJECT = 2lg2_avc
```

Zmiana backendu nie zmienia `PRIMARY_REPO`.
