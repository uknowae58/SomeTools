# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 14:26:00 2023

@author: Franz Burauer
"""

import os
from darstellung_als_Grafik import grafik
from Versuch20 import versuch20

def fallunterscheidung(ordner):#ordner als pfad für ordner der csv datei
    pfade = os.listdir(ordner)#auslesen des Ordners
    #Aufteilen der Dateien im Ordner nach Einstellversuchen
    i = 0
    liste_einstellversuche = []
    liste_nachweisversuche = []
    while i < len(pfade):
        grafik(ordner+"/"+pfade[i])
        if versuch20(ordner+"/"+pfade[i]) == True:
            liste_einstellversuche.append(pfade[i])
        else:
            liste_nachweisversuche.append(pfade[i])
        
        
        i += 1
    
    
    print(f"Die Anzahl der Einstellversuche in dem Ordner beträgt: {len(liste_einstellversuche)}")    
    print(liste_einstellversuche)
    print(f"Die Anzahl der Nachweisversuche in dem Ordner beträgt: {len(liste_nachweisversuche)}")    
    print(liste_nachweisversuche)
    return liste_einstellversuche, liste_nachweisversuche, pfade


#fallunterscheidung("C:/Users/Franz Burauer/Documents/Studium/Vorlesungen/TH Köln/Informatikprojekt/Projekt/Aufgabe_04/S0_Messdaten")



    