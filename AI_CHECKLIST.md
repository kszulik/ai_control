# AI Control — checklist

## Przed analizą

- [ ] Odczytano `PROJECT_REGISTRY.md`.
- [ ] Zidentyfikowano projekt.
- [ ] Wczytano descriptor wskazany przez registry.
- [ ] Ustalono `PRIMARY_REPO`.
- [ ] Ustalono `SINGLE_REPO` albo `CROSS_REPO`.
- [ ] Ustalono `REFERENCE_REPOS`, jeżeli są potrzebne.
- [ ] Ustalono branch.
- [ ] Dla większej analizy ustalono bazowy commit SHA.
- [ ] Wczytano punkt wejścia dokumentacji `PRIMARY_REPO`.
- [ ] Nie użyto repozytorium referencyjnego jako stanu repozytorium podstawowego.

## Przed implementacją

- [ ] Przeanalizowano aktualny kod i ścieżkę wykonania.
- [ ] Określono pliki wymagające zmiany.
- [ ] Określono zależności.
- [ ] Oceniono regresję.
- [ ] Wskazano wymagane testy.
- [ ] Hipotezy wymagające potwierdzenia są jawnie oznaczone.

## Po implementacji

- [ ] Zakres zmian odpowiada zadaniu.
- [ ] Nie wykonano niepowiązanego refaktoringu.
- [ ] Wykonano możliwą weryfikację.
- [ ] Wskazano elementy nieweryfikowane.
- [ ] Zaktualizowano dokumentację właściwego repozytorium.
- [ ] W CROSS_REPO rozdzielono zmiany i wnioski dla każdego repozytorium.
