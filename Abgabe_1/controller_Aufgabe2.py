from api import load_language_data, get_words_for_language, get_all_words
from Aufgabe_2 import BloomFilter
import random

# Testet den Bloom-Filter mit einer bestimmten Anzahl von Wörtern und dokumentiert
def test_bloom_filter(test_size, error_rate):

    # Laden der Wörter
    print("Lade Wortdaten...")
    word_database = load_language_data()
    all_words = get_all_words(word_database)
    
    # Teile die Wörter in zwei Gruppen:
    # 1. Wörter zum Einfügen in den Filter
    # 2. Wörter zum Testen auf falsch positive Ergebnisse
    insert_words = set(random.sample(all_words, test_size))
    test_words = set(random.sample([w for w in all_words if w not in insert_words], test_size))
    
    # Erstelle und fülle den Bloom-Filter
    print("\nErstelle Bloom-Filter...")
    bloom_filter = BloomFilter(n=test_size, p=error_rate)
    
    # Zeige die berechneten Parameter
    n, p, k, m = bloom_filter.getParameters()
    print(f"\nBloom-Filter Parameter:")
    print(f"Anzahl der Daten (n): {n}")
    print(f"Fehlerwahrscheinlichkeit (p): {p}")
    print(f"Anzahl der Hash-Funktionen (k): {k}")
    print(f"Anzahl der Bits (m): {m}")
    
    # Füge Wörter in den Filter ein
    print("\nFüge Wörter in den Filter ein...")
    for word in insert_words:
        bloom_filter.insert(word)
    
    # Teste die eingefügten Wörter
    true_positives = sum(1 for word in insert_words if bloom_filter.search(word))
    print(f"\nTest der eingefügten Wörter:")
    print(f"Korrekt gefunden: {true_positives} von {len(insert_words)}")
    print(f"Falsch negative Rate: {(len(insert_words) - true_positives) / len(insert_words):.4%}")
    
    # Teste auf falsch positive Ergebnisse
    false_positives = []
    for word in test_words:
        if bloom_filter.search(word):
            false_positives.append(word)
    
    # Berechne die falsch positive Rate
    false_positive_rate = len(false_positives) / len(test_words)
    print(f"\nTest auf falsch positive Ergebnisse:")
    print(f"Anzahl falsch positiver Ergebnisse: {len(false_positives)}")
    print(f"Falsch positive Rate: {false_positive_rate:.4%}")
    print(f"Theoretische Fehlerrate: {error_rate:.4%}")
    
    save_test_results(insert_words, test_words, false_positives, bloom_filter)

# Speichert die Testergebnisse in einer Datei
def save_test_results(insert_words, test_words, false_positives, bloom_filter):

    n, p, k, m = bloom_filter.getParameters()
    
    with open("Abgabe_1/Ergebnisse/bloom_filter_test_results.txt", "w", encoding="utf-8") as f:
        f.write("Bloom-Filter Testergebnisse\n")
        f.write("=========================\n\n")
        
        f.write("Parameter:\n")
        f.write(f"- Anzahl der Daten (n): {n}\n")
        f.write(f"- Fehlerwahrscheinlichkeit (p): {p}\n")
        f.write(f"- Anzahl der Hash-Funktionen (k): {k}\n")
        f.write(f"- Anzahl der Bits (m): {m}\n\n")
        
        f.write("Testergebnisse:\n")
        f.write(f"- Anzahl eingefügter Wörter: {len(insert_words)}\n")
        f.write(f"- Anzahl Testwörter: {len(test_words)}\n")
        f.write(f"- Anzahl falsch positiver Ergebnisse: {len(false_positives)}\n")
        f.write(f"- Falsch positive Rate: {len(false_positives)/len(test_words):.4%}\n\n")
        
        f.write("Beispiele für falsch positive Ergebnisse:\n")
        for word in list(false_positives)[:15]:  # Zeige nur die ersten 15 Beispiele
            f.write(f"- {word}\n")