from time import *
import time
from Exos import *
from Ziq import *

class Training():
    def __init__(self,nbre_serie,tps_rope,level,participant,repos_serie=180):
        self.nbre_serie = nbre_serie
        self.tps_rope = tps_rope
        self.repos_serie = repos_serie
        self.level = level
        self.participant = participant

    def cardio(self):
        debut = time.time()
        nbre_serie = self.nbre_serie
        tps_rope = self.tps_rope
        repos_serie = self.repos_serie
        print(f"Vous avez choisi de faire {self.nbre_serie} série(s) avec {self.tps_rope}s de corde à sauter"
              f" entre les exercices au niveau d'intensité {self.level}.\n")
        while self.nbre_serie > 0:
            print(f"--> Vous devez faire {tps_rope}s de corde à sauter sans vous arreter.")
            input("Appuyez sur la touche Enter quand vous etes prêt à commencer l'entrainement.\n")
            print("Mettez vous en place le compte à rebours va commencer dans 5 secondes.")
            print(
                "                         :::::::::   ::::::::  :::::::::  ::::::::::      ::::::::::: :::::::::::   :::   :::   ::::::::::")
            print(
                "                        :+:    :+: :+:    :+: :+:    :+: :+:                 :+:         :+:      :+:+: :+:+:  :+:    ")
            print(
                "                       +:+    +:+ +:+    +:+ +:+    +:+ +:+                 +:+         +:+     +:+ +:+:+ +:+ +:+     ")
            print(
                "                      +#++:++#:  +#+    +:+ +#++:++#+  +#++:++#            +#+         +#+     +#+  +:+  +#+ +#++:++#  ")
            print(
                "                     +#+    +#+ +#+    +#+ +#+        +#+                 +#+         +#+     +#+       +#+ +#+        ")
            print(
                "                    #+#    #+# #+#    #+# #+#        #+#                 #+#         #+#     #+#       #+# #+#          ")
            print(
                "                   ###    ###  ########  ###        ##########          ###     ########### ###       ### ##########      ")

            time.sleep(5)
            while self.tps_rope > 0:
                  self.tps_rope -= 1
                  print("\r","Il vous reste {}s de corde à sauter.".format(self.tps_rope), end="")
                  time.sleep(1)
                  if self.tps_rope == 0:
                      print("\n")
                      print(
                          "                ------------ --------    ********   ------------        --------   ---    ---  ------------ -----------    ")
                      print(
                          "                ************ ********   ----------  ************       **********  ***    ***  ************ ***********    ")
                      print(
                          "                ------------   ----    ************ ----              ----    ---- ---    ---  ----         ----    ---    ")
                      print(
                          "                    ****       ****    ---  --  --- ************      ***      *** ***    ***  ************ *********       ")
                      print(
                          "                    ----       ----    ***  **  *** ------------      ---      --- ---    ---  ------------ ---------       ")
                      print(
                          "                    ****       ****    ---  --  --- ****              ****    ****  ********   ****         ****  ****      ")
                      print(
                          "                    ----     --------  ***  **  *** ------------       ----------    ------    ------------ ----   ----     ")
                      print(
                          "                    ****     ********  ---      --- ************        ********      ****     ************ ****    ****    ")
                      son_chrono()
            liste_exos = choix_diff(self.level)
            for exos, nbre in liste_exos.items():
                fin_inter = time.time()
                chrono_inter = fin_inter - debut
                temps_inter = strftime('%M minutes et %S secondes', gmtime(chrono_inter))
                print("\n")
                print(f"--> Vous devez faire : {nbre} {exos} le chrono est à {temps_inter}")
                input("Appuyez sur la touche Enter quand vous avez terminé l'exercice pour passer à la suite du programme.\n")
                print(f"--> Vous devez faire {tps_rope}s de corde à sauter sans vous arreter.")
                print(
                    "                         :::::::::   ::::::::  :::::::::  ::::::::::      ::::::::::: :::::::::::   :::   :::   ::::::::::")
                print(
                    "                        :+:    :+: :+:    :+: :+:    :+: :+:                 :+:         :+:      :+:+: :+:+:  :+:    ")
                print(
                    "                       +:+    +:+ +:+    +:+ +:+    +:+ +:+                 +:+         +:+     +:+ +:+:+ +:+ +:+     ")
                print(
                    "                      +#++:++#:  +#+    +:+ +#++:++#+  +#++:++#            +#+         +#+     +#+  +:+  +#+ +#++:++#  ")
                print(
                    "                     +#+    +#+ +#+    +#+ +#+        +#+                 +#+         +#+     +#+       +#+ +#+        ")
                print(
                    "                    #+#    #+# #+#    #+# #+#        #+#                 #+#         #+#     #+#       #+# #+#          ")
                print(
                    "                   ###    ###  ########  ###        ##########          ###     ########### ###       ### ##########      ")

                self.tps_rope += tps_rope
                print("Mettez vous en place le compte à rebours va commencer dans 5 secondes.")
                time.sleep(5)
                while self.tps_rope > 0:
                      self.tps_rope -= 1
                      print("\r", "Il vous reste {}s de corde à sauter.".format(self.tps_rope), end="")
                      time.sleep(1)
                      if self.tps_rope == 0:
                          print("\n")
                          print(
                              "                ------------ --------    ********   ------------        --------   ---    ---  ------------ -----------    ")
                          print(
                              "                ************ ********   ----------  ************       **********  ***    ***  ************ ***********    ")
                          print(
                              "                ------------   ----    ************ ----              ----    ---- ---    ---  ----         ----    ---    ")
                          print(
                              "                    ****       ****    ---  --  --- ************      ***      *** ***    ***  ************ *********       ")
                          print(
                              "                    ----       ----    ***  **  *** ------------      ---      --- ---    ---  ------------ ---------       ")
                          print(
                              "                    ****       ****    ---  --  --- ****              ****    ****  ********   ****         ****  ****      ")
                          print(
                              "                    ----     --------  ***  **  *** ------------       ----------    ------    ------------ ----   ----     ")
                          print(
                              "                    ****     ********  ---      --- ************        ********      ****     ************ ****    ****    ")
                          son_chrono()
            self.tps_rope += tps_rope
            print("\n")
            self.nbre_serie -= 1
            if self.nbre_serie > 0:
                print(f"Il vous reste {self.nbre_serie} série(s) avant la fin de l'entrainement.")
            else:
                fin = time.time()
                chrono = fin - debut
                temps = strftime('%M minutes et %S secondes', gmtime(chrono))
                print(f"Félicitations {self.participant}, l'entrainement a duré {temps}.")
                print("Vous avez effectué : ")
                for exos, nbre in liste_exos.items():
                    self.nbre_serie += nbre_serie
                    print(f"{nbre*self.nbre_serie} {exos}")
                    self.nbre_serie = 0
            self.repos_serie = repos_serie
            while self.repos_serie > 0 and self.nbre_serie > 0:
                  self.repos_serie -= 1
                  print("\r","Il vous reste {}s de repos avant la prochaine série.".format(self.repos_serie), end="")
                  time.sleep(1)
            son_chrono()


    def gain(self):
        debut = time.time()
        nbre_serie = self.nbre_serie
        print(f"Vous avez choisi de faire {self.nbre_serie} série(s) de l'entrainement Gainage au niveau d'intensité {self.level}")
        input("Appuyer sur la touche Enter pour commencer l'entrainement")
        while self.nbre_serie > 0:
            liste_exos2 = choix_diff2(self.level)
            for exos2, nbre in liste_exos2.items():
                fin_inter = time.time()
                chrono_inter = fin_inter - debut
                temps_inter = strftime('%M minutes et %S secondes', gmtime(chrono_inter))
                print(f"\n--> Vous devez faire : {exos2} pendant {nbre}s vous avez commencé l'entrainement depuis {temps_inter}.")
                print("\nMettez vous en place le compte à rebours va commencer dans 5 secondes.")
                time.sleep(5)
                while nbre > 0:
                      nbre -= 1
                      print("\r","Il vous reste {}s.".format(nbre), end="")
                      time.sleep(1)
                son_chrono()
            print("\n")
            self.nbre_serie -= 1
            if self.nbre_serie > 0:
                print(f"Il vous reste {self.nbre_serie} série(s) avant la fin de l'entrainement.")
            else:
                fin = time.time()
                chrono = fin - debut
                temps = strftime('%M minutes et %S secondes', gmtime(chrono))
                print(f"Félicitations {self.participant}, l'entrainement a duré {temps}.")

            while self.repos_serie > 0 and self.nbre_serie > 0:
                  self.repos_serie -= 1
                  print("\r","Il vous reste {}s de repos avant la prochaine série.".format(self.repos_serie), end="")
                  time.sleep(1)
            son_chrono()

    def FBI(self):
        input(f"Vous avez choisi de faire l'entrainement FBI avec la musique Thunderstruck d'AC/DC"
              f" appuyez sur Enter pour commencer, vous avez 5s pour vous mettre en place avant le debut de la chanson. ")
        time.sleep(5)
        fbi_ACDC()

    def Poutre_Force(self):
        debut = time.time()
        print(f"Vous avez choisi de faire {self.nbre_serie} série(s) avec {self.tps_rope}s de repos\n")

        serie_exo1 = self.nbre_serie
        while serie_exo1 > 0:
            liste_exos4 = choix_diff4(1)
            for exos, nbre in liste_exos4.items():
                fin_inter = time.time()
                chrono_inter = fin_inter - debut
                temps_inter = strftime('%M minutes et %S secondes', gmtime(chrono_inter))
                print("\n")
                print(f"--> Vous devez faire : {nbre} {exos} le chrono est à {temps_inter}")
                input("Appuyer sur Enter quand vous avez terminé l'exercice")
                tps_exos = self.tps_rope
                while tps_exos > 0 and serie_exo1 > 1:
                    tps_exos -= 1
                    print("\r", "Il vous reste {}s de repos.".format(tps_exos), end="")
                    time.sleep(1)
                son_chrono()
            print("\n")
            serie_exo1 -= 1
            if serie_exo1 > 0:
                print(f"Il vous reste {serie_exo1} série(s) avant la fin de l'exercice.")
        repos_serie_exo1 = self.repos_serie
        while repos_serie_exo1 > 0:
            repos_serie_exo1 -= 1
            print("\r", "Il vous reste {}s de repos avant la prochaine série.".format(repos_serie_exo1), end="")
            time.sleep(1)
        son_chrono()

        serie_exo2 = self.nbre_serie
        while serie_exo2 > 0:
            liste_exos4 = choix_diff4(2)
            for exos, nbre in liste_exos4.items():
                fin_inter = time.time()
                chrono_inter = fin_inter - debut
                temps_inter = strftime('%M minutes et %S secondes', gmtime(chrono_inter))
                print("\n")
                print(f"--> Vous devez faire : {nbre} {exos} le chrono est à {temps_inter}")
                input("Appuyer sur Enter quand vous avez terminé l'exercice")
                tps_exos = self.tps_rope
                while tps_exos > 0 and serie_exo2 > 1:
                    tps_exos -= 1
                    print("\r", "Il vous reste {}s de repos.".format(tps_exos), end="")
                    time.sleep(1)
                son_chrono()
            print("\n")
            serie_exo2 -= 1
            if serie_exo2 > 0:
                print(f"Il vous reste {serie_exo2} série(s) avant la fin de l'exercice.")
        repos_serie_exo2 = self.repos_serie
        while repos_serie_exo2 > 0:
            repos_serie_exo2 -= 1
            print("\r", "Il vous reste {}s de repos avant la prochaine série.".format(repos_serie_exo2), end="")
            time.sleep(1)
        son_chrono()
        serie_exo3 = self.nbre_serie
        while serie_exo3 > 0 and serie_exo3 > 0:
            liste_exos4 = choix_diff4(3)
            for exos, nbre in liste_exos4.items():
                fin_inter = time.time()
                chrono_inter = fin_inter - debut
                temps_inter = strftime('%M minutes et %S secondes', gmtime(chrono_inter))
                print("\n")
                print(f"--> Vous devez faire : {nbre} {exos} le chrono est à {temps_inter}")
                input("Appuyer sur Enter quand vous avez terminé l'exercice")
                tps_exos = self.tps_rope
                while tps_exos > 0 and serie_exo3 > 1:
                    tps_exos -= 1
                    print("\r", "Il vous reste {}s de repos.".format(tps_exos), end="")
                    time.sleep(1)
                son_chrono()
            print("\n")
            serie_exo3 -= 1
            if serie_exo3 > 0:
                print(f"Il vous reste {serie_exo3} série(s) avant la fin de l'exercice.")

    def renfor(self):
        debut = time.time()
        print(f"Vous avez choisi de faire {self.nbre_serie} série(s) avec {self.tps_rope}s de repos\n")

        serie_exo1 = self.nbre_serie
        while serie_exo1 > 0:
            liste_exos3 = choix_diff3(1)
            for exos, nbre in liste_exos3.items():
                fin_inter = time.time()
                chrono_inter = fin_inter - debut
                temps_inter = strftime('%M minutes et %S secondes', gmtime(chrono_inter))
                print("\n")
                print(f"--> Vous devez faire : {nbre} {exos} le chrono est à {temps_inter}")
                input("Appuyer sur Enter quand vous avez terminé l'exercice")
                tps_exos = self.tps_rope
                while tps_exos > 0 and serie_exo1 > 1:
                    tps_exos -= 1
                    print("\r", "Il vous reste {}s de repos.".format(tps_exos), end="")
                    time.sleep(1)
                son_chrono()
            print("\n")
            serie_exo1 -= 1
            if serie_exo1 > 0:
                print(f"Il vous reste {serie_exo1} série(s) avant la fin de l'exercice.")
        repos_serie_exo1 = self.repos_serie
        while repos_serie_exo1 > 0:
            repos_serie_exo1 -= 1
            print("\r", "Il vous reste {}s de repos avant la prochaine série.".format(repos_serie_exo1), end="")
            time.sleep(1)
        son_chrono()

        serie_exo2 = self.nbre_serie
        while serie_exo2 > 0:
            liste_exos3 = choix_diff3(2)
            for exos, nbre in liste_exos3.items():
                fin_inter = time.time()
                chrono_inter = fin_inter - debut
                temps_inter = strftime('%M minutes et %S secondes', gmtime(chrono_inter))
                print("\n")
                print(f"--> Vous devez faire : {nbre} {exos} le chrono est à {temps_inter}")
                input("Appuyer sur Enter quand vous avez terminé l'exercice")
                tps_exos = self.tps_rope
                while tps_exos > 0 and serie_exo2 > 1:
                    tps_exos -= 1
                    print("\r", "Il vous reste {}s de repos.".format(tps_exos), end="")
                    time.sleep(1)
                son_chrono()
            print("\n")
            serie_exo2 -= 1
            if serie_exo2 > 0:
                print(f"Il vous reste {serie_exo2} série(s) avant la fin de l'exercice.")
        repos_serie_exo2 = self.repos_serie
        while repos_serie_exo2 > 0:
            repos_serie_exo2 -= 1
            print("\r", "Il vous reste {}s de repos avant la prochaine série.".format(repos_serie_exo2), end="")
            time.sleep(1)
        son_chrono()

        serie_exo3 = self.nbre_serie
        while serie_exo3 > 0:
            liste_exos3 = choix_diff3(3)
            for exos, nbre in liste_exos3.items():
                fin_inter = time.time()
                chrono_inter = fin_inter - debut
                temps_inter = strftime('%M minutes et %S secondes', gmtime(chrono_inter))
                print("\n")
                print(f"--> Vous devez faire : {nbre} {exos} le chrono est à {temps_inter}")
                input("Appuyer sur Enter quand vous avez terminé l'exercice")
                tps_exos = self.tps_rope
                while tps_exos > 0 and serie_exo2 > 1:
                    tps_exos -= 1
                    print("\r", "Il vous reste {}s de repos.".format(tps_exos), end="")
                    time.sleep(1)
                son_chrono()
            print("\n")
            serie_exo3 -= 1
            if serie_exo3 > 0:
                print(f"Il vous reste {serie_exo3} série(s) avant la fin de l'exercice.")
        repos_serie_exo3 = self.repos_serie
        while repos_serie_exo3 > 0:
            repos_serie_exo3 -= 1
            print("\r", "Il vous reste {}s de repos avant la prochaine série.".format(repos_serie_exo3), end="")
            time.sleep(1)
        son_chrono()

        serie_exo4 = self.nbre_serie
        while serie_exo4 > 0 and serie_exo4 > 0:
            liste_exos3 = choix_diff3(4)
            for exos, nbre in liste_exos3.items():
                fin_inter = time.time()
                chrono_inter = fin_inter - debut
                temps_inter = strftime('%M minutes et %S secondes', gmtime(chrono_inter))
                print("\n")
                print(f"--> Vous devez faire : {nbre} {exos} le chrono est à {temps_inter}")
                input("Appuyer sur Enter quand vous avez terminé l'exercice")
                tps_exos = self.tps_rope
                while tps_exos > 0 and serie_exo4 > 1:
                    tps_exos -= 1
                    print("\r", "Il vous reste {}s de repos.".format(tps_exos), end="")
                    time.sleep(1)
                son_chrono()
            print("\n")
            serie_exo4 -= 1
            if serie_exo4 > 0:
                print(f"Il vous reste {serie_exo4} série(s) avant la fin de l'exercice.")

        fin = time.time()
        chrono = fin - debut
        temps = strftime('%M minutes et %S secondes', gmtime(chrono))
        print(f"Félicitations {self.participant}, l'entrainement a duré {temps}.")
        print("Récapitulatif des exercies effectués :")
        liste_exos3 = choix_diff3(1)
        for exos, nbre in liste_exos3.items():
            print(f"{nbre * self.nbre_serie} {exos}")
        liste_exos3 = choix_diff3(2)
        for exos, nbre in liste_exos3.items():
            print(f"{nbre * self.nbre_serie} {exos}")
        liste_exos3 = choix_diff3(3)
        for exos, nbre in liste_exos3.items():
            print(f"{nbre * self.nbre_serie} {exos}")
        liste_exos3 = choix_diff3(4)
        for exos, nbre in liste_exos3.items():
            print(f"{nbre * self.nbre_serie} {exos}")






