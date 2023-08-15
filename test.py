from fpdf import FPDF

class PDF(FPDF):
    def titles(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Distance totale parcourue en km', 0, 0, 'C')
        self.ln(20)

    def table(self, header, data):
        self.set_font('Arial', 'B', 12)
        w = [160]
        for i in range(len(header)):
            self.cell(w[i], 7, header[i], 1, 0, 'C')
        self.ln()
        self.set_font('Arial', '', 12)
        fill = False
        for row in data:
            self.set_fill_color(200, 200, 200)
            self.cell(w[0], 6, row[0], 'LR', fill=fill)
            self.ln()
            fill = not fill
            for sub_row in row[1]:
                self.cell(80, 6, sub_row[0], 'LR', fill=fill)
                self.cell(80, 6, sub_row[1], 'LR', fill=fill)
                self.ln()
                fill = not fill
        self.cell(sum(w), 0, '', 'T')

pdf = PDF()
pdf.add_page()
pdf.titles()

header = ['DISTANCES']
data = [['Voyages', [['Voyage 1', 'Visite 1'],
                     ['Voyage 2', 'Visite 2'],
                     ['Voyage 3', 'Visite 3'],
                     ['Voyage 4', 'Visite 4'],
                     ['Voyage 5', 'Visite 5']]],
        ['ICS - Visite en Plantations', [['Visite 1', 'Distance 1'],
                                         ['Visite 2', 'Distance 2'],
                                         ['Visite 3', 'Distance 3'],
                                         ['Visite 4', 'Distance 4'],
                                         ['Visite 5', 'Distance 5']]]]
pdf.table(header, data)
pdf.output('table.pdf', 'F')
