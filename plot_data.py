import plotly.express as px
import pandas as pd
import plotly.io as pio
import os

# Forcer l'ouverture du navigatreur
pio.renderers.default = 'browser'


def plot_photos_by_weather(df):

    # Calcul du nombre moyen de photos par météo
    moyenne_photos = df.groupby('weather')['photos'].mean().reset_index()

    # Création du graphique en barres
    fig = px.bar(
        moyenne_photos,
        x='weather',
        y='photos',
        color='weather',
        title='Nombre moyen de photos prises selon la météo',
        labels={'weather': 'Météo', 'photos': 'Nombre moyen de photos'},
        text_auto='.2s'  # Affiche la valeur moyenne au-dessus des barres
    )

    fig.write_html("graph.html", auto_open=False)
    os.system('powershell.exe start graph.html')


def plot_mood_distribution(df):

    fig = px.pie(
        df,
        names='mood',
        title='Répartition des humeurs dans les données',
        hole=0.2,  # Trou du donut
    )
    fig.update_traces(textinfo='percent+label')  # Affiche % et le nom de l’humeur
    fig.write_html("graph.html", auto_open=False)
    os.system('powershell.exe start graph.html')


def plot_photos_by_date(df):

    # on trie par date
    df_sorted = df.sort_values(by='date')  
    fig = px.line(
        df_sorted,
        x='date',
        y='photos',
        color='city',
        markers=True, #cela affiche des points visibles
        title='Évolution du nombre de photos prises au fil du temps',
        labels={'date': 'Date', 'photos': 'Nombre de photos'}
    )
    fig.write_html("graph.html", auto_open=False)
    os.system('powershell.exe start graph.html')


# Test fonction
# plot_photos_by_weather("sorted_travel_data.csv")
# plot_mood_distribution("sorted_travel_data.csv")
# plot_photos_by_date("sorted_travel_data.csv")