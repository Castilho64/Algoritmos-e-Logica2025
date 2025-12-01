# Nome: João Vitor Castilho Mattos
# RA: 0220482523041
print("Prova 2 - Questão Extra: Coleta e Análise de Dados de Desempenho de Alunos")

# Lista para armazenar todos os alunos e suas notas
dados_brutos = []

# Solicita a quantidade de alunos (máximo sugerido 5)
num_alunos = int(input("Digite o número de alunos a serem registrados (máximo 5): "))

# Coleta dos dados de cada aluno
for i in range(num_alunos):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    nota_trab_pratico = int(input(f"Digite a nota do trabalho prático de {nome}: "))
    nota_prova_teorica = int(input(f"Digite a nota da prova teórica de {nome}: "))
    
    # Armazena tudo em uma lista interna
    dados_brutos.append([nome, nota_trab_pratico, nota_prova_teorica])

# Variáveis para cálculos futuros
soma_medias = 0
alunos_acima_media = 0

# Processamento das notas já coletadas
for dados in dados_brutos:
    nome, nota_trab_pratico, nota_prova_teorica = dados
    
    # Cálculo da média ponderada: 60% prática e 40% teórica
    media = (nota_trab_pratico * 0.6) + (nota_prova_teorica * 0.4)
    soma_medias += media

    # Classificação do desempenho com base na média
    if media > 7:
        alunos_acima_media += 1  # Conta os alunos com ótimo desempenho
        print(f"Aluno: {nome} - Situação: Excelente! Média {media:.2f}")
    elif 5 <= media <= 7:
        print(f"Aluno: {nome} - Situação: Necessita Revisão. Média {media:.2f}")
    else:
        print(f"Aluno: {nome} - Situação: Reprovado. Média {media:.2f}")

# Cálculo da média geral da turma
media_geral = soma_medias / num_alunos

# Resumo final com todos os resultados importantes
print("\n--- Resumo da Análise de Desempenho dos Alunos ---")
print(f"Média Geral da Turma: {media_geral:.2f}. \nTotal de Alunos Acima da Média: {alunos_acima_media}")