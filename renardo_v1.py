# Fast coding of Renardo program used on French TV Show 
# "Des chiffres et des lettres" (https://en.wikipedia.org/wiki/Des_chiffres_et_des_lettres)
# by Alex-Pauline Poudade 11/26/2021

import random
random.seed()
 
 
def operations(t, max):
 
    signe = '+-*/'
 
    for i in range(0, 4):
        for j1 in range(1, max):
            for j2 in range(j1 + 1, max + 1):
                if i == 0:
                    a = t[j1] + t[j2]
                elif i == 1:
                    a = t[j1] - t[j2]
                elif i == 2:
                    a = t[j1] * t[j2]
                elif i == 3:
                    a = t[j1] // t[j2]
                    if t[j2] * a != t[j1]:
                        a = 0
 
                if a > 0:
                    if a == t[0]:
                        print("%s%s%s=%s" % (t[j1], signe[i], t[j2], a))
                        trouve = True
                        return trouve
 
                    t1 = t[:]
 
                    t1[j1] = a
                    t1[j2] = 0
                    while True:
                        echange = False
                        for ii in range(1, max):
                            if t1[ii] < t1[ii + 1]:
                                aa = t1[ii]
                                t1[ii] = t1[ii + 1]
                                t1[ii + 1] = aa
                                echange = True
                        if not echange:
                            break
                    trouve = operations(t1, max - 1)
                    if trouve:
                        print("%s%s%s=%s" % (t[j1], signe[i], t[j2], a))
                        return trouve
 
nb_a_trouver = int(input("Entrer le nombre: "))

nb1 = int(input("Entrer le nombre 1: "))
nb2 = int(input("Entrer le nombre 2: "))
nb3 = int(input("Entrer le nombre 3: "))
nb4 = int(input("Entrer le nombre 4: "))
nb5 = int(input("Entrer le nombre 5: "))
nb6 = int(input("Entrer le nombre 6: "))
 

nbs_dispo = [nb1, nb2, nb3, nb4, nb5, nb6]
nbs_dispo.sort(reverse=True)
print("Nombres disponibles", nbs_dispo)
print()
 
nombres = [nb_a_trouver] + nbs_dispo
 
trouve = operations(nombres, 6)
 
if not trouve:
         print("pas de solution")
