# Startnummerngenerator
[![License](https://img.shields.io/badge/license-MIT-blue)](https://opensource.org/licenses/mit)

Ein Python-Tool, um Startnummern für verschiedene Läufe als PDF zu erzeugen. Die PDFs werden auf Basis einer Scribus-Vorlage generiert und am Ende zu einer Datei zusammengefügt.

## Voraussetzungen

- [Scribus](https://www.scribus.net/) (getestet mit Version 1.6.x)
- Python 3.8+
- Die Python-Bibliothek `PyPDF2`

## Nutzung

Das Tool wird über Scribus gestartet:

```bash
scribus -g --python-script run.py
```

- Es werden für alle in `data.py` definierten Läufe und Startnummern PDFs erzeugt.
- Die PDFs werden zu einer Datei `output.pdf` zusammengefügt.
- Die Datei `output.pdf` befindet sich anschließend im Projektverzeichnis.

## Anpassung

- Die Läufe und Startnummern können in `data.py` angepasst werden.
- Die Vorlage für die Startnummern ist `template.sla` (Scribus-Datei, Platzhalter: `RUN_PLACEHOLDER`, `NUMBER_PLACEHOLDER`).
- Das Hintergrundbild ist `background.png`.

## Beispiel für eigene Läufe

In `data.py` können Läufe wie folgt definiert werden:

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Run:
    id: str
    name: str
    number_range: range

all_runs = [
    Run("LDA", "Lauf der Asse", range(1, 3)),
    Run("JDML5", "5 KM Jedermannslauf", range(1, 6)),
    # weitere Läufe ...
]
```

## Hinweise

- Das Skript überschreibt die Datei `output.pdf` bei jedem Lauf.
- Die Generierung kann je nach Anzahl der Startnummern und Geschwindigkeit des Rechners einige Zeit dauern.
- Die Ausführung muss zwingend aus Scribus heraus erfolgen, da das `scribus`-Modul nur dort verfügbar ist.
