# Project Registry

## Cel

Ten plik jest centralnym indeksem projektów obsługiwanych przez `kszulik/ai_control`.

Model powinien używać go do identyfikacji właściwego descriptoru projektu przed wyborem repozytorium implementacyjnego.

## Zasady

1. Każdy projekt ma dokładnie jeden aktywny descriptor w `projects/`.
2. Descriptor definiuje routing repozytoriów i punkty wejścia dokumentacji.
3. Registry nie zawiera wiedzy technicznej projektu.
4. Jeżeli projekt nie jest zarejestrowany, model nie powinien zgadywać na podstawie podobnej nazwy ani istniejącego repozytorium.
5. Dodanie nowego projektu wymaga:
   - utworzenia descriptoru,
   - dodania wpisu do tego registry,
   - określenia jednoznacznych reguł routingu.

## Projekty

| Project | Descriptor | Status | Zakres |
|---|---|---|---|
| CDSO_pAudio | `projects/cdso_paudio.md` | ACTIVE | wielorepozytoryjny projekt firmware/audio |
| 2LG2_AVC | `projects/2lg2_avc.md` | ACTIVE | niezależny projekt rozwojowy AVC dla karty 2LG2 |

## Identyfikacja projektu

Dla bieżącego zadania:

1. dopasuj projekt do kontekstu użytkownika,
2. potwierdź wpis w tym registry,
3. otwórz descriptor,
4. dopiero potem ustal `PRIMARY_REPO`.

Jeżeli więcej niż jeden projekt pasuje do zadania i nie można rozstrzygnąć wyboru na podstawie bieżącego kontekstu, nie wybieraj losowo. Ustal brakującą informację przed rozpoczęciem pracy technicznej.

## Dodawanie nowego projektu

Nowy wpis powinien mieć postać:

```text
Project:
Descriptor:
Status:
Zakres:
```

Descriptor powinien zawierać co najmniej:
- nazwę projektu,
- repozytoria,
- reguły routingu,
- documentation entrypoints,
- ograniczenia specyficzne dla projektu.
