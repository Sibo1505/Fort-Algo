# GeoHash-Algorithmus Implementierung

Ein GeoHash-Programm zur Konvertierung geografischer Koordinaten in Hash-Strings mit drei verschiedenen Kodierungsschemata ohne Standard-Base32.

## Projekt Setup

1. Stelle sicher, dass Python 3.6+ installiert ist
2. Navigiere zum Projektverzeichnis `Abgabe_4/`
3. Führe das Hauptprogramm aus:
   ```bash
   python menu.py
   ```

## Funktionsweise

Das Programm implementiert den GeoHash-Algorithmus mit alternativen Kodierungen:

### Kodierungsschemata

- **Base16**: 4 Bits/Zeichen (0-9, A-F) - Hexadezimal
- **Base64**: 6 Bits/Zeichen (A-Z, a-z, 0-9, +, /) - Höchste Präzision
- **Custom**: 5 Bits/Zeichen (0-9, a-z ohne i,l,o) - Benutzerfreundlich

### GeoHash-Algorithmus

- **Binäre Aufteilung**: Rekursive Halbierung der Erde (Längen-/Breitengrad)
- **Bit-Generierung**: Abwechselnde Bits für Koordinaten-Bereiche
- **Nachbar-Berechnung**: Alle 8 angrenzenden GeoHash-Zellen
- **Präzisions-Steuerung**: Variable Hash-Länge für gewünschte Genauigkeit

## Dateien

- **`geohash.py`**: Kern-Implementierung des GeoHash-Algorithmus
- **`menu.py`**: Interaktives Hauptmenü für alle Funktionen
- **`test_geohash.py`**: Unit-Tests mit 12 Testfällen
- **`restaurant_example.py`**: Praktisches Beispiel mit HAW Kiel Restaurants

## Verfügbare Funktionen

Das Programm bietet ein interaktives Menü mit folgenden Optionen:

**1. GeoHash-Demonstrator**

- Kodiert Koordinaten in alle drei Kodierungsschemata
- Dekodiert GeoHashes zurück zu Koordinaten mit Fehlerbereich
- Berechnet alle 8 Nachbar-GeoHashes für räumliche Suche
- Interaktive Eingabe und sofortige Ergebnisse

**2. Restaurant-Suche HAW Kiel**

- Demonstriert praktische Anwendung mit echten Koordinaten
- Zeigt 5 Restaurants in der Nähe der HAW Kiel (43m - 257m Entfernung)
- Verwendet GeoHash-Nachbarn für effiziente Umgebungssuche
- Berechnet Haversine-Distanzen zur Validierung

**3. Unit-Tests ausführen**

- Führt alle 12 Unit-Tests mit detailliertem Output aus
- Testet alle Funktionen: Kodierung, Dekodierung, Nachbarn, Edge-Cases
- Validiert Roundtrip-Genauigkeit und Eingabevalidierung

### Verwendung

Das Programm analysiert geografische Koordinaten mit drei verschiedenen GeoHash-Kodierungen:

```bash
python menu.py
```

**API-Verwendung:**

```python
from geohash import GeoHash

# Objekt erstellen und Koordinaten kodieren
gh = GeoHash("base64")
geohash = gh.encode(54.33265, 10.18035, precision=6)
print(f"GeoHash: {geohash}")  # → "0Hsas3"

# Dekodierung mit Genauigkeitsangabe
lat, lon, lat_err, lon_err = gh.decode(geohash)
print(f"Koordinaten: {lat:.6f}°, {lon:.6f}°")
print(f"Genauigkeit: ±{lat_err*111000:.0f}m")

# Nachbarn für räumliche Suche
neighbors = gh.get_neighbors(geohash)
print(f"8 Nachbarn: {list(neighbors.values())}")
```

**Beispiel-Ausgabe:**

```
========================================
      GeoHash Algorithmus Demo
========================================
🎯 Koordinaten: 54.332640°, 10.180270°

Base16: 'D07B1A' (±2439m)
Base64: '0Hsas3' (±38m)
Custom: 't1whnc' (±305m)

Nachbarn (Base64): ['0Hsas1', '0Hsas4', '0Hsas6', ...]
```

## Technische Details

### Algorithmus-Implementierung

- **Zeitkomplexität**: O(p) - linear zur gewählten Präzision
- **Speicherkomplexität**: O(p) - minimaler Speicherverbrauch
- **Nachbar-Berechnung**: O(1) - konstante Zeit für alle 8 Richtungen
- **Präzisions-Steuerung**: Variable Hash-Länge von 4-12 Zeichen
- **Keine Dependencies**: Verwendet nur Python Standard Library

### Unit-Tests

12 umfassende Tests validieren alle Funktionen:

```bash
python test_geohash.py
```

- **Kodierungs-Tests**: Alle 3 Schemata mit korrekten Zeichen
- **Validierungs-Tests**: Eingabeprüfung für Koordinaten und Kodierung
- **Roundtrip-Tests**: Kodierung ↔ Dekodierung Genauigkeit
- **Nachbar-Tests**: Alle 8 Richtungen korrekt berechnet
- **Edge-Case-Tests**: Grenzfälle wie Pole, Nullinsel, Datumsgrenze
- **Präzisions-Tests**: Höhere Präzision = kleinere Fehler

**Erwartete Ausgabe:**

```
Tests gesamt: 12, Erfolgreich: 12, Fehlgeschlagen: 0
```

### Hinweise

- Keine externen Dependencies - nur Python Standard Library
- Koordinaten als Dezimalgrad (z.B. 54.33265, 10.18035)
- Base64 bietet höchste Genauigkeit bei gleicher Zeichenlänge
- Präzision 6 optimal für Restaurant-Suche (~610m Zellen)
- Alle Funktionen über interaktives Menü demonstriert
