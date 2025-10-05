import random
import matplotlib.pyplot as plt
from hash_function import h1, h2

# Globale Variable für die Wortliste
words = []

def set_words(word_list):
    """Setzt die globale Wortliste"""
    global words
    words = word_list

def get_hash_function():
    """Lässt den Benutzer die Hash-Funktion auswählen."""
    while True:
        print("\nWähle die Hash-Funktion:")
        print("1. h1 (Polynomiale Hash-Funktion)")
        print("2. h2 (Bit-Manipulation Hash-Funktion)")
        choice = input("Deine Wahl (1/2): ").strip()
        
        if choice == "1":
            return h1
        elif choice == "2":
            return h2
        else:
            print("Ungültige Eingabe! Bitte 1 oder 2 wählen.")

def random_word_hash():
    """Wählt ein zufälliges Wort aus der CSV und gibt dessen Hashwert aus."""
    hash_func = get_hash_function()
    word = random.choice(words)
    hash_val = hash_func(word)
    print(f"Zufälliges Wort: {word} -> Hash: {hash_val}")

def user_word_hash():
    """Der Nutzer kann ein Wort eingeben, das dann gehasht wird."""
    hash_func = get_hash_function()
    word = input("Gib ein Wort ein: ").strip()
    hash_val = hash_func(word)
    print(f"Eingegebenes Wort: {word} -> Hash: {hash_val}")

def full_dataset_hash_distribution():
    """Hasht alle Wörter und erstellt ein detailliertes Histogramm zur Hashverteilung."""
    hash_func = get_hash_function()
    func_name = "h1" if hash_func == h1 else "h2"
    hashes = [hash_func(w) for w in words]

    plt.figure(figsize=(12, 6))
    plt.hist(
        hashes,
        bins=200,                # mehr Bins = feinere Auflösung
        color='cornflowerblue',
        edgecolor='black',
        alpha=0.8
    )

    # Zusatzinfos
    plt.title(f"Verteilung der Hashwerte ({func_name})", fontsize=16, fontweight='bold')
    plt.xlabel("Hashwert (0 – 100000)", fontsize=13)
    plt.ylabel("Anzahl Wörter", fontsize=13)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Statistische Werte im Plot anzeigen
    mean_val = sum(hashes) / len(hashes)
    plt.axvline(mean_val, color='red', linestyle='dashed', linewidth=1.5, label=f"Mittelwert: {int(mean_val)}")
    plt.legend()

    plt.tight_layout()
    plt.show()

def show_menu():
    print("\n=== Hash-Funktionen Menu ===")
    print("1. Zufälliges Wort hashen")
    print("2. Eigenes Wort hashen")
    print("3. Hash-Verteilung anzeigen")
    print("4. Exit")
    return input("\nWähle eine Option (1-4): ")

def main():
    running = True
    while running:
        choice = show_menu()
        
        if choice == "1":
            random_word_hash()
        elif choice == "2":
            user_word_hash()
        elif choice == "3":
            full_dataset_hash_distribution()
        elif choice == "4":
            print("\nProgramm wird beendet...")
            running = False
        else:
            print("\nUngültige Eingabe! Bitte wähle eine Zahl zwischen 1 und 4.")
        
        if running:
            input("\nDrücke Enter um fortzufahren...")