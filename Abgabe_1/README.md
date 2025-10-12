# Projekt Setup

1. Erstelle einen Kaggle-Account: https://www.kaggle.com
2. Gehe zu Profile → Settings → API → "Create New API Token"
3. Speichere die Datei `kaggle.json` unter:
   - Windows: C:\Users\<Benutzer>\.kaggle\kaggle.json
   - macOS/Linux: ~/.kaggle/kaggle.json
4. Installiere die nötigen Pakete:
   - pip install kagglehub pandas matplotlib numpy
5. Führe `main.py` aus, um das Programm zu starten.

### Verfügbare Funktionen

Das Programm bietet ein interaktives Menü mit folgenden Optionen:

**1. Hash-Funktionen analysieren**

- Analysiert die implementierten Hash-Funktionen h1 und h2
- Testet mit 10.000 zufälligen Wörtern aus dem Datensatz
- Zeigt Verteilungsstatistiken und Kollisionsraten
- Optional: Visualisierung der Hash-Verteilung

**2. Bloom-Filter testen**

- Testet den implementierten Bloom-Filter
- Verwendet 10.000 Wörter mit 5% Fehlerwahrscheinlichkeit
- Berechnet falsch-positive Rate
- Speichert Ergebnisse in `Ergebnisse/bloom_filter_test_results.txt`

**3. Programm beenden**

- Beendet das Programm

### Hinweise

- Beim ersten Start wird automatisch der Kaggle-Datensatz heruntergeladen
- Die Analyse kann je nach Systemleistung einige Sekunden dauern
- Ergebnisse werden im Ordner `Ergebnisse/` gespeichert
