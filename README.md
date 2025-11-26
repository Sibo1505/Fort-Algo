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

**Web-basierter Multi-Kriterien Routing-Algorithmus für Schleswig-Holstein**

- **PHP-Web-Anwendung** mit interaktiver Kartendarstellung
- Implementierung von Algorithmen für kürzeste (d), schnellste (t) und energieeffizienteste (e) Wege
- **30+ Städte in Schleswig-Holstein** als reales Straßennetz-Szenario
- Interaktive Auswahl von Start- und Zielknoten über Kartenklicks
- Visuelle Darstellung der berechneten Routen auf Schleswig-Holstein Karte

**Implementierte Kantentypen:**

- **Dorfstraße**: 50 km/h, 6l/100km, Kurvigkeitsfaktor 1.4
- **Landstraße**: 80 km/h, 7l/100km
- **Autobahn**: 130 km/h, 9l/100km

**Technische Features:**

- Web-Interface mit Kartengrafik (`sh.png`)
- Städte-Datenbank mit Pixel-Koordinaten für Visualisierung
- Skalierung: 1km ≈ 10px (Flensburg ↔ Neumünster: ~98km ≈ 980px)
- Dreiecksungleichung für alle Distanzberechnungen
- Unterschiedliche optimale Wege je nach Kriterium (Distanz vs. Zeit vs. Verbrauch)

**Status: 🔄 In Bearbeitung** - Siehe Ordner `Abgabe_3/`

### Programmieraufgabe 4 - GeoHash-Algorithmus

**Räumliche Indexierung mit alternativen Kodierungsschemata**

- Implementierung des GeoHash-Algorithmus für geografische Koordinaten
- Drei verschiedene Kodierungsschemata statt Standard-Base32:
  - **Base16** (Hexadezimal, 4 Bits/Zeichen)
  - **Base64** (Standard, 6 Bits/Zeichen)
  - **Custom** (32-Zeichen ohne verwechselbare Zeichen, 5 Bits/Zeichen)
- Nachbar-Algorithmus für räumliche Nachbarschaftssuche
- Interaktives Menü-System für Demonstrationen
- Praktisches Restaurant-Beispiel mit HAW Kiel Koordinaten
- Umfassende Test-Suite mit 12 Unit-Tests
- Vollständige API-Dokumentation und Präzisions-Analyse

**Funktionale Highlights:**

- Kodierung/Dekodierung geografischer Koordinaten
- Berechnung aller 8 Nachbar-GeoHashes für Umgebungssuche
- Fehlerbereich-Berechnung für Präzisions-Analyse
- Location-Based Services Demonstration

**Status: ✅ Abgeschlossen** - Siehe Ordner `Abgabe_4/`
