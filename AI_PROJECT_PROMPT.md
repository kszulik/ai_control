# AI Control — bootstrap

AI_RULESET_VERSION: 1
AI_RULESET_DATE: 2026-09-20

## 1. Cel

Ten dokument jest neutralnym projektowo bootstrapem dla modelu AI.

Nie zawiera wiedzy domenowej. Jego zadaniem jest ustalenie projektu, repozytorium, źródła prawdy i procesu pracy przed analizą techniczną.

## 2. Kolejność uruchomienia

Przed większym zadaniem:

1. przeczytaj wymagane polityki z `core/`,
2. zidentyfikuj projekt,
3. wczytaj właściwy descriptor z `projects/`,
4. ustal:
   - `PRIMARY_REPO`,
   - `MODE = SINGLE_REPO | CROSS_REPO`,
   - `REFERENCE_REPOS`,
5. ustal branch i — dla większej analizy — bazowy commit SHA,
6. przejdź do punktu wejścia dokumentacji `PRIMARY_REPO`,
7. dopiero potem analizuj kod.

## 3. Zasada separacji

Nie mieszaj niejawnie:
- kodu z różnych repozytoriów,
- dokumentacji z różnych repozytoriów,
- plików z różnych rewizji,
- stanu bieżącego z materiałami historycznymi.

Kod z `REFERENCE_REPOS` nie określa stanu `PRIMARY_REPO`.

## 4. Priorytet źródeł

Szczegóły definiuje `core/SOURCE_OF_TRUTH.md`.

W skrócie:
1. bieżące jednoznaczne polecenie użytkownika,
2. jawnie wskazany nowszy plik roboczy — tylko dla jego zakresu,
3. aktualny kod `PRIMARY_REPO`,
4. aktywna dokumentacja `PRIMARY_REPO`,
5. repozytoria referencyjne,
6. archiwa i materiały historyczne,
7. wcześniejsze rozmowy.

## 5. Operacje zapisu

Bez jednoznacznego polecenia użytkownika nie wykonuj:
- zapisu do repozytorium,
- commitów,
- merge,
- Pull Requestów,
- usuwania plików.

## 6. Fazy pracy

```text
Analiza
→ Plan
→ Implementacja
→ Weryfikacja
→ Dokumentacja
→ Zakończenie
```

Szczegóły definiuje `core/WORKFLOW.md`.

## 7. Fakty i hipotezy

Rozróżniaj:
- FAKT,
- WNIOSEK,
- HIPOTEZA,
- BRAK DANYCH.

Hipoteza nie może być jedyną podstawą implementacji.

## 8. Zasada skalowalności

Nowy projekt dodaje się przez nowy descriptor w `projects/`.

Nie kopiuj globalnych polityk do repozytoriów projektowych, jeżeli nie istnieje lokalna potrzeba ich rozszerzenia.
