# Recriando o E-book completo corretamente, com as imagens aplicadas corretamente sem opacidade
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Capa do E-book (Imagem nítida)
pdf.add_page()
pdf.image('/mnt/data/A_traditional_pencil_or_charcoal_illustration_depi.png', x=0, y=0, w=210, h=297)
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

# Sumário (Imagem suave)
pdf.add_page()
pdf.image('/mnt/data/A_traditional_pencil_or_charcoal_illustration_depi.png', x=0, y=0, w=210, h=297)
pdf.set_font("Arial", 'B', 18)
pdf.multi_cell(0, 10, "\n\n\n\nSumário", align="C")
pdf.set_font("Arial", '', 14)
pdf.multi_cell(0, 10, "\n1. Introdução.......................................................3")
pdf.multi_cell(0, 10, "2. Artigo 1: Qual a Melhor Fonte de Energia para Cavalos Atletas?....4")
pdf.multi_cell(0, 10, "3. Importância da Suplementação Mineral.....................7")
pdf.multi_cell(0, 10, "4. Estratégias de Manejo Nutricional para Cavalos Idosos...10")
pdf.multi_cell(0, 10, "5. Conclusão......................................................13")
pdf.multi_cell(0, 10, "6. Referências...................................................14")

# Artigo 1 - Fonte de Energia (Imagem de fundo e tabela)
pdf.add_page()
pdf.image('/mnt/data/A_digital_illustration_in_sepia_tones_showcases_a_.png', x=0, y=0, w=210, h=297)
pdf.set_font("Arial", 'B', 16)
pdf.multi_cell(0, 10, "Artigo 1: Qual a Melhor Fonte de Energia para Cavalos Atletas?")
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 10, """
Introdução:
A escolha da fonte de energia é fundamental para o desempenho dos cavalos atletas. Cavalos de explosão,
como os de corrida, dependem de carboidratos. Já cavalos de resistência beneficiam-se de gorduras.
""")
pdf.multi_cell(0, 10, "\nTabela: Fontes de Energia para Cavalos Atletas")
pdf.multi_cell(0, 10, "Fonte de Energia | Tipo | Benefício | Modalidade Ideal")
pdf.multi_cell(0, 10, "Milho             | Carboidrato | Energia rápida | Corrida e Salto")
pdf.multi_cell(0, 10, "Aveia             | Carboidrato | Energia moderada | Provas mistas")
pdf.multi_cell(0, 10, "Óleo de Arroz     | Gordura     | Energia sustentada | Enduro")
pdf.image('/mnt/data/graph_energy_distribution.png', x=40, y=140, w=130)

# Artigo 2 - Suplementação Mineral (Imagem de fundo e tabela)
pdf.add_page()
pdf.image('/mnt/data/A_monochromatic_digital_illustration_of_a_horse_sl.png', x=0, y=0, w=210, h=297)
pdf.set_font("Arial", 'B', 16)
pdf.multi_cell(0, 10, "Artigo 2: Importância da Suplementação Mineral para Cavalos em Trabalho")
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 10, """
Introdução:
Os minerais são essenciais para a saúde e desempenho dos cavalos. Garantem o equilíbrio e a saúde óssea.
""")
pdf.multi_cell(0, 10, "\nTabela: Minerais Essenciais e Suas Funções")
pdf.multi_cell(0, 10, "Mineral   | Função Principal          | Consequência da Deficiência")
pdf.multi_cell(0, 10, "Cálcio    | Formação óssea            | Osteoporose")
pdf.multi_cell(0, 10, "Fósforo   | Equilíbrio ósseo          | Desmineralização")
pdf.multi_cell(0, 10, "Magnésio  | Contração muscular        | Espasmos")
pdf.multi_cell(0, 10, "Eletrólitos| Hidratação               | Fadiga")
pdf.image('/mnt/data/graph_minerals.png', x=40, y=150, w=130)

# Artigo 3 - Manejo para Cavalos Idosos (Imagem de fundo e tabela)
pdf.add_page()
pdf.image('/mnt/data/24d2faaa-119e-49e3-ba28-9f9b2dfb6d8b.png', x=0, y=0, w=210, h=297)
pdf.set_font("Arial", 'B', 16)
pdf.multi_cell(0, 10, "Artigo 3: Estratégias de Manejo Nutricional para Cavalos Idosos")
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 10, """
Introdução:
Cavalos idosos necessitam de cuidados nutricionais especiais. Fibras digestíveis, vitaminas e controle
de peso são fundamentais.
""")
pdf.multi_cell(0, 10, "\nTabela: Manejo Nutricional para Cavalos Idosos")
pdf.multi_cell(0, 10, "Estratégia                  | Descrição")
pdf.multi_cell(0, 10, "Fibras de Alta Digestibilidade | Feno de alfafa e polpa de beterraba")
pdf.multi_cell(0, 10, "Suplementação de Vitaminas | Vitaminas A, E e C")
pdf.multi_cell(0, 10, "Controle de Peso           | Dieta balanceada e exercícios leves")
pdf.image('/mnt/data/graph_senior_care.png', x=40, y=150, w=130)

# Conclusão e Referências (Imagem suave)
pdf.add_page()
pdf.image('/mnt/data/A_traditional_pencil_or_charcoal_illustration_depi.png', x=0, y=0, w=210, h=297)
pdf.set_font("Arial", 'B', 16)
pdf.multi_cell(0, 10, "Conclusão")
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 10, """
A nutrição é a base do desempenho e da saúde dos cavalos. Com o conhecimento adequado, é possível
garantir que cada cavalo atinja seu potencial máximo.
""")

# Referências
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
pdf_output = "/mnt/data/E-book_Zootecnia_Equina_Completo_Ajustado_Final_V2.pdf"
pdf.output(pdf_output)

pdf_output
