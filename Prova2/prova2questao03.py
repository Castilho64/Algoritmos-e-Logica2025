# Nome: João Vitor Castilho Mattos
# RA: 0220482523041
print("Prova 2 - Questão 03: Avaliação de Renda e Classificação de Status")

nomes = []
rendas = []
status_aprovacao = []
rendas_aprovadas = []
# Loop de registro
while True:
    nome = input("Digite o nome do indivíduo (ou 'fim' para encerrar): ")
    if nome.lower() == "fim":
        break
    renda = float(input(f"Digite a renda mensal de {nome} em R$ "))
    nomes.append(nome)
    rendas.append(renda)
    # Classificação
    if renda > 2500:
        status_aprovacao.append("Aprovado")
        rendas_aprovadas.append(renda)
    else:
        status_aprovacao.append("Reprovado")
# Impressão dos resultados individuais
for i in range(len(nomes)):
    print(f"{nomes[i]} - Renda: R$ {rendas[i]:.2f} - Status: {status_aprovacao[i]}")
# Cálculo da média dos aprovados, se houver
if len(rendas_aprovadas) > 0:
    media = sum(rendas_aprovadas) / len(rendas_aprovadas)
else:
    media = 0
# Resumo
print("\n--- Resumo da Avaliação de Renda ---")
print(f"Nomes: {nomes}. \nStatus de Aprovação: {status_aprovacao}. \nMédia das Rendas dos Aprovados: R$ {media:.2f}")