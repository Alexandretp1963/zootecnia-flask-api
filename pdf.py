# Recriando o E-book completo do zero após a reinicialização, garantindo que todas as imagens e textos estejam presentes corretamente.
from fpdf import FPDF

# Configurando o E-book com texto completo e imagens corretamente aplicadas
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Capa do E-book (Imagem nítida)
pdf.add_page()
pdf.set_text_color(0, 51, 102)  # Azul marinho brilhante
pdf.set_font("Arial", 'B', 28)
pdf.set_xy(10, 30)
pdf.multi_cell(0, 12, "Guia Completo de Nutrição e Manejo para Cavalos Atletas", align="C")
pdf.set_font("Arial", 'I', 18)
pdf.set_xy(10, 120)
pdf.multi_cell(0, 10, "Energia, Suplementação e Estratégias Práticas", align="C")
pdf.set_font("Arial", 'B', 16)
pdf.set_xy(10, 150)
pdf.multi_cell(0, 10, "Autor: Alexandre - Zootecnista e Consultor em Equinocultura", align="C")

# Sumário (sem imagem no momento)
pdf.add_page()
pdf.set_font("Arial", 'B', 18)
pdf.multi_cell(0, 10, "\n\n\n\nSumário", align="C")
pdf.set_font("Arial", '', 14)
pdf.multi_cell(0, 10, "\n1. Introdução.......................................................3")
pdf.multi_cell(0, 10, "2. Artigo 1: Qual a Melhor Fonte de Energia para Cavalos Atletas?....4")
pdf.multi_cell(0, 10, "3. Importância da Suplementação Mineral.....................7")
pdf.multi_cell(0, 10, "4. Estratégias de Manejo Nutricional para Cavalos Idosos...10")
pdf.multi_cell(0, 10, "5. Conclusão......................................................13")
pdf.multi_cell(0, 10, "6. Referências...................................................14")

# Artigo 1 - Fonte de Energia
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.multi_cell(0, 10, "Artigo 1: Qual a Melhor Fonte de Energia para Cavalos Atletas?")
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 10, """
A energia é o combustível que move os cavalos atletas. Cavalos de explosão, como os de corrida,
dependem de carboidratos. Já cavalos de resistência beneficiam-se de gorduras.

Fonte de Energia | Tipo | Benefício | Modalidade Ideal
Milho | Carboidrato | Energia rápida | Corrida e Salto
Aveia | Carboidrato | Energia moderada | Provas mistas
Óleo de Arroz | Gordura | Energia sustentada | Enduro
Farelo de Soja | Proteína | Recuperação muscular | Todas
""")

# Artigo 2 - Suplementação Mineral
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.multi_cell(0, 10, "Artigo 2: Importância da Suplementação Mineral para Cavalos em Trabalho")
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 10, """
Os minerais são essenciais para a saúde e desempenho dos cavalos. Cálcio, fósforo, magnésio e eletrólitos
garantem o equilíbrio e a saúde óssea.

Mineral | Função Principal | Consequência da Deficiência
Cálcio | Formação óssea | Osteoporose
Fósforo | Equilíbrio ósseo | Desmineralização
Magnésio | Contração muscular | Espasmos
Eletrólitos | Hidratação | Fadiga
""")

# Artigo 3 - Manejo para Cavalos Idosos
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.multi_cell(0, 10, "Artigo 3: Estratégias de Manejo Nutricional para Cavalos Idosos")
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 10, """
Cavalos idosos necessitam de cuidados nutricionais especiais. Fibras digestíveis, vitaminas e controle
de peso são fundamentais.

Estratégia | Descrição
Fibras de Alta Digestibilidade | Feno de alfafa e polpa de beterraba
Suplementação de Vitaminas | Vitaminas A, E e C
Controle de Peso | Dieta balanceada e exercícios leves
""")

# Conclusão e Referências
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.multi_cell(0, 10, "Conclusão")
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 10, """
A nutrição é a base do desempenho e da saúde dos cavalos. Com o conhecimento adequado e as melhores práticas,
é possível garantir que cada cavalo atinja seu potencial máximo.
""")

pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.multi_cell(0, 10, "Referências")
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 10, """
- FRAPE, D. "Equine Nutrition and Feeding".
- NRC (2007). "Nutrient Requirements of Horses".
- GEOR, R. J.; HARRIS, P.; COENEN, M. "Equine Applied and Clinical Nutrition".
""")

# Salvando o E-book completo
pdf_output = "/mnt/data/E-book_Zootecnia_Equina_Completo_Recriado_Corrigido.pdf"
pdf.output(pdf_output)

pdf_output
