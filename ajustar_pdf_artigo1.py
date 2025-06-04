import fitz  # PyMuPDF
import matplotlib.pyplot as plt
import pandas as pd
import os

# Solicitando o caminho do PDF ao usuário
pdf_path = input('Digite o caminho completo do PDF: ').strip()

# Verificando se o PDF existe
if not os.path.exists(pdf_path):
    print(f'ERRO: O arquivo {pdf_path} não foi encontrado.')
    exit()

pdf_document = fitz.open(pdf_path)

# Selecionando a página 3 (índice 2)
page = pdf_document[2]

# Removendo o título duplicado e o texto antigo
for annot in page.annots():
    page.delete_annot(annot)

# Adicionando o texto com fonte azul marinho diretamente sobre a imagem
page.insert_text((50, 100), 'Artigo 1: Qual a Melhor Fonte de Energia para Cavalos Atletas?', fontsize=20, fontname='helv', color=(0, 0, 0.5))

text_content = ('A energia é o combustível que move os cavalos atletas. Cavalos de explosão, como os de corrida, '
                'dependem de carboidratos. Já cavalos de resistência beneficiam-se de gorduras.')
page.insert_textbox(fitz.Rect(50, 140, 550, 220), text_content, fontsize=14, fontname='helv', color=(0, 0, 0.5), align=1)

# Adicionando a tabela em estilo acadêmico
table_text = ('Fonte de Energia | Tipo | Benefício | Modalidade Ideal\n'
              'Milho | Carboidrato | Energia rápida | Corrida e Salto\n'
              'Aveia | Carboidrato | Energia moderada | Provas mistas\n'
              'Óleo de Arroz | Gordura | Energia sustentada | Enduro')
page.insert_textbox(fitz.Rect(50, 240, 550, 320), table_text, fontsize=14, fontname='helv', color=(0, 0, 0.5), align=1)

# Gerando o gráfico em azul marinho brilhante
data = {'Fonte de Energia': ['Milho', 'Aveia', 'Óleo de Arroz'], 'Energia': [80, 60, 90]}
df = pd.DataFrame(data)
plt.figure(figsize=(8, 4))
plt.bar(df['Fonte de Energia'], df['Energia'], color='#000080')
plt.title('Comparativo de Fontes de Energia para Cavalos Atletas', fontsize=14, color='#000080')
plt.xticks(color='#000080')
plt.yticks(color='#000080')
graph_path = 'Grafico_Energia_Cavalos_Atletas.png'
plt.savefig(graph_path, bbox_inches='tight', transparent=True)
plt.close()

# Inserindo o gráfico diretamente sobre a imagem
page.insert_image(fitz.Rect(50, 330, 550, 480), filename=graph_path, overlay=True)

# Salvando o PDF
output_pdf = 'Ebook_Zootecnia_Equina_Artigo1_VSCode_Final_Ajustado.pdf'
pdf_document.save(output_pdf)
pdf_document.close()

print(f'PDF atualizado: {output_pdf}')
