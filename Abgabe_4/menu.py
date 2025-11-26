import os
import sys
from geohash import GeoHash
from restaurant_example import restaurant_search_example
from test_geohash import run_tests

# Hilfsfunktionen für das Menüsystem - cleart Konsole etc.
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Zeigt das Hauptmenü
def show_main_menu():
    clear_screen()
    print("=" * 70)
    print("🌍 GeoHash-Algorithmus - Hauptmenü")
    print("=" * 70)
    print()
    print("Wählen Sie eine Option:")
    print()
    print("1. 🧪 GeoHash-Demonstrator")
    print("2. 🍕 Restaurant-Suche HAW Kiel")
    print("3. 🧾 Unit-Tests ausführen")
    print("0. ❌ Programm beenden")
    print()
    print("=" * 70)


# GeoHash-Demonstrator - Menü
def geohash_demonstrator():
    clear_screen()
    print("=" * 70)
    print("🧪 GeoHash-Demonstrator")
    print("=" * 70)
    print()
    
    while True:
        print("\nWas möchten Sie testen?")
        print()
        print("1. 📍 Koordinaten kodieren & dekodieren")
        print("2. 🗺️  Nachbar-GeoHashes finden")
        print("0. ⬅️  Zurück zum Hauptmenü")
        print()
        
        choice = input("Ihre Wahl: ").strip()
        
        if choice == "1":
            encode_decode_demo()
        elif choice == "2":
            neighbors_demo()
        elif choice == "0":
            break
        else:
            print("❌ Ungültige Eingabe! Bitte wählen Sie 0-2.")
            input("\nDrücken Sie Enter zum Fortfahren...")

# Kodieren und Dekodieren demonstrieren
def encode_decode_demo():
    print("\n" + "=" * 50)
    print("📍 GeoHash Kodierung & Dekodierung")
    print("=" * 50)
    
    try:
        lat = float(input("Breitengrad (-90 bis 90): "))
        lon = float(input("Längengrad (-180 bis 180): "))
        precision = int(input("Präzision (1-12, empfohlen: 6-8): "))
        
        print(f"\n🎯 Koordinaten: {lat:.6f}°, {lon:.6f}°")
        print("=" * 70)
        
        # Alle drei Kodierungen mit vollständigen Infos
        encodings = [
            ("Base64", "base64", "📍"),
            ("Base16", "base16", "🔢"), 
            ("Custom", "custom", "🎲")
        ]
        
        for name, encoding, icon in encodings:
            gh = GeoHash(encoding)
            geohash = gh.encode(lat, lon, precision)
            decoded_lat, decoded_lon, lat_err, lon_err = gh.decode(geohash)
            
            print(f"\n{icon} GeoHash ({name}): '{geohash}'")
            print(f"🔍 Dekodiert:")
            print(f"   Koordinaten: {decoded_lat:.6f}°, {decoded_lon:.6f}°")
            print(f"   Fehlerbereich: ±{lat_err:.6f}°")
        
    except ValueError as e:
        print(f"❌ Fehler: {e}")
    except Exception as e:
        print(f"❌ Unerwarteter Fehler: {e}")
    
    input("\nDrücken Sie Enter zum Fortfahren...")

# Nachbarn demonstrieren
def neighbors_demo():
    print("\n" + "=" * 50)
    print("🗺️ Nachbar-GeoHashes finden")
    print("=" * 50)
    
    try:
        geohash = input("GeoHash eingeben: ").strip()
        
        # Kodierungs-Auswahl mit Validierung
        while True:
            print("\nWelche Kodierung soll verwendet werden?")
            print("1. Base64 (Standard)")
            print("2. Base16") 
            print("3. Custom")
            
            encoding_choice = input("Ihre Wahl (1-3, Enter für Base64): ").strip()
            
            # Kodierung bestimmen
            if encoding_choice == "1":
                encoding = "base64"
                encoding_name = "Base64"
                break
            elif encoding_choice == "2":
                encoding = "base16"
                encoding_name = "Base16"
                break
            elif encoding_choice == "3":
                encoding = "custom"
                encoding_name = "Custom"
                break
            else:
                print("❌ Ungültige Eingabe! Bitte wählen Sie 1-3 oder Enter für Standard.")
                print()
        
        try:
            gh = GeoHash(encoding)
            neighbors = gh.get_neighbors(geohash)
            
            print(f"\n🎯 Nachbarn von '{geohash}' ({encoding_name}):")
            print()
            
            # Rasteranzeige
            directions = [
                ("northwest", "north", "northeast"),
                ("west", "CENTER", "east"),
                ("southwest", "south", "southeast")
            ]
            
            for row in directions:
                for direction in row:
                    if direction == "CENTER":
                        print(f"{geohash:^12s}", end=" ")
                    else:
                        neighbor = neighbors.get(direction, "ERROR")
                        print(f"{neighbor:^12s}", end=" ")
                print()
            
            print(f"\n📋 Nachbarliste ({encoding_name}):")
            for direction in ["north", "south", "east", "west", "northeast", "northwest", "southeast", "southwest"]:
                print(f"   {direction:10s}: {neighbors[direction]}")
                
        except Exception as e:
            print(f"❌ Fehler bei Nachbar-Berechnung mit {encoding_name}: {e}")
            print("💡 Tipp: Versuchen Sie eine andere Kodierung oder prüfen Sie den GeoHash.")
            
    except Exception as e:
        print(f"❌ Fehler: {e}")
    
    input("\nDrücken Sie Enter zum Fortfahren...")


# Restaurant-Suche Demonstration
def run_restaurant_demo():
    clear_screen()
    print("🍕 Starte Restaurant-Suche Demonstration...")
    print()
    restaurant_search_example()
    print()
    input("Drücken Sie Enter um zum Hauptmenü zurückzukehren...")


# Unit-Tests ausführen
def run_unit_tests():
    clear_screen()
    print("🧾 Starte Unit-Tests...")
    print()
    
    try:
        success = run_tests()
        print()
        if success:
            print("✅ Alle Tests erfolgreich bestanden!")
        else:
            print("❌ Einige Tests sind fehlgeschlagen!")
    except Exception as e:
        print(f"❌ Fehler beim Ausführen der Tests: {e}")
    
    print()
    input("Drücken Sie Enter um zum Hauptmenü zurückzukehren...")

# Hauptprogramm mit Menüschleife
def main():
    while True:
        show_main_menu()
        
        choice = input("Ihre Wahl: ").strip()
        
        if choice == "1":
            geohash_demonstrator()
        elif choice == "2":
            run_restaurant_demo()
        elif choice == "3":
            run_unit_tests()
        elif choice == "0":
            clear_screen()
            print("👋 Auf Wiedersehen!")
            print("Danke für die Nutzung des GeoHash-Algorithmus!")
            return False
        else:
            print()
            print("❌ Ungültige Eingabe! Bitte wählen Sie 0-3.")
            input("\nDrücken Sie Enter zum Fortfahren...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Programm durch Benutzer beendet.")
    except Exception as e:
        print(f"\n❌ Unerwarteter Fehler: {e}")
        sys.exit(1)