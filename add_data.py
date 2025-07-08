import pandas as pd
from datetime import datetime

def add_data():
    all_trips = []

    while True:
        data = {}

        city = input("What is the city you traveled to: ").strip()
        while not city:
            print("❌ La ville ne peut pas être vide.")
            city = input("What is the city you traveled to: ").strip()
        data["city"] = city

        while True:
            date_input = input("When was the date of this trip (format: YYYY/MM/DD): ").strip()
            try:
                datetime.strptime(date_input, "%Y/%m/%d")
                break
            except ValueError:
                print("❌ Format incorrect. Exemple : 2025/07/04")
        data["date"] = date_input

        weather = input("What was the weather like during this trip: ").strip()
        while not weather:
            print("❌ Le champ météo ne peut pas être vide.")
            weather = input("What was the weather like during this trip: ").strip()
        data["weather"] = weather

        mood = input("What was your mood during this trip: ").strip()
        while not mood:
            print("❌ Le champ humeur ne peut pas être vide.")
            mood = input("What was your mood during this trip: ").strip()
        data["mood"] = mood

        while True:
            photos = input("How many photos did you take during your trip: ").strip()
            if photos.isdigit():
                data["photos"] = int(photos)
                break
            else:
                print("❌ Entre un nombre entier (ex: 3, 12...)")

        all_trips.append(data)

        again = input("\nSouhaitez-vous ajouter un autre voyage ? (oui/non) : ").strip().lower()
        if again not in ["oui", "o", "yes", "y"]:
            print("\n✅ Fin de l’ajout des voyages.\n")
            break

    # À la fin : demander le nom du fichier à générer
    while True:
        name_data_frame = input("Nom du fichier CSV final (sans extension) : ").strip()
        if name_data_frame:
            break
        else:
            print("❌ Le nom du fichier ne peut pas être vide.")

    filename = f"{name_data_frame}.csv"
    df = pd.DataFrame(all_trips)
    df.to_csv(filename, index=False)
    print(f"✅ Données enregistrées dans le fichier : {filename}\n")

    return filename
