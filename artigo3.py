# Script de Geração de PDF - Artigo 3: Estratégias de Manejo Nutricional para Cavalos Idosos
# Desenvolvido para criar um PDF com design profissional

from fpdf import FPDF

# Função para gerar o PDF
def gerar_pdf_artigo_3():
    pdf = FPDF()
    pdf.add_page()

    # Configurando a imagem de fundo (marca d'água)
    pdf.image('Marca_Dagua_Cavalo_Idoso_Suave.png', x=0, y=0, w=210, h=297)

    # Definindo fonte e título com cor destacada
    pdf.set_font("Arial", 'B', 16)
    pdf.set_text_color(0, 50, 0)
    pdf.multi_cell(0, 10, "Estratégias de Manejo Nutricional para Cavalos Idosos\n\n", align='C')

    # Texto do artigo com cor destacada e justificado
    pdf.set_font("Arial", '', 12)
    texto_artigo = """Introdução
À medida que os cavalos envelhecem, suas necessidades nutricionais mudam...

Principais Desafios Nutricionais
- Redução da Capacidade Digestiva...
- Perda de Massa Muscular...

Suplementação Específica"""

    pdf.multi_cell(0, 8, texto_artigo, align='J')

    # Tabela justificada
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(63, 10, "Nutriente", 1, 0, 'C')
    pdf.cell(63, 10, "Função", 1, 0, 'C')
    pdf.cell(63, 10, "Fonte Recomendada", 1, 1, 'C')

    pdf.cell(63, 10, "Proteínas", 1, 0, 'C')
    pdf.cell(63, 10, "Manutenção muscular", 1, 0, 'C')
    pdf.cell(63, 10, "Farelo de soja, alfafa", 1, 1, 'C')

    # Salvando o PDF
    pdf.output('Artigo_Estrategias_Manejo_Cavalos_Idosos_Final.pdf')

# Executando o script
if __name__ == '__main__':
    gerar_pdf_artigo_3()
