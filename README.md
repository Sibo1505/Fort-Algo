# Fortgeschrittene Algorithmen - Programmieraufgaben

Dieses Repository enthält die Lösungen zu den Programmieraufgaben des Kurses "Fortgeschrittene Algorithmen".

## Übersicht der Aufgaben

### Programmieraufgabe 1 - Hash-Funktionen & Bloom-Filter

**Teilaufgabe 1: Hash-Funktionen**

- Implementierung von zwei unterschiedlichen Hash-Funktionen (h1 und h2)
- Verteilung von Input-Werten auf 100.000 Zahlen (möglichst kollisionsfrei)
- Test mit Wörtern aus 30 europäischen Sprachen
- Optimierung auf gleichmäßige Verteilung und Kollisionsfreiheit
- Datenquelle: [Languages of Europe Dataset](https://www.kaggle.com/datasets/jacekpardyak/languages-of-europe)

**Teilaufgabe 2: Bloom-Filter**

- Implementierung eines Bloom-Filters mit den Hash-Funktionen aus Teilaufgabe 1
- Auslegung für 10.000 Daten mit 5% Fehlerwahrscheinlichkeit
- Methoden: `insert(element)` und `search(element)`
- Test und Dokumentation der falsch-positiven Ergebnisse

**Status: ✅ Abgeschlossen** - Siehe Ordner `Abgabe_1/`

### Programmieraufgabe 2 - Plagiats-Erkennung mit simHash

**Plagiats-Messprogramm (simHash)**

- Implementierung des simHash-Algorithmus ohne externe Libraries (numpy etc.)
- Verwendung von 3-Wort-Gruppen als Shingles ("the lazy dog", "lazy dog jumps", etc.)
- 64-Bit SimHash-Fingerprints mit einfacher Hash-Funktion
- Hamming-Distanz zur Ähnlichkeitsberechnung
- Test mit "articles.txt" (1000+ Artikel aus Moodle-System)
- Paarweiser Vergleich aller Artikel mit 90% Plagiat-Schwellenwert
- Ergebnis: 9 Plagiat-Paare mit 95-98% Ähnlichkeit gefunden

**Status: ✅ Abgeschlossen** - Siehe Ordner `Abgabe_2/`

### Programmieraufgabe 3

**Details folgen**

**Status: ⏳ Noch nicht verfügbar**

### Programmieraufgabe 4

**Details folgen**

**Status: ⏳ Noch nicht verfügbar**
