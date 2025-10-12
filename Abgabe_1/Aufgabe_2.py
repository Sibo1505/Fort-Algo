from Aufgabe_1 import h1, h2
from math import ceil, log

class BloomFilter:
    def __init__(self, n, p, k=2):
        self.n = n  # Anzahl der Daten
        self.p = p  # Fehlerwahrscheinlichkeit
        self.k = k  # Anzahl der Hash-Funktionen

        # Berechnung der Bitanzahl (m) für festes k
        self.m = ceil(-self.k * self.n / log(1 - self.p**(1/self.k)))

        # Initialisiere das Bit-Array
        self.bit_array = [0] * self.m

    # Fügt ein Element in den Bloom-Filter ein
    def insert(self, element):
        h1_val = h1(str(element)) % self.m
        h2_val = h2(str(element)) % self.m

        # Setze die Bits an den berechneten Positionen
        self.bit_array[h1_val] = 1
        self.bit_array[h2_val] = 1

    # Überprüft, ob ein Element möglicherweise im Bloom-Filter enthalten ist
    def search(self, element):
        h1_val = h1(str(element)) % self.m
        h2_val = h2(str(element)) % self.m

        # Überprüfe, ob die Bits an den berechneten Positionen gesetzt sind
        return self.bit_array[h1_val] == 1 and self.bit_array[h2_val] == 1

    # Gibt die Parameter des Bloom-Filters zurück
    def getParameters(self):
        return self.n, self.p, self.k, self.m