# Importer la bibliothèque fpdf
from fpdf import FPDF

# Créer un objet pdf
pdf = FPDF()

# Ajouter une page
pdf.add_page()

# Définir la police et la taille
pdf.set_font("Arial", size=12)

# Écrire le titre de la facture

# Insérer une image au-dessus de John Doe
pdf.image('wapiti_logo_png (1).png', x=0, y=10, w=40) # Vous pouvez changer le nom, la position et la taille de l'image selon vos besoins
pdf.set_y(10)
# Écrire l'adresse du destinataire
pdf.set_y(50)
pdf.cell(200, 10, txt="Jhon Doe", ln=1, align="L")
pdf.cell(200, 10, txt="123 Rue de la Paix", ln=2, align="L")
pdf.cell(200, 10, txt="75000 Paris", ln=3, align="L")

# Écrire en très grand caractères 'Facture' au-dessus de la date

pdf.set_font("Arial", "B",size=30) # Changer la taille de la police
pdf.set_y(50) # Positionner le curseur à 50 mm du haut
# Positionner le curseur à 10 mm du bord droit
pdf.set_x(200 - 10)
pdf.cell(0, 10, txt="Facture", ln=5, align="R") # Créer une cellule sans largeur définie pour aligner le texte à droite


# Écrire la date de la facture
pdf.set_font("Arial", size=12) # Rétablir la taille de la police
pdf.set_y(60) # Positionner le curseur à 60 mm du haut
pdf.cell(0, 10, txt="Date: 14/08/2023", ln=6, align="R") # Créer une cellule sans largeur définie pour aligner le texte à droite

# Créer une table avec les articles, les prix et les totaux
pdf.set_font("Arial", size=10)
pdf.ln(20) # Sauter une ligne
header = ["Article"]
data = [["Produit A", "1000.00", "2000.00"],
        ["Produit B", "500.00", "1500.00"],
        ["Produit C", "300.00", "900.00"],
        ["Produit D", "100.00", "400.00"]]
w = [80, 60, 60] # Largeur des colonnes
h = 10 # Hauteur des lignes

# Positionner le curseur à 10 mm du bord gauche
pdf.set_x(5)

# Définir la couleur de remplissage en noir (0, 0, 0)
pdf.set_fill_color(0, 0, 0)
# Définir la couleur du texte en blanc (255, 255, 255)
pdf.set_text_color(255, 255, 255)
# Écrire les en-têtes de la table avec le paramètre fill=True
for i in range(len(header)):
    pdf.cell(w[i], h, header[i], border=1, fill=True)
pdf.ln(h)

# Rétablir la couleur du texte en noir (0, 0, 0)
pdf.set_text_color(0, 0, 0)
# Écrire les données de la table
for row in data:
    # Positionner le curseur à 10 mm du bord gauche
    pdf.set_x(5)
    for i in range(len(row)):
        pdf.cell(w[i], h, row[i], border=1)
    pdf.ln(h)

# Écrire le total de la facture
pdf.set_font("Arial", size=12)
# Positionner le curseur à 10 mm du bord gauche
pdf.set_x(5)
pdf.cell(140, h, "Total TTC:", border=1)
pdf.cell(60, h, "5209.62 Euros", border=1)
pdf.set_fill_color(0, 0, 0)
pdf.set_text_color(255, 255, 255)

# Écrire la signature de la facture
pdf.ln(20) # Sauter une ligne
pdf.cell(200- 10, txt="Signature:", ln=6, align="R")
#pdf.image("signature.png", x=170, y=240, w=20) # Ajouter une image de signature

# Créer un pied de page et le remplir en gris
pdf.set_font("Arial", size=8)
# Définir la couleur de remplissage en gris (200, 200, 200)
pdf.set_fill_color(200, 200, 200)


pdf.cell(0, 10, txt="Facture-Excel - SIRET: 12345678901234 - Tel: 01 23 45 67 89 - Email: contact@facture-excel.com", ln=7, align="C")

# Enregistrer le pdf
pdf.output("facture.pdf")
