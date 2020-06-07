import matplotlib.pyplot as plt
import sqlite3

def graph_poids(participant):
    connection = sqlite3.connect("entrainements.db")
    cursor = connection.cursor()
    cursor.execute("SELECT date,poids,gras FROM training WHERE user_name = ?", [participant])
    date = []
    poids = []
    gras = []
    rows = cursor.fetchall()
    for row in rows:
        date.append(row[0])
        poids.append(row[1])
        gras.append(row[2])
    plt.clf()
    plt.title(f"Courbe de poids de {participant}")
    plt.plot(date,poids, "b:o",label="Poids")
    plt.plot(date,gras,"r:o",label="Taux de graisse")
    plt.xlabel("Date d'entrainement")
    plt.ylabel("Poids en Kgs")
    plt.legend()
    plt.show()
