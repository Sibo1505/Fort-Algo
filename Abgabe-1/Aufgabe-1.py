import pandas as pd
import os
import kagglehub
from hash_functions_menu import set_words, main

''' Kaggle-Setup API '''
# Load the dataset from Kaggle
path = kagglehub.dataset_download("jacekpardyak/languages-of-europe")
print("Datensatzpfad:", path)

# Shows the files in the dataset directory
print(os.listdir(path))

# Load the German word list
df = pd.read_csv(os.path.join(path, "de_De.csv"), encoding="latin1")

# Extract the list of words from the DataFrame (assuming the column is named 'word')
words = df.iloc[:, 0].astype(str).tolist()

# Setze die Wortliste für das Menü
set_words(words)

# Starte das Hauptprogramm
if __name__ == "__main__":
    main()