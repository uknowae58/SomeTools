# -*- coding: utf-8 -*-
"""
Created on Mon May 22 17:39:55 2023

@author: Franz Burauer
"""
import pandas 
import matplotlib.pyplot as plt
#import numpy as np

def grafik(pfad):
    df = pandas.read_csv(pfad, sep="_")
    #print (df)
    #Aufteilung in einzelne unterplots
    fig, axs = plt.subplots(3)
    #plot der Vorspannkraft
    axs[0].plot(df.Vorspannkraft,'tab:orange')
    axs[0].set_title('Vorspannkraft')
    #plot der Querkraft
    axs[1].plot(df.Querkraft,'tab:red')
    axs[1].set_title('Querkraft')
    #plot der Auslenkung
    axs[2].plot(df.Auslenkung,'tab:blue')
    axs[2].set_title('Auslenkung')
    #Code zur berechnung der Lastwechsel
    n = 0
    anzahl_Wechsel= 0
    while n < len(df.Lastwechsel)-1:
        
        if df.Lastwechsel[n] == df.Lastwechsel[n+1]:
            n += 1
        else:
            anzahl_Wechsel += 1
            n += 1
    #print(f"Anzahl der Lastwechsel in dem Versuch: {anzahl_Wechsel}")

#grafik('C:/Users/Franz Burauer/Documents/Studium/Vorlesungen/TH Köln/Informatikprojekt/Projekt/Aufgabe_04/S0_Messdaten/04_IP23_FA_5M_6g_Fu_2r_32_Rq_V7_mj_Ao_B7_rj_yw.csv')



#Code für einen light Modus ohne Diagrammausgabe für schnelleres Rechnen
def entscheidung(pfad):
    df = pandas.read_csv(pfad, sep="_")
    n = 0
    anzahl_Wechsel= 0
    while n < len(df.Lastwechsel)-1:
        
        if df.Lastwechsel[n] == df.Lastwechsel[n+1]:
            n += 1
        else:
            anzahl_Wechsel += 1
            n += 1
    #print(f"Anzahl der Lastwechsel in dem Versuch: {anzahl_Wechsel}")
#entscheidung('C:/Users/Franz Burauer/Documents/Studium/Vorlesungen/TH Köln/Informatikprojekt/Projekt/Aufgabe_04/S0_Messdaten/04_IP23_FA_5M_6g_Fu_8b_32_Rq_V7_mj_Ao_B7_rj_yw.csv')