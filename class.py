liste_exos1 = {"Abdos": 10, "Bras_tendu_coude": 5}
liste_exos2 = liste_exos1.values()

print("Liste exercice :")
for exo, qte in liste_exos1.items():
    print (f"{exo} : {qte}")


def choix_diff(level):
    if level == 1:
         liste_exos = {"Abdos rameur": 15, "Bras tendu coude": 10, "Tractions": 5, "Mountain Climbers": 15, "Pompes": 5}
    if level == 2:
         liste_exos = {"Abdos rameur": 20, "Bras tendu coude": 15, "Tractions": 10, "Mountain Climbers": 20, "Pompes": 10}
    if level == 3:
         liste_exos = {"Abdos rameur": 25, "Bras tendu coude": 20, "Tractions": 15, "Mountain Climbers": 25, "Pompes": 15}
    if level == 4:
         liste_exos = {"Abdos rameur": 30, "Bras tendu coude": 25, "Tractions": 20, "Mountain Climbers": 30, "Pompes": 20}
    # random.shuffle(liste_exos)
    # liste_exos = liste_exos[0:5]

    return liste_exos