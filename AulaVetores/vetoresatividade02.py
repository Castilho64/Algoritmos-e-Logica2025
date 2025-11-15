# Criando vetor com um tamanho fixo
tamanho_vetor = 5
# Iniciando com 5 posições com strings vazias para reservar espaço
vetor_nomes =[""] * tamanho_vetor

print("--- Entrada de Nomes ---")

# Primeiro FOR: Leitura e Atribuição por Índice
for i in range(tamanho_vetor):
    nome = input(f"Digite o nome {i + 1}: ")# Solicitando o nome
    vetor_nomes[i] = nome

print("\n--- Nomes Digitados ---")
print("Os nomes registrados, acessados por índice:")

# Segundo FOR: Exibição e Processamento por Índice
for i in range(tamanho_vetor):
    nome_atual = vetor_nomes[i]

    print(vetor_nomes[i]) # Exibindo o nome