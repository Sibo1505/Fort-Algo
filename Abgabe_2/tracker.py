from function import load_articles, similarity
import os

# Hauptprogramm
def main():
    # Einfacher Pfad zur articles.txt im gleichen Verzeichnis
    script_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(script_dir, "articles.txt")
    
    print("SimHash Plagiat-Checker")
    print("=" * 40)
    
    articles = load_articles(path)
    if not articles:
        return

    print(f"Analysiere {len(articles)} Artikel...")
    
    # Alle Artikel vergleichen
    ids = list(articles.keys())
    plagiate_gefunden = 0
    
    # Geht alle möglichen Paare durch
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            sim = similarity(articles[ids[i]], articles[ids[j]])
            if sim >= 90:  # ab 90 % gilt als Plagiat
                print(f"{ids[i]} und {ids[j]} -> {sim:.2f}% Ähnlichkeit")
                plagiate_gefunden += 1
    
    print(f"\nErgebnis: {plagiate_gefunden} Plagiat-Paare gefunden.")
    

if __name__ == "__main__":
    main()