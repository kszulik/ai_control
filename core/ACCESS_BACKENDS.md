# Repository Access Backends

## Cel

Ta polityka rozdziela semantykę source-of-truth od technicznego sposobu dostępu
do repozytorium.

`PRIMARY_REPO` odpowiada na pytanie: **które repozytorium jest właściwe**.
`ACCESS_BACKEND` odpowiada na pytanie: **jak model uzyskuje do niego dostęp**.

Zmiana backendu nie może zmieniać hierarchii source-of-truth.

## Dozwolone backendy

### GITHUB

Obecny tryb pracy przez connector GitHub.

Jest backendem domyślnym i bezpiecznym fallbackiem.

### LOCAL_MCP

Dostęp do jawnie skonfigurowanego lokalnego checkoutu przez zaufany serwer MCP.

Przed większą analizą model musi odczytać co najmniej:
- project id,
- lokalną ścieżkę repozytorium,
- branch,
- HEAD SHA,
- dirty/clean state,
- wynik kontroli identity, jeżeli jest wymagana.

Lokalny working tree jest traktowany jako aktualny stan tylko wtedy, gdy
`ACCESS_BACKEND=LOCAL_MCP`.

### AUTO

Tryb przyszłościowy.

Nie używaj go domyślnie w wersji v0.1. Może zostać włączony dopiero po
potwierdzeniu stabilności LOCAL_MCP.

## Domyślny tryb

Jeżeli użytkownik nie wskaże inaczej:

```text
ACCESS_BACKEND = GITHUB
```

Dzięki temu wdrożenie LOCAL_MCP nie zmienia obecnego sposobu pracy.

## Fallback

Jeżeli LOCAL_MCP jest niedostępny:
- nie przełączaj niejawnie źródła podczas zadania zależnego od lokalnych
  niecommitowanych zmian,
- poinformuj o braku dostępu,
- jeżeli zadanie nie zależy od lokalnego working tree, można wrócić do GITHUB.

## Zasada rewizji

Dla LOCAL_MCP przed analizą większego zakresu pobierz `repo_status`.

Raport powinien wskazywać:
- backend,
- project,
- root,
- branch,
- HEAD,
- dirty,
- upstream/ahead/behind, jeżeli istnieją,
- identity status.

## Bezpieczeństwo

LOCAL_MCP powinien:
- mapować jawne identyfikatory projektów na katalogi,
- nie przyjmować dowolnych ścieżek systemowych,
- nie udostępniać ogólnego shella,
- ograniczać odczyt do skonfigurowanych katalogów,
- odrzucać path traversal i symlinki wychodzące poza root,
- ograniczać rozmiar odpowiedzi.

Etap v0.1 jest read-only.
Operacje zapisu, build i Git write należą do osobnych etapów wdrożenia.

## Rollback

Powrót do obecnego trybu polega na:

```text
ACCESS_BACKEND = GITHUB
```

Wyłączenie lub usunięcie LOCAL_MCP nie wymaga zmian w repozytoriach projektowych.
