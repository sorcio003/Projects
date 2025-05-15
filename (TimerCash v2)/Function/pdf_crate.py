from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import os

def create_invoice(pdf_file, invoice_data, receiver, time):
    # Informazioni di base dalla fattura
    invoice_number = invoice_data.get('invoice_number', '')
    invoice_date = invoice_data.get('invoice_date', '')
    client_name = invoice_data.get('provider_name', '')
    items = invoice_data.get('items', [])
    total_amount = invoice_data.get('total_amount', '')

    script_dir = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(script_dir, "logo.png")

    # Creazione del documento PDF
    doc = SimpleDocTemplate(pdf_file, pagesize=letter)
    elements = []

    # Stili di testo
    styles = getSampleStyleSheet()
    style_normal = styles["Normal"]
    style_title = styles["Title"]
    
    elements.append(Paragraph("<b>Timer Cash Python</b>", style_title))
    elements.append(Paragraph("\n", style_normal))

    # Aggiungere il logo e il nome dell'app
    if os.path.exists(logo_path):
        logo = Image(logo_path, width=1*inch, height=1*inch)
        elements.append(logo)
    else:
        elements.append(Paragraph("Logo non trovato", style_normal))
        
    elements.append(Paragraph("Fattura Numero: {}".format(invoice_number), style_normal))
    elements.append(Spacer(1, 12))

    # Informazioni del lavoratore
    receiver_info = " ".join(receiver[:2])
    elements.append(Paragraph("<b>"+receiver_info+"</b>", style_normal))
    elements.append(Paragraph("email: " + receiver[2], style_normal))
    elements.append(Paragraph("\n", style_normal))

    # Intestazione
    elements.append(Paragraph("Data: {}".format(invoice_date), style_normal))
    elements.append(Paragraph("Provider: {}".format(client_name), style_normal))
    elements.append(Spacer(1, 12))

    # Tabella degli articoli
    data = [["Tipo di lavoro", "Ora di inizio", "Ora di fine", "Tariffa oraria", "Totale ore", "Totale"]]
    for item in items:
        data.append([item.get('description', ''), item.get('start_time', ''), item.get('end_time', ''), item.get('hourly_rate', ''), item.get('total_hours', ''), item.get('total', '')])
    t = Table(data)
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.aqua),
                           ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                           ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                           ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                           ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                           ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                           ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    elements.append(t)

    # Importo totale
    elements.append(Spacer(1, 12))
    elements.append(Paragraph("\nImporto totale: {} €".format(total_amount), style_normal))

    # Firma
    elements.append(Spacer(1, 50))
    elements.append(Paragraph("Data: " + time.strftime("%d/%m/%Y") + "   ________________________Firma", style_normal))

    # Generazione del PDF
    doc.build(elements)