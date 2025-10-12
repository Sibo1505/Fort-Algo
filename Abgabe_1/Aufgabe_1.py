''' Aufgabe 1: Hash-Funktion implementieren '''

def h1(obj):
    primes = [
        7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
        43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
        89, 97, 101, 103, 107, 109, 113, 127, 131, 137
    ]

    # Input Check
    if not obj:
        return 0

    # Choose a base from the prime list based on the first character
    base_index = sum(ord(c) for c in obj) % len(primes)
    base = primes[base_index]

    # Now mix it like in the classic polynomial hash
    hash_value = 0
    for char in obj:
        hash_value = hash_value * base + ord(char)

    # Bring the result into the range 0–99999
    return hash_value % 100000

def h2(obj):
    """Hashfunktion: wechselt nach jedem Buchstaben die Primzahl."""
    if not obj:
        return 0

    primes = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
              43, 47, 53, 59, 61, 67, 71, 73, 79, 83]

    hash_value = 0
    for i, char in enumerate(obj):
        c = ord(char)
        left_shift = c << (i % 5)
        right_shift = c >> (i % 3)
        prime = primes[i % len(primes)]  # wechsle Primzahl bei jedem Buchstaben
        hash_value ^= (left_shift ^ right_shift)
        hash_value *= prime
        hash_value &= 0xFFFFFFFF

    return hash_value % 100000
