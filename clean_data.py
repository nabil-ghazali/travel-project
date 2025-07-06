"""
 Charge un fichier CSV, nettoie les données et sauvegarde un nouveau fichier propre.

    Paramètres :
    - filename (str) : chemin du fichier d'entrée (CSV brut)
    - new_filename (str) : nom du fichier de sortie (CSV nettoyé)

    Étapes :
    1. Chargement du fichier original
    2. Gestion des valeurs manquantes
    3. Détection et correction des valeurs aberrantes
    4. Sauvegarde du nouveau fichier nettoyé

"""

# Import des librairies
import pandas as pd

def load_and_clean_data(filename, new_filename):
    # - Charger le fichier CSV  
    df_original = pd.read_csv(filename)

    # Je fais une copie de mon fichier afin de garder l'original pour comoparaison
    df = df_original.copy()
    # print(df)

    # - Traitement des valeurs manquantes, remplacement des valeurs NaN par 'unknown' et modification du fichier avec 'Inplace = True'
    df.fillna(value = 'unknown', inplace=True)
    # print(df1)
    # J'ai choisi fillna afin de modifier seulement les valeurs manquantes ici la météo, sachant que les ces valeurs peuvent être n'étant pas très importantes parce qu'on pas de données sur la météo déja et supprimer la ligne ferait qu'on passerrai à côté de données plus importatntes

    # - Détecter et traiter les valeurs aberrantes, justifier les choix faits
    print(df[df['photos'] < 0] )
    # Sur les données du fichier je vois qu'il des photos prises à -15, je mets la valeur à 0

    # df.loc[(df['city'] == 'Grenoble') & (df['date'] == '2024-12-10'), 'photos'] = 0 #cette fonction permet de localiser la ligne et la mettre à zéro
    df['photos'] = df['photos'].clip(lower=0) #Met à 0 les photos avec des valeurs inférieures à 0
    print(df)
    # Mon data frame (copy) est propre et prêt à l'analyse
    df.to_csv(new_filename, index=False)
    return df
# load_and_clean_data("travel_data.csv","sorted_travel_data.csv")