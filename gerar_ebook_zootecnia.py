from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.lib.colors import HexColor
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle, Paragraph, Frame, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.textlabels import Label
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.units import cm

# Cores e dimensões
azul_marinho = HexColor("#002e6d")
width, height = A4

# Caminhos das imagens (substitua pelos seus arquivos locais)
img_capa = "capa.png"
img_sumario = "sumario.png"
img_artigo1 = "artigo1.png"
img_artigo2 = "artigo2.png"
img_artigo3 = "artigo3.png"

# Nome do arquivo de saída
output = "Ebook_Zootecnia_Equina_Completo_FINAL.pdf"

# Criar o canvas principal
pdf = canvas.Canvas(output, pagesize=A4)

# === CAPA ===
pdf.drawImage(img_capa, 0, 0, width=width, height=height)
pdf.setFillColor(azul_marinho)
pdf.setFont("Helvetica-Bold", 26)
pdf.drawCentredString(width / 2, height - 100, "Guia Completo de Nutrição e Manejo")
pdf.drawCentredString(width / 2, height - 135, "para Cavalos Atletas")
pdf.setFont("Helvetica-Bold", 16)
pdf.drawCentredString(width / 2, height / 2, "Energia, Suplementação e Estratégias Práticas")
pdf.setStrokeColor(azul_marinho)
pdf.setLineWidth(1)
pdf.line(width / 2 - 180, height / 2 - 5, width / 2 + 180, height / 2 - 5)
pdf.setFont("Helvetica-Bold", 14)
pdf.drawCentredString(width / 2, 80, "Autor: Alexandre Augusto – Zootecnista e Consultor em Equinocultura")
pdf.showPage()

# === SUMÁRIO ===
pdf.drawImage(img_sumario, 0, 0, width=width, height=height)
pdf.setFillColor(azul_marinho)
pdf.setFont("Helvetica-Bold", 16)
pdf.drawString(50, height - 80, "Sumário")

sumario_itens = [
    ["1. Introdução", "3"],
    ["2. Artigo 1: Qual a Melhor Fonte de Energia para Cavalos Atletas", "4"],
    ["3. Importância da Suplementação Mineral", "7"],
    ["4. Estratégias de Manejo Nutricional para Cavalos Idosos", "10"],
    ["5. Conclusão", "13"],
    ["6. Referências", "14"]
]

pdf.setFont("Helvetica", 11)
y = height - 120
for item in sumario_itens:
    titulo, pagina = item
    linha = f"{titulo}{'.' * (90 - len(titulo))}{pagina}"
    pdf.drawString(60, y, linha)
    y -= 20
pdf.showPage()

# === ARTIGO 1 ===
pdf.drawImage(img_artigo1, 0, 0, width=width, height=height, mask='auto')
pdf.setFillColor(azul_marinho)
pdf.setFont("Helvetica-Bold", 16)
pdf.drawString(50, height - 80, "Artigo 1: Qual a Melhor Fonte de Energia para Cavalos Atletas?")

pdf.setFont("Helvetica", 12.5)
textos1 = [
    "A energia é o combustível que move os cavalos atletas. Mas qual fonte escolher?",
    "Cavalos de explosão, como os de corrida ou salto, se beneficiam de carboidratos de rápida absorção.",
    "Já os cavalos de resistência, como os de enduro, respondem melhor às gorduras de liberação prolongada.",
    "A escolha da fonte energética deve considerar o tipo de atividade, a duração do esforço e o metabolismo individual do animal."
]
y = height - 110
for linha in textos1:
    pdf.drawString(50, y, linha)
    y -= 18

pdf.setFont("Helvetica-Oblique", 11)
pdf.drawString(50, y - 10, "Abaixo, comparamos as principais fontes de energia utilizadas em dietas para cavalos atletas:")

tabela1 = [
    ["Fonte de Energia", "Tipo", "Benefício", "Modalidade Ideal"],
    ["Milho", "Carboidrato", "Energia rápida", "Corrida e Salto"],
    ["Aveia", "Carboidrato", "Energia moderada", "Provas mistas"],
    ["Óleo de Arroz", "Gordura", "Energia sustentada", "Enduro"]
]
table = Table(tabela1, colWidths=[4.5*cm]*4)
table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
    ("TEXTCOLOR", (0,0), (-1,-1), azul_marinho),
    ("ALIGN", (0,0), (-1,-1), "CENTER"),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTNAME", (0,1), (-1,-1), "Helvetica"),
    ("FONTSIZE", (0,0), (-1,-1), 9),
    ("GRID", (0,0), (-1,-1), 0.5, colors.grey)
]))
table.wrapOn(pdf, width, height)
table.drawOn(pdf, 50, y - 100)
pdf.setFont("Helvetica-Oblique", 9)
pdf.drawString(50, y - 115, "Fonte: Adaptado de FRAPE, 2010; NRC, 2007.")
pdf.showPage()

# === CONTINUAR COM ARTIGO 2, 3, CONCLUSÃO E REFERÊNCIAS ===
# Você pode seguir copiando a lógica do artigo 1 para os demais, alterando imagem, texto e dados conforme necessário.

pdf.save()
print("E-book gerado com sucesso: Ebook_Zootecnia_Equina_Completo_FINAL.pdf")
