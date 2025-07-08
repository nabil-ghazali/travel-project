#   - Importe et utilise les fonctions des modules précédents  
from clean_data import load_and_clean_data
from print_stat import print_statistics
from plot_data import (
    plot_photos_by_weather,
    plot_mood_distribution,
    plot_photos_by_date,
)
from add_data import add_data
"""
main.py

 Script principal qui :  
  - Importe et utilise les fonctions des modules précédents  
  - Ajoute des données et les traduit en fichier.csv
  - Charge et nettoie les données  
  - Affiche les statistiques  
  - Produit les graphiques  
  - Permet une exécution simple et claire du projet
"""


def main() -> None:

    # Ajouter des données
    new_trip = add_data()

    # Charger, nettoyer les données et exporter un nouveau fichier 
    df_clean = load_and_clean_data(new_trip,"cleaned_data")

    # Afficher statistiques dans la console
    print_statistics(df_clean)

    # Générer et afficher les graphiques interactifs
    plot_mood_distribution(df_clean)
    plot_photos_by_weather(df_clean)
    plot_photos_by_date(df_clean)


if __name__ == "__main__":
    
    start = input("Souhaitez-vous ajouter un voyage ? (oui/non) : ").strip().lower()
    if start in ["oui", "o", "yes", "y"]:
        main() 
    else:
        print("👋 Aucun ajout effectué. Fin du programme.")