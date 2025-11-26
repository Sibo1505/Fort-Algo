from geohash import GeoHash

# Praktisches Beispiel: Restaurant-Suche mit GeoHash-Nachbarn
# HAW Kiel Umgebung - "Was gibt es in der Nähe zu essen?"
def restaurant_search_example():
    print("=" * 80)
    print("Restaurant-Suche mit GeoHash-Nachbarn")
    print("=" * 80)
    
    # Standorte rund um die HAW Kiel
    locations = {
        "HAW Kiel": (54.33265481857568, 10.180353587098494),
        "American Diner": (54.33260164465626, 10.181013410494288),
        "HAW Kiel Bunker-D": (54.33277280869422, 10.179356391431096),
        "Bistro Max Planck": (54.33077315356874, 10.18197198341049),
        "Yummy Pizza House": (54.331379743752855, 10.182136562354621),
        "YUM SLICE GmbH": (54.33317471757841, 10.1764979756617)
    }
    
    gh = GeoHash("base64")
    
    # 1. Berechne GeoHashes für alle Standorte
    print("\n1. GeoHash-Kodierung aller Standorte:")
    print("-" * 50)
    
    location_hashes = {}
    for name, (lat, lon) in locations.items():
        # Präzision 6 = ca. 610m x 1220m Genauigkeit (für Nachbarschafts-Suche)
        geohash = gh.encode(lat, lon, 6)
        location_hashes[name] = geohash
        print(f"{name:20s}: {geohash}")
    
    # 2. HAW Kiel als Ausgangspunkt - finde Nachbarzellen
    haw_kiel_hash = location_hashes["HAW Kiel"]
    neighbors = gh.get_neighbors(haw_kiel_hash)
    
    print(f"\n2. Nachbarzellen von HAW Kiel ({haw_kiel_hash}):")
    print("-" * 50)
    for direction, neighbor_hash in neighbors.items():
        print(f"{direction:12s}: {neighbor_hash}")
    
    # 3. Prüfe welche Restaurants in Nachbarzellen liegen
    print(f"\n3. Restaurant-Analyse:")
    print("-" * 50)
    
    # Sammle alle relevanten Zellen (HAW Kiel + Nachbarn)
    search_area = {haw_kiel_hash}  # Zentrale Zelle
    search_area.update(neighbors.values())  # Alle Nachbarzellen
    
    print(f"Suchbereich: {len(search_area)} GeoHash-Zellen")
    print(f"   Zentrum: {haw_kiel_hash}")
    print(f"   + {len(neighbors)} Nachbarzellen\n")
    
    # Prüfe jeden Restaurant-Standort
    restaurants_in_area = []
    restaurants_outside = []
    
    for name, geohash in location_hashes.items():
        if name == "HAW Kiel":
            continue  # Ausgangspunkt überspringen
            
        if geohash in search_area:
            restaurants_in_area.append(name)
            print(f"✅ {name:25s} → IN Suchbereich ({geohash})")
        else:
            restaurants_outside.append(name)
            print(f"❌ {name:25s} → AUßERHALB ({geohash})")
    
    # 4. Zusammenfassung
    print(f"\n4. Ergebnis der lokalen Suche:")
    print("-" * 50)
    print(f"Restaurants in der NÄHE: {len(restaurants_in_area)}")
    for restaurant in restaurants_in_area:
        print(f"   • {restaurant}")
    
    print(f"\n Restaurants etwas WEITER weg: {len(restaurants_outside)}")
    for restaurant in restaurants_outside:
        print(f"   • {restaurant}")

if __name__ == "__main__":
    restaurant_search_example()