#   - Importe et utilise les fonctions des modules précédents  
from clean_data import load_and_clean_data
from print_stat import print_statistics
from plot_data import (
    plot_photos_by_weather,
    plot_mood_distribution,
    plot_photos_by_date,
)

"""
main.py

 Script principal qui :  
  - Importe et utilise les fonctions des modules précédents  
  - Charge et nettoie les données  
  - Affiche les statistiques  
  - Produit les graphiques  
  - Permet une exécution simple et claire du projet
"""


def main() -> None:

    # Charger, nettoyer les données et exporter un nouveau fichier 
    df_clean = load_and_clean_data("travel_data.csv","cleaned_data")

    # Afficher statistiques dans la console
    print_statistics(df_clean)

    # Générer et afficher les graphiques interactifs
    plot_mood_distribution(df_clean)
    plot_photos_by_weather(df_clean)
    plot_photos_by_date(df_clean)


if __name__ == "__main__":
    main()
