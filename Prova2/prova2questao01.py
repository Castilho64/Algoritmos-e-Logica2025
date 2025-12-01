# Nome: João Vitor Castilho Mattos
# RA: 0220482523041
print("Prova 2 - Questão 01: Calculadora de Gastos Interativa")

gastos_semanais = []
continuar = "sim"

while continuar.lower() == "sim":
    gasto = float(input("Digite o valor do gasto semanal R$ "))
    gastos_semanais.append(gasto)

    # Validação de sim/não
    continuar = input("Deseja adicionar outro gasto? (sim/não): ").lower()
    while continuar not in ["sim", "não"]:
        print("Opção inválida! Digite apenas 'sim' ou 'não'.")
        continuar = input("Deseja adicionar outro gasto? (sim/não): ").lower()

# Soma total usando FOR
soma = 0
for gasto in gastos_semanais:
    soma += gasto

print("\n--- Resumo dos Gastos Semanais ---")
print(f"Gastos Semanais: {gastos_semanais}")
print(f"Total gasto nas semanas: R$ {soma:.2f}")