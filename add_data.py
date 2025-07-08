import pandas as pd
from datetime import datetime
import os

def add_data():

    while True:
        data_frame = {}

        city = input("What is the city you traveled to: ").strip()
        while not city:
            print("❌ La ville ne peut pas être vide.")
            city = input("What is the city you traveled to: ").strip()
        data_frame["city"] = city

        while True:
            date_input = input("When was the date of this trip (format: YYYY/MM/DD): ").strip()
            try:
                datetime.strptime(date_input, "%Y/%m/%d")
                break
            except ValueError:
                print("❌ Format incorrect. Exemple : 2025/07/04")
        data_frame["date"] = date_input

        weather = input("What was the weather like during this trip: ").strip()
        while not weather:
            print("❌ Le champ météo ne peut pas être vide.")
            weather = input("What was the weather like during this trip: ").strip()
        data_frame["weather"] = weather

        mood = input("What was your mood during this trip: ").strip()
        while not mood:
            print("❌ Le champ humeur ne peut pas être vide.")
            mood = input("What was your mood during this trip: ").strip()
        data_frame["mood"] = mood

        while True:
            photos = input("How many photos did you take during your trip: ").strip()
            if photos.isdigit():
                data_frame["photos"] = int(photos)
                break
            else:
                print("❌ Entre un nombre entier (ex: 3, 12...)")

        df = pd.DataFrame([data_frame])

        while True:
            name_data_frame = input("Nom du fichier CSV (sans extension) : ").strip()
            if name_data_frame:
                break
            else:
                print("❌ Le nom du fichier ne peut pas être vide.")

        new_data_frame_csv = f"{name_data_frame}.csv"

        if os.path.exists(new_data_frame_csv):
            df.to_csv(new_data_frame_csv, mode='a', header=False, index=False)
            print(f"✅ Données ajoutées à {new_data_frame_csv}")
        else:
            df.to_csv(new_data_frame_csv, index=False)
            print(f"✅ Nouveau fichier créé : {new_data_frame_csv}")
            return new_data_frame_csv
        
  