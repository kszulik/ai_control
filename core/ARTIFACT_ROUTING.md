# Artifact Routing

## Cel

Ta polityka wymusza ponowny routing przed utworzeniem lub modyfikacją artefaktu plikowego. Ma zapobiegać sytuacji, w której model kontynuuje wcześniejszy workflow (np. analizę kodu) i pomija instrukcje właściwe dla nowego formatu.

## Kiedy stosować

Stosuj tę politykę zawsze, gdy bieżące polecenie przechodzi do utworzenia lub modyfikacji artefaktu, w szczególności:
- PDF,
- DOCX,
- XLSX / arkusz kalkulacyjny,
- PPTX / prezentacja,
- raport lub dokument przekazywany jako plik,
- konwersja pomiędzy formatami plików.

Kontynuacja tej samej rozmowy ani wcześniejsze załadowanie polityk projektu nie zwalniają z tego kroku.

## Obowiązkowy preflight

Przed pierwszym narzędziem tworzącym lub modyfikującym artefakt:

1. określ żądany format i cel artefaktu,
2. sprawdź aktywne polityki `ai_control` dotyczące dokumentacji/artefaktów,
3. sprawdź, czy środowisko posiada dedykowaną instrukcję lub skill dla tego formatu,
4. przeczytaj tę instrukcję/skill przed generowaniem,
5. ustal wymagany sposób weryfikacji wyniku,
6. dopiero wtedy utwórz lub zmodyfikuj plik.

Jeżeli użytkownik wskazuje konkretny format, jego bieżące polecenie ma pierwszeństwo. Jeżeli formatu nie wskazuje, zasady domyślnego formatu dokumentacji określa `core/DOCUMENTATION_RULES.md`.

## Mapowanie typowych formatów

Jeżeli środowisko udostępnia dedykowane instrukcje/skills, użyj ich odpowiednio:
- PDF -> instrukcja/skill PDF,
- DOCX -> instrukcja/skill dokumentów,
- XLSX/arkusze -> instrukcja/skill arkuszy kalkulacyjnych,
- PPTX/slajdy -> instrukcja/skill prezentacji.

Nie zastępuj dedykowanej ścieżki ogólnym narzędziem tylko dlatego, że technicznie potrafi ono utworzyć dany format.

## Weryfikacja artefaktu

Artefakt nie jest gotowy tylko dlatego, że plik został zapisany.

Po wygenerowaniu wykonaj weryfikację właściwą dla formatu zgodnie z instrukcją/skill środowiska. W zależności od formatu może to obejmować:
- render i kontrolę wizualną,
- sprawdzenie liczby stron/slajdów/arkuszy,
- kontrolę układu, przepełnień i fontów,
- sprawdzenie linków, tabel i wykresów,
- ponowne otwarcie lub walidację pliku.

Jeżeli wymaganej weryfikacji nie wykonano, nie przedstawiaj artefaktu jako w pełni zweryfikowanego.

## Zasada separacji odpowiedzialności

`ai_control` określa kiedy i jak wykonać routing oraz preflight.

Szczegółowe wymagania techniczne formatu (np. sposób renderowania PDF, budowania DOCX, styl arkusza, zasady slajdów) należą do instrukcji/skillów środowiska i nie powinny być kopiowane do tego pliku.
