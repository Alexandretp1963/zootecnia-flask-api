# Remover emojis para evitar erro de codificação
def remove_emojis(text):
    return text.encode("ascii", "ignore").decode("ascii")

pdf = RoteiroPDF()
pdf.add_page()

pdf.section_title(remove_emojis("🎬 Introdução"))
pdf.section_body(remove_emojis(
    "Olá, seja muito bem-vindo ao canal Zootecnia Equina com Alexandre.\n"
    "Eu sou Alexandre Trindade, zootecnista com especializações em nutrição animal, equinocultura e reprodução de equinos, "
    "e criei este espaço para compartilhar conhecimento prático sobre manejo, nutrição e gestão de cavalos — sempre com foco em resultado no campo."
))

pdf.section_title(remove_emojis("🎯 Parte 1 – Quem sou eu e o que você vai encontrar aqui"))
pdf.section_body(remove_emojis(
    "Ao longo da minha trajetória, trabalhei com criação, alimentação e reprodução de cavalos de alto desempenho, incluindo provas como o Freio de Ouro, Paleteada, Corridas e Salto.\n"
    "Aqui no canal, você vai encontrar:\n"
    "- Dicas diretas sobre alimentação e suplementos\n"
    "- Manejo de éguas em reprodução\n"
    "- Avaliações técnicas para melhorar o desempenho dos animais\n"
    "- E conteúdos voltados para quem quer fazer uma zootecnia de verdade, com qualidade e resultado."
))

pdf.section_title(remove_emojis("✅ Parte 2 – Dica prática: Qual a melhor fonte de energia para cavalos atletas?"))
pdf.section_body(remove_emojis(
    "Vamos começar com uma dica rápida:\n"
    "Muita gente pergunta se é melhor usar milho, aveia, óleo ou ração pronta. A verdade é que depende do tipo de trabalho do cavalo.\n"
    "Se for um cavalo de explosão, como o de corrida, o carboidrato de rápida digestão é fundamental — como milho e aveia.\n"
    "Se for um cavalo de resistência, como na paleteada ou enduro, o ideal é equilibrar com gorduras de boa qualidade, como óleo vegetal (soja, arroz, canola).\n"
    "Mas sempre com acompanhamento técnico — porque energia demais pode causar cólicas, acidose e laminites."
))

pdf.section_title(remove_emojis("📣 Encerramento"))
pdf.section_body(remove_emojis(
    "Gostou da dica? Então curte o vídeo, se inscreve no canal e ativa o sininho.\n"
    "Toda semana eu vou trazer conteúdo prático e direto do campo, pra você aplicar aí na sua criação.\n"
    "E se quiser uma consultoria personalizada, me chama no WhatsApp que está aqui na descrição.\n"
    "Até a próxima!"
))

# Salvar PDF
pdf_path = "/mnt/data/Roteiro_Video1_ZootecniaEquina_Alexandre.pdf"
pdf.output(pdf_path)
