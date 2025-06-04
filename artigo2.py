# Script de Geração de PDF - Artigo 2: Importância da Suplementação Mineral para Cavalos
# Desenvolvido para criar um PDF com design profissional

from fpdf import FPDF

# Função para gerar o PDF
def gerar_pdf_artigo_2():
    pdf = FPDF()
    pdf.add_page()

    # Configurando a imagem de fundo (marca d'água)
    pdf.image('Marca_Dagua_Cavalo_Suplementacao_Suave.png', x=0, y=0, w=210, h=297)

    # Definindo fonte e título com cor destacada
    pdf.set_font("Arial", 'B', 16)
    pdf.set_text_color(0, 50, 0)
    pdf.multi_cell(0, 10, "Importância da Suplementação Mineral para Cavalos\n\n", align='C')

    # Texto do artigo com cor destacada e justificado
    pdf.set_font("Arial", '', 12)
    texto_artigo = """Introdução
Os minerais são nutrientes essenciais para a saúde e desempenho dos cavalos...

Principais Minerais e Suas Funções
- Cálcio e Fósforo...
- Magnésio...
- Eletrólitos...

Comparação entre Minerais"""

    pdf.multi_cell(0, 8, texto_artigo, align='J')

    # Tabela justificada
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(63, 10, "Mineral", 1, 0, 'C')
    pdf.cell(63, 10, "Deficiência", 1, 0, 'C')
    pdf.cell(63, 10, "Sintomas", 1, 1, 'C')

    pdf.cell(63, 10, "Cálcio", 1, 0, 'C')
    pdf.cell(63, 10, "Hipocalcemia", 1, 0, 'C')
    pdf.cell(63, 10, "Fraqueza, tetania", 1, 1, 'C')

    # Salvando o PDF
    pdf.output('Artigo_Importancia_Suplementacao_Mineral_Final.pdf')

# Executando o script
if __name__ == '__main__':
    gerar_pdf_artigo_2()
