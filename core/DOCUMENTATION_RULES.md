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


## Routing generowanych artefaktow

Przed utworzeniem pliku dokumentacji, raportu lub innego artefaktu stosuj `core/ARTIFACT_ROUTING.md`. Ta polityka określa obowiązkowy preflight, dobór instrukcji/skillów środowiska i weryfikację gotowego pliku.

## Format generowanych dokumentow i raportow

Gdy uzytkownik prosi o wygenerowanie dokumentacji, raportu, analizy lub podobnego
materialu jako pliku, domyslnym formatem wyjsciowym jest PDF.

Nie generuj dodatkowo pliku DOCX, jezeli uzytkownik o niego jawnie nie poprosil.
DOCX ani inny format edytowalny nie jest wymaganym artefaktem posrednim do
przekazania uzytkownikowi.

Jezeli uzytkownik wskaze konkretny format pliku, jego biezace polecenie ma
pierwszenstwo przed domyslnym PDF.
