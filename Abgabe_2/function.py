import os

# Lade Artikel aus Datei und berechne SimHash-Fingerprints
def load_articles(path):
    articles = {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                parts = line.strip().split(" ", 1)
                if len(parts) == 2:
                    art_id, text = parts
                    articles[art_id] = simhash(text)
    except FileNotFoundError:
        print(f"Datei nicht gefunden: {os.path.abspath(path)}")
        return {}
    return articles

# SimHash berechnen (64 Bit), um Ähnlichkeiten zu erkennen
def simhash(text):
    shingles = get_shingles(text)
    bit_counts = [0] * 64

    # Zähle Bits für jedes Shingle
    for shingle in shingles:
        h = simple_hash(shingle)
        for i in range(64):
            if (h >> i) & 1:
                bit_counts[i] += 1
            else:
                bit_counts[i] -= 1

    # Erstelle den SimHash-Fingerprint
    fingerprint = 0
    for i in range(64):
        if bit_counts[i] > 0:
            fingerprint |= 1 << i
    return fingerprint

# Erstellt Shingles (3-Wort-Kombinationen)
def get_shingles(text, size=3):
    words = text.lower().split()
    return [' '.join(words[i:i+size]) for i in range(len(words) - size + 1)]

# einfache Hashfunktion für Shingles
def simple_hash(shingle):
    # einfache deterministische Hashfunktion (64 Bit)
    h = 0
    for c in shingle:
        h = (h * 31 + ord(c)) % (1 << 64)
    return h


# Hamming-Distanz zwischen zwei SimHash-Fingerprints
def hamming_distance(x, y):
    return bin(x ^ y).count("1")

# Prozentuale Ähnlichkeit basierend auf Hamming-Distanz
def similarity(x, y):
    # Prozentuale Ähnlichkeit (100 % = identisch)
    dist = hamming_distance(x, y)
    return 100 - (dist / 64 * 100)