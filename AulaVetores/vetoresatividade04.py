# Definição do tamnho do vetor
tamanho = 5

# 1 - Pré-alocação do vetor (reserva 5 espaços, inicializando em 0.0)
vetor_notas = [0.0] * tamanho
soma_notas = 0.0 # Acumulador para soma das notas
media = 0.0 # Variável para armazenar a média

print("--- Entrada de Notas ---")

#Primeiro For: Coleta e Atribuição por índice
#O laço itera de 0 até 4, que são os índices válidos
for i in range(tamanho):
    #Solicitamos a nota. Usamos i + 1 apenas para exibir Nota 01, Nota 02 etc.
    nota = float(input(f"Digite a nota {i + 1}: "))

    #Atribuímos diretamente ao índice, como em C/Java: vetor[i] = valor
    vetor_notas[i] = nota

print("\n--- Processamento das Notas ---")

#Segundo For: Soma e Acumulação ( Percorrendo o vetor)
#Usamos o índice 'i' para garantir que percorremos as 5 posições
for i in range(tamanho):
    soma_notas += vetor_notas[i] #Acessamos o elemento pelo índice e somamos ao acumulador

#2 - Cáculo Final da Média
if tamanho > 0:
    media = soma_notas /  tamanho

#3 - Exibição dos Resultados
print(f"\nVetor de Notas Registrados: {vetor_notas}. \nSoma Total das Notas: {soma_notas:.2f} \nMédia Final da Turma: {media:.2f}")