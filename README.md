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

### Programmieraufgabe 3 - Kürzeste/Schnellste/Energieeffizienteste Wege

**Multi-Kriterien Routing-Algorithmus**

- Implementierung eines Algorithmus für kürzeste (d), schnellste (t) und energieeffizienteste (e) Wege
- Reales Szenario mit mindestens 30 Knoten
- Freie Wahl von Start- und Endknoten
- Dreiecksungleichung gilt für alle Berechnungen

**Kantentypen und Parameter:**

- **Dorfstraße**: 50 km/h, 6l/100km, Faktor 1.4 für Kurvigkeit
- **Landstraße**: 80 km/h, 7l/100km
- **Autobahn**: 130 km/h, 9l/100km

**Funktionale Anforderungen:**

- Verschiedene Geschwindigkeiten je Kantentyp
- Verschiedene Kraftstoffverbräuche je Kantentyp
- Test-Fälle mit unterschiedlichen optimalen Wegen für d, t, e
- Luftlinie als Basis für nicht definierte Kanten

**Nicht-funktionale Anforderungen:**

- Ansehnliche Visualisierung der berechneten Routen
- Gut strukturierter, modularer Code
- Interaktive Auswahl von Start/Ziel-Knoten

**Referenz-Daten:**

- Schleswig-Holstein Straßennetz (Flensburg ↔ Neumünster: ~98km ≈ 980px)
- Skalierung: 1km ≈ 10px Luftlinie

**Status: 🔄 In Bearbeitung**

### Programmieraufgabe 4

**Details folgen**

**Status: ⏳ Noch nicht verfügbar**
