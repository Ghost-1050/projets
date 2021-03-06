from modules import *
from Exos import *
from datetime import date
from GraphPoids import graph_poids
from Record_sql import record_base
from Stat import stat_poids
from Stat import stat_entrainement
from Stat import histo_part


today = date.today()
d1 = today.strftime("%d/%m/%Y")
print(f"Nous sommes le {d1}.")
print("___________              __        __")
print("\__    ___/___________  |__| ____ |__| ____    _____")
print("  |    |  \_  __ \__  \ |  |/    \|  |/    \  / ___ \ ")
print("  |    |   |  | \// __ \|  |   |  \  |   |  \/ /_/  >")
print("  |____|   |__|  /____  /__|___|  /__|___|  /\___  /")
print("                      \/        \/        \//_____/   by Ghost v2.5")
print("\n")

participant = input("Veuillez rentrer votre nom : ")
participant = participant.capitalize()
rec_poids = input("Souhaitez vous avoir un suivi de votre poids ? oui/non\n > ")
if rec_poids == "oui":
    poids = float(input("Veuillez rentrer votre poids avec 1 chiffre apres le . : "))
    gras = float(input("Veuillez rentrer votre taux de graisse avec 1 chiffre apres le . : "))
else:
    poids = 0
    gras = 0
    print("Vous pourrez changer d'avis au prochain entrainement")

def menu():
        while 1:
            choix_menu = int(input(f"\n- Faites votre choix {participant} - \n 1- Faire un entrainement\n "
                                  "2- Consulter mes statistiques \n"
                                  " 3- Consulter ma courbe de poids\n 4- Quitter \n> "))
            if choix_menu == 1:

                entrainement = int(input(f"\nQuel type d'entrainement souhaitez vous faire {participant} ?\n 1- Gainage"
                                         "\n 2- Cardio Renforcement musculaire\n"
                                         " 3- Renforcement musculaire \n 4- Challenge FBI 'AC/DC'\n"
                                         " 5- Travail Force à la poutre\n 6- Revenir au menu principal\n> "))

                if entrainement == 1:
                    print("Matériel : Vous avez besoin d'un tapis de sol.\n")
                    print("Choisissez le niveau d'intensité : \n")
                    level = int(input(f"1-Débutant: {choix_diff2(1)}\n2-Intermédiaire: {choix_diff2(2)}\n>"))
                    serie = int(input("Combien de serie(s) souhaitez-vous faire ? : 1,2,3...? : "))
                    print(f"\nBienvenue {participant} l'entrainement va commencer.\n")
                    tps_rope = 0
                    train = Training(nbre_serie=serie, tps_rope=tps_rope, level=level, participant=participant)
                    train.gain()
                    record_base(participant, d1, entrainement, serie, tps_rope, level, poids, gras)
                if entrainement == 2:
                    print("Matériel : Vous avez besoin d'un tapis de sol, d'une corde à sauter et d'une barre de traction.\n")
                    tps_rope = int(input("Choisissez le temps de corde à sauter en seconde : "))
                    print("Choisissez l'intensité : \n")
                    level = int(input(f"1-Débutant: {choix_diff(1)}\n2-Intermédiaire: {choix_diff(2)}"
                                      f"\n3-Confirmé: {choix_diff(3)}\n4-Expert: {choix_diff(4)}\n> "
                                      f""))
                    serie = int(input("Combien de serie(s) souhaitez-vous faire ? : 1,2,3...? : "))
                    train = Training(nbre_serie=serie, tps_rope=tps_rope, level=level, participant=participant)
                    train.cardio()
                    record_base(participant, d1, entrainement, serie, tps_rope, level, poids, gras)
                if entrainement == 3:
                    print("Matériel : Vous avez besoin d'un tapis de sol, d'une barre de traction et d'un tretix.\n")
                    tps_rope = int(input("Choisissez le temps de repos entre les exercices : "))
                    level = 0
                    serie = int(input("Combien de serie(s) souhaitez-vous faire ? : 1,2,3...? : "))
                    train = Training(nbre_serie=serie, tps_rope=tps_rope, level=level, participant=participant)
                    train.renfor()
                    record_base(participant, d1, entrainement, serie, tps_rope, level, poids, gras)
                if entrainement == 4:
                    print("L'entrainement commence en planche bras tendu, vous devez faire une pompe"
                          " à chaque fois que vous entendez le mot 'Thunder' ou 'Thunderstruck' pendant la chanson.\n")
                    serie = int(input("Combien de serie(s) souhaitez-vous faire ? : 1,2,3...? : "))
                    level = 0
                    tps_rope = 0
                    train = Training(nbre_serie=serie, tps_rope=tps_rope, level=level, participant=participant)
                    train.FBI()
                    record_base(participant, d1, entrainement, serie, tps_rope, level, poids, gras)
                if entrainement == 5:
                    print("Vous avez choisi de faire un entrainement Force à la poutre.\n")
                    print("Matériel : Vous avez besoin d'une barre de traction et d'un élastique et d'un gilet lesté.\n")
                    tps_rope = int(input("Choisissez le temps de repos entre les exercices : "))
                    serie = int(input("Combien de serie(s) souhaitez-vous faire ? : 1,2,3...? : "))
                    level = 0
                    train = Training(nbre_serie=serie, tps_rope=tps_rope, level=level, participant=participant)
                    train.Poutre_Force()
                    record_base(participant, d1, entrainement, serie, tps_rope, level, poids, gras)
                if entrainement == 6:
                    menu()
            if choix_menu ==2:
                print("Depuis que vous avez commencé a vous entrainer :")
                stat_entrainement(participant)
                if stat_poids(participant) is not None:
                    histo_part(participant)
                    difference = (stat_poids(participant) - poids)
                    if difference < 0 and poids > 0:
                        print(f"\nDepuis que vous vous entrainez vous avez pris {difference}kgs")
                    if difference > 0 and poids >0:
                        print(f"\nDepuis que vous vous entrainez vous avez perdu {difference}kgs")
                else:
                    print(f"\nBienvenue {participant} c'est la première fois que vous utilisez l'application"
                          f" revenez voir vos stats qand vous aurez fait quelques entrainements.")
            if choix_menu ==3:
                graph_poids(participant)
            if choix_menu ==4:
                print(f"Merci pour votre visite {participant} à bientôt.")
                break

menu()


