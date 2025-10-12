
import pandas as pd
import os
import kagglehub

# Lade alle Sprachdateien und speichere die Wörter in einem Dictionary
def load_language_data():

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

# Gibt die Wörter für eine bestimmte Sprache zurück.
def get_words_for_language(all_words, language):
    return all_words.get(language, [])

# Gibt eine Liste aller verfügbaren Sprachen zurück.
def get_available_languages(all_words):
    return list(all_words.keys())

# Gibt eine Liste aller Wörter aus allen Sprachen zurück.
def get_all_words(all_words):
    all_word_list = []
    for words in all_words.values():
        all_word_list.extend(words)
    return all_word_list