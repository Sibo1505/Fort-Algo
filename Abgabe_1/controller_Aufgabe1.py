
from api import load_language_data, get_all_words
from Aufgabe_1 import h1, h2
import random
import matplotlib.pyplot as plt
import numpy as np

# Analysetool für die Hash-Funktionen h1 und h2
def analyze_hash_functions(sample_size):

    # Lade alle Wörter
    print("Lade Wörter aus allen Sprachen...")
    word_database = load_language_data()
    all_words = get_all_words(word_database)
    
    # Zufällige Stichprobe
    sample_words = random.sample(all_words, sample_size)
    
    # Hash-Werte berechnen
    h1_values = [h1(word) for word in sample_words]
    h2_values = [h2(word) for word in sample_words]
    
    # Analyse der Verteilung
    print("\nAnalysiere Verteilung...")
    analyze_spread(h1_values, "h1")
    analyze_spread(h2_values, "h2")
    
    # Visualisierung
    print("\nSoll die Verteilung visuell dargestellt werden? (j/n)")
    if input().strip().lower() == 'j':
        plot_hash_distribution(h1_values, h2_values)

    # Kollisionsanalyse
    print("\nAnalysiere Kollisionen...")
    analyze_collisions(h1_values, "h1")
    analyze_collisions(h2_values, "h2")

# Analysiert die Verteilung der Hash-Werte
def analyze_spread(hash_values, hash_name):
    """Analysiert die Verteilung der Hash-Werte."""
    min_val = min(hash_values)
    max_val = max(hash_values)
    mean_val = np.mean(hash_values)
    
    print(f"\n{hash_name} Verteilungsanalyse:")
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")
    print(f"Mittelwert: {mean_val:.2f}")
    print(f"Genutzter Bereich: {(max_val - min_val + 1) / 100000 * 100:.2f}% des möglichen Bereichs")

# Analysiert die Kollisionen in den Hash-Werten
def analyze_collisions(hash_values, hash_name):
    """Analysiert die Kollisionen in den Hash-Werten."""
    unique_values = len(set(hash_values))
    total_values = len(hash_values)
    collisions = total_values - unique_values
    
    print(f"\n{hash_name} Kollisionsanalyse:")
    print(f"Eindeutige Werte: {unique_values}")
    print(f"Kollisionen: {collisions}")
    print(f"Kollisionsrate: {collisions/total_values*100:.2f}%")

# Visualisiert die Verteilung der Hash-Werte
def plot_hash_distribution(h1_values, h2_values):

    plt.figure(figsize=(15, 5))
    
    # h1 Verteilung
    plt.subplot(121)
    plt.hist(h1_values, bins=100, alpha=0.7)
    plt.title('Verteilung h1')
    plt.xlabel('Hash-Wert')
    plt.ylabel('Häufigkeit')
    
    # h2 Verteilung
    plt.subplot(122)
    plt.hist(h2_values, bins=100, alpha=0.7)
    plt.title('Verteilung h2')
    plt.xlabel('Hash-Wert')
    plt.ylabel('Häufigkeit')
    
    plt.tight_layout()
    plt.show()