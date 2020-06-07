from time import *
import time
from Exos import *


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
                      tps_exos = self.tps_rope
                      print("\r", "Il vous reste {}s de corde à sauter.".format(self.tps_rope), end="")
                      time.sleep(1)
                      if int(tps_exos) == 2*int(self.tps_rope):
                          print("Half Time")

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

            while self.repos_serie > 0 and self.nbre_serie > 0:
                  self.repos_serie -= 1
                  print("\r","Il vous reste {}s de repos avant la prochaine série.".format(self.repos_serie), end="")
                  time.sleep(1)

    def gain(self):
        debut = time.time()
        nbre_serie = self.nbre_serie
        tps_rope = self.tps_rope
        print(f"Vous avez choisi de faire {self.nbre_serie} série(s) de l'entrainement Gainage au niveau d'intensité {self.level} "
              f"chaque exercice devra etre effectué pendant {self.tps_rope}s.\n")
        input("Appuyer sur la touche Enter pour commencer l'entrainement")
        while self.nbre_serie > 0:
            liste_exos2 = choix_diff2(self.level)
            tps_exos = self.tps_rope
            for exos2 in liste_exos2:
                fin_inter = time.time()
                chrono_inter = fin_inter - debut
                temps_inter = strftime('%M minutes et %S secondes', gmtime(chrono_inter))
                print(f"\n--> Vous devez faire : {exos2} pendant {tps_exos}s vous avez commencé l'entrainement depuis {temps_inter}.")
                print("\nMettez vous en place le compte à rebours va commencer dans 5 secondes.")
                time.sleep(5)
                while self.tps_rope > 0:
                      self.tps_rope -= 1
                      print("\r","Il vous reste {}s.".format(self.tps_rope), end="")
                      time.sleep(1)
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

            while self.repos_serie > 0 and self.nbre_serie > 0:
                  self.repos_serie -= 1
                  print("\r","Il vous reste {}s de repos avant la prochaine série.".format(self.repos_serie), end="")
                  time.sleep(1)



