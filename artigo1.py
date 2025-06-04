# Script de Geração de PDF - Artigo: Qual a Melhor Fonte de Energia para Cavalos Atletas
# Desenvolvido para criar um PDF com design profissional

from fpdf import FPDF

# Função para gerar o PDF
def gerar_pdf_artigo():
    pdf = FPDF()
    pdf.add_page()

    # Configurando a imagem de fundo (marca d'água)
    pdf.image('Marca_Dagua_Cavalo_Verde_Suave.png', x=0, y=0, w=210, h=297)

    # Definindo fonte e título com cor destacada
    pdf.set_font("Arial", 'B', 16)
    pdf.set_text_color(0, 50, 0)
    pdf.multi_cell(0, 10, "Qual a Melhor Fonte de Energia para Cavalos Atletas\n\n", align='C')

    # Texto do artigo com cor destacada e justificado
    pdf.set_font("Arial", '', 12)
    texto_artigo = """Introdução
Os cavalos atletas possuem necessidades energéticas específicas que variam conforme a modalidade esportiva...

Principais Fontes de Energia
- Carboidratos de Rápida Digestão...
- Gorduras de Alta Qualidade...
- Proteínas como Fonte Secundária...

Comparação entre Fontes Energéticas"""

    pdf.multi_cell(0, 8, texto_artigo, align='J')

    # Tabela original, justificada
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(63, 10, "Fonte Energética", 1, 0, 'C')
    pdf.cell(63, 10, "Digestibilidade", 1, 0, 'C')
    pdf.cell(63, 10, "Ideal para", 1, 1, 'C')

    pdf.set_font("Arial", '', 12)
    pdf.cell(63, 10, "Carboidratos", 1, 0, 'C')
    pdf.cell(63, 10, "Alta", 1, 0, 'C')
    pdf.cell(63, 10, "Cavalos de Explosão", 1, 1, 'C')

    pdf.cell(63, 10, "Gorduras", 1, 0, 'C')
    pdf.cell(63, 10, "Média", 1, 0, 'C')
    pdf.cell(63, 10, "Cavalos de Resistência", 1, 1, 'C')

    # Texto final
    pdf.ln(10)
    pdf.multi_cell(0, 8, """
Conclusão
A escolha da fonte de energia adequada é essencial para garantir o máximo desempenho...
""", align='J')

    # Salvando o PDF
    pdf.output('Artigo_Qual_a_Melhor_Fonte_de_Energia_Final.pdf')

# Executando o script
if __name__ == '__main__':
    gerar_pdf_artigo()
