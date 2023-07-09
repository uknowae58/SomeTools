# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 16:25:21 2023

@author: Franz Burauer
"""

import numpy as np
from Dateiauswahl import fallunterscheidung



def Position(liste_einstellversuche, liste_nachweisversuche):
    positions1 = [[] for _ in range(15)]  # Leere Liste für jede Position erstellen
    positions2 = [[] for _ in range(15)]  # Leere Liste für den zweiten Datensatz
    gleicheelemente1 = []
    gleicheelemente2 = []
    
    def istGleich(x): #vergleichen aller Listenelemente einer Liste
        return np.all(np.array(x[1:]) == x[:-1])
    
    
    
    for dateiname in liste_einstellversuche:
        parts = dateiname.split('_')  # Dateinamen anhand des Unterstrich-Zeichens aufteilen
        for i in range(15):
            positions1[i].append(parts[i])  # Jeden Schlüssel an die entsprechende Position in positions1 anfügen
    
    # Ergebnisse ausgeben
    for i, position_list in enumerate(positions1):
        #print(f"Position {i+1}: {position_list}")
    
        if istGleich(position_list) == True :
            #print ("alle Elemente der Liste sind gleich")
            gleicheelemente1.append(i+1)
        else:
            #print("es sind nicht alle Elemente der Liste gleich")
            pass
        # Überprüfen, ob alle Elemente in den Listen gleich sind
    
    for dateiname in liste_nachweisversuche:
        parts = dateiname.split('_')  # Dateinamen anhand des Unterstrich-Zeichens aufteilen
        for i in range(15):
            positions2[i].append(parts[i])  # Jeden Schlüssel an die entsprechende Position in positions2 anfügen
            
    for i, position_list in enumerate(positions2):
        #print(f"Position {i+1}: {position_list}")
        
        if istGleich(position_list) == True :
            #print ("alle Elemente der Liste sind gleich")
            gleicheelemente2.append(i+1)
        else:
            #print("es sind nicht alle Elemente der Liste gleich")
            pass
            
    def find_common_values(list1, list2):
        moeglicheKandidaten = []
        for item in list1:
            if item in list2:
                moeglicheKandidaten.append(item)  # Gemeinsamen Wert gefunden, Rückgabe des Wertes
        return moeglicheKandidaten # Keinen gemeinsamen Wert gefunden
    
    moeglicheKandidaten = find_common_values(gleicheelemente1, gleicheelemente2)
    
    if len(moeglicheKandidaten) > 0:
        #print("Gemeinsame Werte gefunden:")
        for value in moeglicheKandidaten:
            #print(value)
            pass
    else:
        #print("Keine gemeinsamen Werte gefunden.")
        pass
    #print(f"mögliche Kandidaten sind: {moeglicheKandidaten}")
    
    for position in moeglicheKandidaten:
        unterschiede_gefunden = False
        for i in range(len(liste_einstellversuche)):
            if positions1[position-1][i] != positions2[position-1][i]:
                dieRichtigePosition = position
                #print(f"Die richtige Position ist {position}")
                unterschiede_gefunden = True
                break  # Sobald ein Unterschied gefunden wurde, die Schleife beenden
        if not unterschiede_gefunden:
            #print(f"Keine Unterschiede gefunden in Position {position}")
            pass
    
    
    

    
    # if dieRichtigePosition < 2:
    #     print("Fehler bei der Länge der Zahl")
    #     pass
    # elif dieRichtigePosition >= 2:
    #     Key1 = 6+3*(dieRichtigePosition-2)-1
    #     Key2 = 6+3*(dieRichtigePosition-2)
    # #print(gleicheelemente1)
    # return Key1,Key2
    # #return dieRichtigePosition
    for element in liste_einstellversuche:
        position = element.index(positions1[dieRichtigePosition-1][1])
        #print(f"Die Position vom gesuchten Schlüssel im Dateinamen ist: {position} und {position+1}")
        return position, position+1, liste_einstellversuche,liste_nachweisversuche
        break

#wert = fallunterscheidung("C:/Users/Franz Burauer/Documents/Studium/Vorlesungen/TH Köln/Informatikprojekt/Projekt/Aufgabe_04/S0_Messdaten")
    
#print(Position(wert[0],wert[1]))#Rückgabe von der ersten Position des Keys, der 2 Position des Keys, aller Dateinamen