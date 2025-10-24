# SimHash Plagiat-Checker

Ein Plagiats-Messprogramm mit dem SimHash-Algorithmus zur Überprüfung der Ähnlichkeit von Texten ohne zusätzliche Libraries wie numpy.

## Projekt Setup

1. Stelle sicher, dass Python installiert ist
2. Navigiere zum Projektverzeichnis `Abgabe_2/`
3. Führe das Hauptprogramm aus:
   ```bash
   python3 tracker.py
   ```

## Funktionsweise

Das Programm implementiert den SimHash-Algorithmus zur Erkennung von Plagiaten:

### SimHash-Algorithmus

- **Shingles**: Verwendet 3-Wort-Gruppen (z.B. "the lazy dog", "lazy dog jumps", "dog jumps over")
- **Hash-Funktion**: Einfache deterministische 64-Bit Hash-Funktion
- **Fingerprint**: Erstellt 64-Bit SimHash-Fingerprints für jeden Text
- **Ähnlichkeitsberechnung**: Verwendet Hamming-Distanz zur Bestimmung der prozentualen Ähnlichkeit

### Plagiat-Erkennung

- **Schwellenwert**: Texte mit ≥90% Ähnlichkeit gelten als Plagiate
- **Paarweiser Vergleich**: Alle Artikel werden miteinander verglichen
- **Ergebnis**: Ausgabe aller gefundenen Plagiat-Paare mit Ähnlichkeitsprozentsatz

## Dateien

- **`tracker.py`**: Hauptprogramm für die Plagiat-Analyse
- **`function.py`**: Implementierung des SimHash-Algorithmus und Hilfsfunktionen
- **`articles.txt`**: Testdatei mit 1000+ Artikeln (Format: ID Text)

## Verfügbare Funktionen

### `function.py`

- `load_articles(path)`: Lädt Artikel aus Datei und berechnet SimHash-Fingerprints
- `simhash(text)`: Berechnet 64-Bit SimHash-Fingerprint für einen Text
- `get_shingles(text, size=3)`: Erstellt 3-Wort-Kombinationen aus Text
- `simple_hash(shingle)`: Einfache Hash-Funktion für Shingles
- `hamming_distance(x, y)`: Berechnet Hamming-Distanz zwischen zwei Fingerprints
- `similarity(x, y)`: Berechnet prozentuale Ähnlichkeit (100% = identisch)

### `tracker.py`

- Hauptprogramm zur Ausführung der Plagiat-Analyse
- Lädt alle Artikel aus `articles.txt`
- Führt paarweisen Vergleich aller Artikel durch
- Gibt alle Plagiat-Paare mit Ähnlichkeit ≥90% aus

## Verwendung

Das Programm analysiert automatisch alle Artikel in der `articles.txt` Datei:

```bash
python3 tracker.py
```

**Beispiel-Ausgabe:**

```
SimHash Plagiat-Checker
========================================
Analysiere 1001 Artikel...
t120 und t125 -> 92.19% Ähnlichkeit
t120 und t126 -> 90.63% Ähnlichkeit
t125 und t126 -> 95.31% Ähnlichkeit

Ergebnis: 3 Plagiat-Paare gefunden.
```

## Technische Details

- **Shingle-Größe**: 3 Wörter (optimaler Kompromiss zwischen Genauigkeit und Performance)
- **Hash-Größe**: 64 Bit für ausreichende Kollisionsresistenz
- **Plagiat-Schwelle**: 90% Ähnlichkeit
- **Keine externen Dependencies**: Verwendet nur Standard-Python-Bibliotheken
