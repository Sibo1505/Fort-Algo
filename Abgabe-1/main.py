from controller_Aufgabe1 import analyze_hash_functions
from controller_Aufgabe2 import test_bloom_filter

def print_menu():
    print("\nHauptmenü:")
    print("1. Hash-Funktionen analysieren")
    print("2. Bloom-Filter testen")
    print("3. Programm beenden")
    print("\nBitte wählen Sie eine Option (1-3):")

def main():
    while True:
        print_menu()
        choice = input().strip()
        
        if choice == "1":
            # Teste die Hash-Funktionen mit einer Stichprobe von 10.000 Wörtern
            analyze_hash_functions(10000)
        elif choice == "2":
            # Teste den Bloom-Filter mit 10.000 Wörtern und 5% Fehlerwahrscheinlichkeit
            test_bloom_filter(10000, 0.05)
        elif choice == "3":
            print("Programm wird beendet. Auf Wiedersehen!")
            return False
        else:
            print("Ungültige Eingabe! Bitte wählen Sie 1, 2 oder 3.")

if __name__ == "__main__":
    main()