class GeoHash:

    BASE16_CHARS = "0123456789ABCDEF"
    BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    CUSTOM_CHARS = "0123456789abcdefghjkmnpqrstuvwxyz"  # Ähnlich Base32, aber ohne i, l, o
    
    def __init__(self, encoding="base64"):

        self.encoding = encoding.lower()
        
        if self.encoding == "base16":
            self.chars = self.BASE16_CHARS
            self.bits_per_char = 4
        elif self.encoding == "base64":
            self.chars = self.BASE64_CHARS
            self.bits_per_char = 6
        elif self.encoding == "custom":
            self.chars = self.CUSTOM_CHARS
            self.bits_per_char = 5
        else:
            raise ValueError("Ungültiges Kodierungsschema. Verwenden Sie 'base16', 'base64' oder 'custom'")
    
    def encode(self, latitude, longitude, precision=12):

        if not -90 <= latitude <= 90:
            raise ValueError("Breitengrad muss zwischen -90 und 90 liegen")
        if not -180 <= longitude <= 180:
            raise ValueError("Längengrad muss zwischen -180 und 180 liegen")
        
        # Berechne benötigte Anzahl an Bits
        total_bits = precision * self.bits_per_char
        
        # Konvertiere Koordinaten in Binärstring
        lat_range = [-90.0, 90.0]
        lon_range = [-180.0, 180.0]
        
        bits = []
        is_longitude = True  # Wir beginnen mit Längengrad
        
        for i in range(total_bits):
            if is_longitude:
                mid = (lon_range[0] + lon_range[1]) / 2
                if longitude >= mid:
                    bits.append('1')
                    lon_range[0] = mid
                else:
                    bits.append('0')
                    lon_range[1] = mid
            else:
                mid = (lat_range[0] + lat_range[1]) / 2
                if latitude >= mid:
                    bits.append('1')
                    lat_range[0] = mid
                else:
                    bits.append('0')
                    lat_range[1] = mid
            
            is_longitude = not is_longitude
        
        # Konvertiere Bits in Zeichen
        geohash = ""
        bit_string = ''.join(bits)
        
        for i in range(0, len(bit_string), self.bits_per_char):
            chunk = bit_string[i:i + self.bits_per_char]
            # Falls letzter Chunk unvollständig, mit Nullen auffüllen
            if len(chunk) < self.bits_per_char:
                chunk = chunk.ljust(self.bits_per_char, '0')
            
            # Konvertiere Binär zu Dezimal und dann zum entsprechenden Zeichen
            index = int(chunk, 2)
            geohash += self.chars[index]
        
        return geohash
    
    def decode(self, geohash):

        bits = ""
        for char in geohash:
            if char not in self.chars:
                raise ValueError(f"Ungültiges Zeichen '{char}' im GeoHash")
            
            index = self.chars.index(char)
            # Konvertiere Index zu Binär mit entsprechender Länge
            bits += format(index, f'0{self.bits_per_char}b')
        
        # Dekodiere Bits zurück zu Koordinaten
        lat_range = [-90.0, 90.0]
        lon_range = [-180.0, 180.0]
        
        is_longitude = True
        
        for bit in bits:
            if is_longitude:
                mid = (lon_range[0] + lon_range[1]) / 2
                if bit == '1':
                    lon_range[0] = mid
                else:
                    lon_range[1] = mid
            else:
                mid = (lat_range[0] + lat_range[1]) / 2
                if bit == '1':
                    lat_range[0] = mid
                else:
                    lat_range[1] = mid
            
            is_longitude = not is_longitude
        
        latitude = (lat_range[0] + lat_range[1]) / 2
        longitude = (lon_range[0] + lon_range[1]) / 2
        lat_error = (lat_range[1] - lat_range[0]) / 2
        lon_error = (lon_range[1] - lon_range[0]) / 2
        
        return latitude, longitude, lat_error, lon_error
    
    def get_neighbors(self, geohash):

        lat, lon, lat_err, lon_err = self.decode(geohash)
        
        neighbors = {
            'north': self.encode(lat + 2 * lat_err, lon, len(geohash)),
            'south': self.encode(lat - 2 * lat_err, lon, len(geohash)),
            'east': self.encode(lat, lon + 2 * lon_err, len(geohash)),
            'west': self.encode(lat, lon - 2 * lon_err, len(geohash)),
            'northeast': self.encode(lat + 2 * lat_err, lon + 2 * lon_err, len(geohash)),
            'northwest': self.encode(lat + 2 * lat_err, lon - 2 * lon_err, len(geohash)),
            'southeast': self.encode(lat - 2 * lat_err, lon + 2 * lon_err, len(geohash)),
            'southwest': self.encode(lat - 2 * lat_err, lon - 2 * lon_err, len(geohash)),
        }
        
        return neighbors


def main():
    """
    Demonstriert die Verwendung des GeoHash-Algorithmus
    """
    print("=" * 70)
    print("GeoHash-Algorithmus Demonstration")
    print("=" * 70)
    
    # Beispielkoordinaten
    test_locations = [
        ("Berlin, Deutschland", 52.5200, 13.4050),
        ("Hamburg, Deutschland", 53.5511, 9.9937),
        ("München, Deutschland", 48.1351, 11.5820),
        ("London, UK", 51.5074, -0.1278),
        ("New York, USA", 40.7128, -74.0060),
        ("Tokio, Japan", 35.6762, 139.6503),
    ]
    
    encodings = ["base16", "base64", "custom"]
    
    for encoding in encodings:
        print(f"\n{'=' * 70}")
        print(f"Kodierung: {encoding.upper()}")
        print(f"{'=' * 70}\n")
        
        gh = GeoHash(encoding)
        
        for location, lat, lon in test_locations:
            print(f"Standort: {location}")
            print(f"  Koordinaten: {lat:.4f}°, {lon:.4f}°")
            
            # Verschiedene Präzisionsstufen
            for precision in [6, 10]:
                geohash = gh.encode(lat, lon, precision)
                decoded_lat, decoded_lon, lat_err, lon_err = gh.decode(geohash)
                
                print(f"  Präzision {precision}: {geohash}")
                print(f"    Dekodiert: {decoded_lat:.6f}°, {decoded_lon:.6f}°")
                print(f"    Fehler: ±{lat_err:.6f}° (Breite), ±{lon_err:.6f}° (Länge)")
            
            print()
    
    # Demonstriere Nachbarn
    print(f"\n{'=' * 70}")
    print("Benachbarte GeoHash-Zellen (Base64, Berlin)")
    print(f"{'=' * 70}\n")
    
    gh = GeoHash("base64")
    berlin_hash = gh.encode(52.5200, 13.4050, 8)
    print(f"Berlin GeoHash: {berlin_hash}")
    
    neighbors = gh.get_neighbors(berlin_hash)
    print("\nNachbarn:")
    for direction, neighbor_hash in neighbors.items():
        print(f"  {direction:12s}: {neighbor_hash}")


if __name__ == "__main__":
    main()
