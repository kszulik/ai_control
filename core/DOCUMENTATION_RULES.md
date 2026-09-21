# Documentation Rules

## Zasada lokalności

Dokumentacja techniczna należy do repozytorium, którego stan opisuje.

Nie przenoś bieżącego stanu technicznego do `ai_control`.

## Aktualizacja

Jeżeli zmiana wpływa na:
- architekturę,
- API,
- konfigurację,
- komunikację,
- inicjalizację,
- logowanie,
- mapowanie danych,
- tor danych/audio,
- build,
- testowanie,
- algorytm,
- telemetrię,

zaktualizuj odpowiedni istniejący dokument.

## Historia

Materiały historyczne powinny być:
- oznaczone jako historyczne,
- przeniesione do Archive, jeżeli repozytorium stosuje taki katalog,
- niewykorzystywane jako bieżąca specyfikacja.

## Baseline

Dla ważnych dokumentów warto utrzymywać:
- repozytorium,
- branch,
- commit ostatniej pełnej rewalidacji,
- datę rewalidacji.

Nie oznacza to, że dokument traci ważność po każdym commicie. Wymaga ponownej oceny, gdy zmienia się kod w jego zakresie.


## Commit dokumentacji powiazanej ze zmiana kodu

Jeżeli aktualizacja dokumentacji wynika bezpośrednio z bieżącej zmiany kodu, dokumentacja musi zostać dołączona do tego samego commitu co kod.

Nie twórz następujących po sobie commitów typu:
- commit kodu,
- osobny commit "Docs" opisujący dokładnie tę samą zmianę.

Wyjątkiem jest zadanie wyłącznie dokumentacyjne lub niezależna korekta dokumentacji niewynikająca z bieżącej zmiany implementacji.
