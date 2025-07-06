import pandas as pd

def print_statistics(df) : 

    # - Afficher la distribution des valeurs météo et humeur
    print(f"Affichage des valeurs 'weather' et 'mood' \n {df[['weather', 'mood']]}")

    # - Afficher des statistiques descriptives sur la colonne `photos` (moyenne, médiane, min, max) 
    print_average_photos = df['photos'].mean()
    print(f"La moyenne de photos prise est de {print_average_photos}")
    print_min_photos = df['photos'].min()
    print(f"Le minimum de photos pris est de {print_min_photos}")
    print_max_photos = df['photos'].max()
    print(f"Le maximum de photos pris est de {print_max_photos}")

    # - Afficher le nombre de valeurs manquantes et aberrantes détectées
    print_valeurs_manquantes=df.isnull().sum()
    print(f"Affichage des valeurs manquantes: \n {print_valeurs_manquantes}")

    # - Afficher les valeurs aberrantes détectées
    valeurs_aberrantes = df[(df['photos'] < 0)]
    print(f"Affichage valeurs aberrantes : \n {valeurs_aberrantes}")


# print_statistics("clean_travel_data.csv")