
import pandas as pd
import os
import kagglehub

def load_language_data():
    """Lädt alle Sprachdateien und gibt ein Dictionary mit den Wörtern zurück."""
    # Lade den Datensatz von Kaggle
    path = kagglehub.dataset_download("jacekpardyak/languages-of-europe")
    print("Datensatzpfad:", path)

    # Lade die languages.csv als Index
    languages_df = pd.read_csv(os.path.join(path, "languages.csv"))
    
    # Dictionary für alle Wörter
    all_words = {}

    # Iteriere über alle Sprachen
    for _, row in languages_df.iterrows():
        language = row['language']
        code = row['code']
        encoding = row['encoding']
        
        file_name = f"{code}.csv"
        try:
            # Lade die Sprachdatei mit der korrekten Kodierung
            df = pd.read_csv(os.path.join(path, file_name), encoding=encoding.lower())
            # Extrahiere die Wörter (erste Spalte) und konvertiere zu Liste
            words = df.iloc[:, 0].astype(str).tolist()
            # Speichere die Wörter im Dictionary mit Sprache als Schlüssel
            all_words[language] = words
            # print(f"Erfolgreich geladen: {language} ({len(words)} Wörter)")
        except Exception as e:
            print(f"Fehler beim Laden von {language}: {e}")

    return all_words

def get_words_for_language(all_words, language):
    """Gibt die Wörter für eine bestimmte Sprache zurück."""
    return all_words.get(language, [])

def get_available_languages(all_words):
    """Gibt eine Liste aller verfügbaren Sprachen zurück."""
    return list(all_words.keys())

def get_all_words(all_words):
    """Gibt eine Liste aller Wörter aus allen Sprachen zurück."""
    all_word_list = []
    for words in all_words.values():
        all_word_list.extend(words)
    return all_word_list


if __name__ == "__main__":
    # Lade alle Sprachdaten
    word_database = load_language_data()
    
    # Zeige verfügbare Sprachen
    languages = get_available_languages(word_database)
    print("\nVerfügbare Sprachen:", languages)
    
    # Lade alle Wörter
    all_words = get_all_words(word_database)
    print(f"\nGesamtanzahl der Wörter über alle Sprachen: {len(all_words)}") 