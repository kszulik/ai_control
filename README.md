# ai_control

Centralne repozytorium reguł sterowania modelem AI.

## Cel

Repozytorium definiuje **jak model ma pracować**, niezależnie od konkretnego projektu lub domeny.

Nie przechowuje bieżącej wiedzy technicznej o firmware, produktach ani implementacjach projektów. Wiedza techniczna pozostaje w repozytoriach, których dotyczy.

## Zasada nadrzędna

```text
ai_control
    = sposób pracy modelu

project descriptor
    = routing do właściwych repozytoriów

repozytorium projektu
    = aktualny kod i dokumentacja techniczna
```

## Punkt wejścia

Model powinien rozpocząć od:

1. `AI_PROJECT_PROMPT.md`,
2. `PROJECT_REGISTRY.md`,
3. właściwych polityk w `core/`,
4. descriptoru projektu wskazanego przez registry,
5. dokumentacji wskazanego `PRIMARY_REPO`.

## Struktura

```text
ai_control/
├── README.md
├── AI_PROJECT_PROMPT.md
├── AI_CHECKLIST.md
├── PROJECT_REGISTRY.md
├── core/
│   ├── SOURCE_OF_TRUTH.md
│   ├── REPOSITORY_ROUTING.md
│   ├── WORKFLOW.md
│   ├── ANALYSIS_RULES.md
│   ├── IMPLEMENTATION_RULES.md
│   ├── VERIFICATION_RULES.md
│   └── DOCUMENTATION_RULES.md
└── projects/
    └── cdso_paudio.md
```

## Granice odpowiedzialności

Do `ai_control` należą:
- routing repozytoriów,
- source-of-truth,
- SINGLE_REPO / CROSS_REPO,
- zasady analizy,
- zasady implementacji,
- zasady weryfikacji,
- zasady utrzymania dokumentacji,
- zasady operacji Git,
- checklisty procesu.

Do repozytoriów projektowych należą:
- architektura produktu,
- API,
- konfiguracja sprzętowa,
- algorytmy,
- aktualne parametry,
- bieżące ryzyka techniczne,
- testy i telemetria projektu,
- dokumentacja konkretnych modułów.

## Wersja rulesetu

AI_RULESET_VERSION: 1
AI_RULESET_DATE: 2026-09-20
