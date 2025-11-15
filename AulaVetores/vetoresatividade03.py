# Declaração da lista (vetor) para armazenar os nomes das cidades
cidades = []
# Definição da constante com número de cidades
NUM_CIDADES = 5

# Primeiro FOR: Leitura e Armazenamento das cidades
for i in range(NUM_CIDADES):
    nome = input(f"Digite o nome da cidade {i + 1}: ")
    cidades.append(nome)

# Segundo FOR: Exibição e Transformação para maicúsculas
print("\n--- Cidades em letras maiúsculas ---")
for i in range(len(cidades)):
    cidade_maiscula = cidades[i].upper()
    print(f"Cidade {i + 1}: {cidade_maiscula}")