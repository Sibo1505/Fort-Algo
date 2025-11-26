import unittest
from geohash import GeoHash


class TestGeoHash(unittest.TestCase):
    
    # Dieser Test prüft die Kodierung für alle unterstützten Kodierungsschemata
    def test_encode_all_encodings(self):
        test_cases = [
            ("base16", 12, "BASE16_CHARS"),
            ("base64", 10, "BASE64_CHARS"),
            ("custom", 8, "CUSTOM_CHARS"),
        ]
        
        for encoding, precision, chars_attr in test_cases:
            with self.subTest(encoding=encoding):
                gh = GeoHash(encoding)
                result = gh.encode(52.5200, 13.4050, precision)
                
                # Prüfe Typ und Länge
                self.assertIsInstance(result, str)
                self.assertEqual(len(result), precision)
                
                # Prüfe gültige Zeichen
                valid_chars = getattr(gh, chars_attr)
                for char in result:
                    self.assertIn(char, valid_chars)
    
    # Tester für ungültiges Kodierungsschema
    def test_invalid_encoding(self):
        with self.assertRaises(ValueError):
            GeoHash("invalid_encoding")
    
    # Tester für ungültige Breitengrade (latitude)
    def test_invalid_latitude(self):
        gh = GeoHash("base64")
        with self.assertRaises(ValueError):
            gh.encode(100, 0)  # Zu groß
        with self.assertRaises(ValueError):
            gh.encode(-100, 0)  # Zu klein
    
    # Tester für ungültige Längengrade (longitude)
    def test_invalid_longitude(self):
        gh = GeoHash("base64")
        with self.assertRaises(ValueError):
            gh.encode(0, 200)  # Zu groß
        with self.assertRaises(ValueError):
            gh.encode(0, -200)  # Zu klein
    
    # Tester für Kodierung und Dekodierung
    def test_encode_decode_roundtrip(self):
        gh = GeoHash("base64")
        lat, lon = 52.5200, 13.4050
        precision = 12
        
        geohash = gh.encode(lat, lon, precision)
        decoded_lat, decoded_lon, lat_err, lon_err = gh.decode(geohash)
        
        # Prüfe, ob die dekodierten Werte im Fehlerbereich liegen
        self.assertAlmostEqual(decoded_lat, lat, delta=lat_err * 2)
        self.assertAlmostEqual(decoded_lon, lon, delta=lon_err * 2)
    
    # Tester für Berechnung von Nachbarn
    def test_neighbors(self):
        gh = GeoHash("base64")
        geohash = gh.encode(52.5200, 13.4050, 8)
        neighbors = gh.get_neighbors(geohash)
        
        # Prüfe, dass alle 8 Nachbarn vorhanden sind
        expected_directions = ['north', 'south', 'east', 'west', 
                              'northeast', 'northwest', 'southeast', 'southwest']
        for direction in expected_directions:
            self.assertIn(direction, neighbors)
            self.assertIsInstance(neighbors[direction], str)
            self.assertEqual(len(neighbors[direction]), 8)
    
    # Tester für gleiche Standorte
    def test_same_location_same_hash(self):
        gh = GeoHash("base64")
        hash1 = gh.encode(52.5200, 13.4050, 10)
        hash2 = gh.encode(52.5200, 13.4050, 10)
        self.assertEqual(hash1, hash2)
    
    # Tester für unterschiedliche Standorte
    def test_different_locations_different_hashes(self):
        gh = GeoHash("base64")
        hash1 = gh.encode(52.5200, 13.4050, 10)
        hash2 = gh.encode(48.1351, 11.5820, 10)
        self.assertNotEqual(hash1, hash2)
    
    # Tester für Grenzfälle
    def test_edge_cases(self):
        gh = GeoHash("base64")
        
        # Nordpol
        north_pole = gh.encode(90, 0, 8)
        self.assertEqual(len(north_pole), 8)
        
        # Südpol
        south_pole = gh.encode(-90, 0, 8)
        self.assertEqual(len(south_pole), 8)
        
        # Nullinsel (0, 0)
        null_island = gh.encode(0, 0, 8)
        self.assertEqual(len(null_island), 8)
        
        # Datumsgrenze
        dateline = gh.encode(0, 180, 8)
        self.assertEqual(len(dateline), 8)


# Hier werden die Tests ausgeführt
def run_tests():
    print("=" * 70)
    print("GeoHash Unit Tests")
    print("=" * 70)
    print()
    
    # Erstelle Test Suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestGeoHash)
    
    # Führe Tests aus
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Zusammenfassung
    print("\n" + "=" * 70)
    print("Zusammenfassung:")
    print(f"  Tests gesamt: {result.testsRun}")
    print(f"  Erfolgreich:  {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"  Fehlgeschlagen: {len(result.failures)}")
    print(f"  Fehler:       {len(result.errors)}")
    print("=" * 70)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    run_tests()
