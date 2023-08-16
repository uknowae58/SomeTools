from fpdf import FPDF

class PDF(FPDF):

    def table(self, header, data):
        self.set_font('Arial', 'B', 12)
        w = [160]

        for i in range(len(header)):
            self.set_y(34)
            self.cell(w[i], 7, header[i], 1, 0, 'C')
        self.ln()
        fill = False
        for row in data:
            self.set_font('Arial', 'B', 10)
            self.set_fill_color(0, 0, 0)
            self.set_text_color(255, 255, 255)
            self.cell(w[0], 6, row[0], 'LR', fill=True)
            self.ln()
            fill = not fill
            self.set_font('Arial', '', 8)
            for i, sub_row in enumerate(row[1]):
                if i == len(row[1]) - 1:
                    self.set_font('Arial', 'B', 10)
                    self.set_fill_color(200, 200, 200)
                else:
                    self.set_fill_color(221, 221, 221)
                    self.set_text_color(0, 0, 0)

                self.cell(80, 6, sub_row[0], 1, fill=True)
                self.cell(80, 6, sub_row[1], 1, fill=True)
                self.ln()
                fill = not fill
        self.cell(sum(w), 0, '', 'T')


pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Écrire le titre de la facture

# Insérer une image au-dessus de John Doe
pdf.image('wapiti_logo_png (1).png', x=(210-40)/2, y=10, w=40) # Vous pouvez changer le nom et la taille de l'image selon vos besoins
pdf.set_y(10)


# Écrire en très grand caractères 'Facture' au-dessus de la date

pdf.set_font("Arial", "B",size=21) # Changer la taille de la police
pdf.set_y(50) # Positionner le curseur à 50 mm du haut
pdf.cell(0, 10, txt="Cotation adressée a la coopérative ", ln=5, align="C") # Créer une cellule sans largeur définie pour centrer le texte
pdf.cell(0, 10, txt=" coopérative ", ln=5, align="C") # Créer une cellule sans largeur définie pour centrer le texte


# Écrire la date de la facture
pdf.set_font("Arial",'B', size=14) # Rétablir la taille de la police
pdf.set_y(100) # Positionner le curseur à 100 mm du haut
pdf.cell(0, 8, txt="Numéro de l'offre: 14/08/2023", ln=6, align="L") # Créer une cellule sans largeur définie pour aligner le texte à droite
pdf.cell(0, 8, txt="Organisme de certification: 14/08/2023", ln=6, align="L") # Créer une cellule sans largeur définie pour aligner le texte à droite
pdf.cell(0, 8, txt="Titulaire du certificat: 14/08/2023", ln=6, align="L") # Créer une cellule sans largeur définie pour aligner le texte à droite
pdf.cell(0, 8, txt="Code du Titulaire du certificat: 14/08/2023", ln=6, align="L") # Créer une cellule sans largeur définie pour aligner le texte à droite
pdf.cell(0, 8, txt="Personne de contact: 14/08/2023", ln=6, align="L") # Créer une cellule sans largeur définie pour aligner le texte à droite
pdf.cell(0, 8, txt="Contact: 14/08/2023", ln=6, align="L") # Créer une cellule sans largeur définie pour aligner le texte à droite
pdf.cell(0, 8, txt="Adresse: 14/08/2023", ln=6, align="L") # Créer une cellule sans largeur définie pour aligner le texte à droite

pdf.set_font("Arial",'', size=11) # Rétablir la taille de la police
pdf.cell(0, 21, txt="Veuillez trouver ci-après notre cotation pour les frais liés au deplacement de l'équipe d'audit", ln=10, align="C") # Créer une cellule sans largeur définie pour aligner le texte à droite

header = ['Distance totale parcourue en km']
data = [['DISTANCES VOYAGES', [
                     ['ABIDJAN-KOUIBLY', '500km'],
                     ['KOUIBLY-ABIDJAN', '600km'],
                     ['Distance totale du trajet', '1100km']]],
        ['DISTANCES ICS', [
                           ['Nombre jours ICS:', 'Distance 1'],
                           ['Distance moyenne/jour ', 'Distance 2'],
                           ['Distance totale ICS','Distance 3']]],
        [' DISTANCES VISITE EN PLANTATIONS', [
                                         ['Nombre jours visite en plantations:', 'Distance 1'],
                                         ['Distance moyenne/jour ', 'Distance 2'],
                                         ['Distance totale visite en plantations', 'Distance 3']]]]

# Location de vehicules

pdf.set_font("Arial",'B', size=17) # Rétablir la taille de la police
pdf.cell(0, 16, txt="Location de vehicules", ln=6, align="L")

pdf.set_font("Arial", size=10)
pdf.ln(5) # Sauter une ligne
header1 = ["Location de vehicule"]
data1 = [["Jours",''],
        ["Cout/ Jour",'']]
w = [80, 60, 60] # Largeur des colonnes
h = 6 # Hauteur des lignes


pdf.set_x(10)

pdf.set_fill_color(0, 0, 0)
pdf.set_text_color(255, 255, 255)
pdf.set_font('Arial', 'B', 13)
# Écrire les en-têtes de la table avec le paramètre fill=True
for i in range(len(header1)):
    pdf.cell(w[i], h, header1[i], border=1, fill=True)
pdf.ln(h)

pdf.set_fill_color(221, 221, 221)
pdf.set_text_color(0, 0, 0)
pdf.set_font('Arial', '', 9)
# Écrire les données de la table
for row in data1:
    pdf.set_x(10)
    for i in range(len(row)):
        if i == len(row[1]) - 1:
            pdf.set_font('Arial', 'B', 10)
            pdf.set_fill_color(200, 200, 200)
        else:
            pdf.set_fill_color(221, 221, 221)

        pdf.cell(w[i], h, row[i], border=1,fill=True)
    pdf.ln(h)
# Écrire le total de la facture
pdf.set_font("Arial",'B', size=12)
pdf.set_fill_color(200, 200, 200)
pdf.set_text_color(0, 0, 0)

pdf.set_x(10)
pdf.cell(80, h, "Cout totale de la location de vehicule", border=1,fill=True)
pdf.set_fill_color(255, 223, 145)
pdf.cell(60, h, "15616 FR CFA", border=1,fill=True)
pdf.ln(10)

#Peage
pdf.set_font("Arial",'B', size=17)
pdf.cell(0, 16, txt="Péage", ln=6, align="L")

pdf.set_y(255)
pdf.set_font("Arial",'B', size=13)
pdf.set_fill_color(0, 0, 0)
pdf.set_text_color(255, 255, 255)
pdf.set_x(10)

pdf.cell(140, h, "Péage", border=1, fill=True)
pdf.ln(h)
pdf.set_font("Arial",'B', size=11)
pdf.set_fill_color(255, 223, 145)
pdf.set_text_color(0, 0, 0)
pdf.cell(140, h, "5000 FR CFA", border=1,fill=True)

#Distance
pdf.set_x(10)
pdf.set_font("Arial",'B', size=17) # Rétablir la taille de la police
pdf.cell(0, 16, txt="Distances", ln=6, align="L")
pdf.table(header,data)

#Distance totale
pdf.set_y(121)
pdf.set_font("Arial",'B', size=9)
pdf.set_fill_color(0, 0, 0)
pdf.set_text_color(255, 255, 255)
pdf.set_x(10)

pdf.cell(70, h, "Distance totale a parcourir", border=1, fill=True)
pdf.ln(h)
pdf.set_font("Arial",'B', size=11)
pdf.set_fill_color(200, 200, 200)
pdf.set_text_color(0, 0, 0)
pdf.cell(70, h, "1500000 km", border=1,fill=True)
pdf.ln(10)


#Consommation de carburant
pdf.set_y(145)
pdf.set_font("Arial",'B', size=17) # Rétablir la taille de la police
pdf.cell(0, 16, txt="Consommation de carburant", ln=6, align="L")

pdf.set_y(150)
pdf.set_font("Arial", size=10)
pdf.ln(20) # Sauter une ligne
header1 = ["Consommation de carburant"]
data1 = [["Consommation Moyenne(L/100km)",''],
        ["Quantité de carburant",''],["Cout unitaire du litre de carburant",'']]
w = [80, 60, 60] # Largeur des colonnes
h = 6 # Hauteur des lignes


pdf.set_x(10)

pdf.set_fill_color(0, 0, 0)
pdf.set_text_color(255, 255, 255)
pdf.set_font('Arial', 'B', 12)
# Écrire les en-têtes de la table avec le paramètre fill=True
for i in range(len(header1)):
    pdf.cell(w[i], h, header1[i], border=1, fill=True)
pdf.ln(h)


pdf.set_fill_color(221, 221, 221)
pdf.set_text_color(0, 0, 0)
pdf.set_font('Arial', '', 9)
# Écrire les données de la table
for row in data1:
    pdf.set_x(10)
    for i in range(len(row)):
        if i == len(row[1]) - 1:
            pdf.set_font('Arial', 'B', 10)
            pdf.set_fill_color(200, 200, 200)
        else:
            pdf.set_fill_color(221, 221, 221)

        pdf.cell(w[i], h, row[i], border=1,fill=True)
    pdf.ln(h)
# Écrire le total
pdf.set_font("Arial",'B', size=12)
pdf.set_fill_color(200, 200, 200)
pdf.set_text_color(0, 0, 0)

pdf.set_x(10)
pdf.cell(80, h, "Cout totale du carburant", border=1,fill=True)
pdf.set_fill_color(255, 223, 145)
pdf.cell(60, h, "15616", border=1,fill=True)
pdf.ln()

#Montant Total A payer
pdf.set_y(203)
pdf.set_font("Arial",'B', size=17) # Rétablir la taille de la police
pdf.cell(0, 16, txt="Montant total a payer", ln=6, align="L")
pdf.set_y(221)

pdf.set_font("Arial",'B', size=13)
pdf.set_fill_color(0, 0, 0)
pdf.set_text_color(255, 255, 255)
pdf.set_x(10)

pdf.cell(140, h, "Total", border=1, fill=True)
pdf.ln(h)
pdf.set_font("Arial",'B', size=15)
#30, 217, 97
pdf.set_fill_color(255, 223, 145)
pdf.set_text_color(0, 0, 0)
pdf.cell(140, 13, "5000 FR CFA", border=1,fill=True)


# Écrire la signature de la facture
pdf.set_font("Arial",'I', size=10)
pdf.set_text_color(0, 0, 0)
pdf.ln(20) # Sauter une ligne
pdf.cell(200- 10, txt="Associé gérant Wapiticar SARL:", ln=6, align="R")
pdf.ln(5)
pdf.cell(200- 10, txt="Luc-Arnaud Yapi", ln=6, align="R")
pdf.image("N°CC 2245356 L-pdf.png", x=170, y=255, w=37) # Ajouter une image de signature

pdf.cell(200- 10, txt="Le client:", ln=6, align="L")
pdf.ln(2)



#pdf.cell(0, 140, txt="Facture-Excel - SIRET: 12345678901234 - Tel: 01 23 45 67 89 - Email: contact@facture-excel.com", ln=7, align="C")
pdf.output('table.pdf', 'F')
