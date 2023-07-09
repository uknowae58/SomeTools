# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 16:58:45 2023

@author: man61
"""
import pandas 
import matplotlib.pyplot as plt
#import numpy as np

def versuch20(pfad):#datei als vordefinierte Funktion


    datei = pandas.read_csv(f"{pfad}", sep="_")
    #berechnung mit endvorspannkraft/anfangsvorspannkraft
    ergebnis = datei.Vorspannkraft[len(datei.Vorspannkraft)-1]/datei.Vorspannkraft[0] #prüfen, ob unter 20%
    #try():
    if  ergebnis < 0.2:#identifizieren der Versuchsart
        return True #Ausgabe als Warheitswert, eingabe ist ein Einstellversuch
    else:
        return False
#print(versuch20("C:/Users/man61/Desktop/Uni/Informatikprojekt/Gruppenprojekt/Aufgabe_04/S0_Messdaten/04_IP23_FA_5M_6g_Fu_2r_32_Rq_V7_mj_Ao_B7_rj_yw.csv"))