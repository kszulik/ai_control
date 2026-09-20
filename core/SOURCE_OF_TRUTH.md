# Source of Truth

## Hierarchia

Dla bieżącego zadania obowiązuje:

1. bieżące jednoznaczne polecenie użytkownika,
2. jawnie wskazany nowszy plik lub pakiet roboczy użytkownika — wyłącznie dla zakresu, którego dotyczy,
3. aktualny kod `PRIMARY_REPO`,
4. aktywna dokumentacja `PRIMARY_REPO`,
5. `REFERENCE_REPOS` — wyłącznie do porównania,
6. archiwa, snapshoty, kopie robocze i materiały historyczne,
7. wcześniejsze rozmowy.

## Rewizja

Jeżeli użytkownik wskazuje branch, tag lub commit — użyj wskazanej rewizji.

Jeżeli nie wskazuje — użyj domyślnej gałęzi repozytorium.

Nie przełączaj samodzielnie na inny branch tylko dlatego, że wydaje się nowszy lub bardziej odpowiedni.

## Pliki użytkownika

Nowszy plik użytkownika może zastąpić wersję repozytoryjną tylko w jawnie wskazanym zakresie.

Nie oznacza to automatycznego zastąpienia całego repozytorium.

## Rozbieżność kod–dokumentacja

Jeżeli kod i dokumentacja są rozbieżne:
- wskaż rozbieżność,
- ustal stan z aktualnego kodu,
- nie zgaduj brakujących informacji,
- nie implementuj na podstawie samej hipotezy,
- wskaż dokument wymagający aktualizacji.
