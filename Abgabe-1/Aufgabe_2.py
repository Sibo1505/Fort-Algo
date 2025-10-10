from Aufgabe_1 import h1, h2
from math import ceil, log


class BloomFilter:
    def __init__(self, n=10000, p=0.05, k=2):
        self.n = n  # Anzahl der Daten
        self.p = p  # Fehlerwahrscheinlichkeit
        self.k = k  # Anzahl der Hash-Funktionen

        # Berechnung der Bitanzahl (m) für festes k
        self.m = ceil(-self.k * self.n / log(1 - self.p**(1/self.k)))

        # Initialisiere das Bit-Array
        self.bit_array = [0] * self.m

    def insert(self, element):
        h1_val = h1(str(element)) % self.m
        h2_val = h2(str(element)) % self.m

        # Setze die Bits an den berechneten Positionen
        self.bit_array[h1_val] = 1
        self.bit_array[h2_val] = 1

    def search(self, element):
        h1_val = h1(str(element)) % self.m
        h2_val = h2(str(element)) % self.m

        # Überprüfe, ob die Bits an den berechneten Positionen gesetzt sind
        return self.bit_array[h1_val] == 1 and self.bit_array[h2_val] == 1

    def getParameters(self):
        return self.n, self.p, self.k, self.m

bloom_filter = BloomFilter()
print(bloom_filter.getParameters())

bloom_filter.insert("Hallo")
print(bloom_filter.search("Hallo"))  # Sollte True zurückgeben
print(bloom_filter.search("Welt"))  # Sollte False zurückgeben