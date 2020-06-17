def choix_diff(level):
    if level == 1:
         liste_exos = {"Abdos rameur": 15, "Bras tendu coude": 10,
                       "Tractions": 5, "Mountain Climbers": 15, "Pompes": 5}
    if level == 2:
         liste_exos = {"Abdos rameur": 20, "Bras tendu coude": 12,
                       "Tractions": 7, "Mountain Climbers": 18, "Pompes": 7}
    if level == 3:
         liste_exos = {"Abdos rameur": 25, "Bras tendu coude": 20,
                       "Tractions": 15, "Mountain Climbers": 25, "Pompes": 15}
    if level == 4:
         liste_exos = {"Abdos rameur": 30, "Bras tendu coude": 25,
                       "Tractions": 20, "Mountain Climbers": 30, "Pompes": 20}
    return liste_exos

def choix_diff2(level):
    if level == 1:
        liste_exos2 = {"La Planche": 60, "Superman": 60, "La Planche Latérale Gauche": 45,
                       "La Planche Latérale Droite": 45, "La Planche Dos": 60}
    if level == 2:
        liste_exos2 = {"La Planche": 60, "La Planche Latérale Gauche avec torsion": 30,
                       "La Planche Latérale Droite avec torsion": 30,
                       "La Planche 1 bras 1 jambe levée gauche": 30,
                       "La Planche 1 bras 1 jambe levée droit": 30}
    return liste_exos2


def choix_diff3(level):
    if level == 1:
         liste_exos3 = {"Dips": 5, "Pompes pieds surélevés": 10,
                       "Pompes": 10, "Tractions": 10}
    if level == 2:
        liste_exos3 = {"Dips": 10, "Pompes pieds surélevés": 15,
                      "Pompes": 15, "Tractions": 15}

    return liste_exos3

def choix_diff4(level):
    if level == 1:
        liste_exos4 = {"Tractions_lentes" : 10}
    if level == 2:
        liste_exos4 = {"Frenchies": 10}
    if level == 3:
        liste_exos4 = {"Tractions_négative" : 3}
    return liste_exos4
