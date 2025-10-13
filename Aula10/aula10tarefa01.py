print("Tarefa 01 - Aula 10: Calcular o imposto a pagar com base no total das notas fiscais")
print("===================================================================")

quantidade_notas = int(input("Digite a quantidade de notas fiscais: "))

soma_das_notas = 0.0

for i in range(1, quantidade_notas + 1):
    valor_nota = float(input(f"Digite o valor da nota fiscal {i}: R$ "))
    soma_das_notas += valor_nota

# 4. Determina a alíquota com base na soma das notas
if soma_das_notas <= 100:
    aliquota = 0.05
elif soma_das_notas <= 4999.99:
    aliquota = 0.08
elif soma_das_notas <= 14999.99:
    aliquota = 0.12
else:
    aliquota = 0.16

# 5. Calcula o imposto
valor_imposto = soma_das_notas * aliquota

# 6. Exibe o resultado
print("\n=== RESULTADO ===")
print(f"Total das notas fiscais: R$ {soma_das_notas:.2f}")
print(f"Alíquota aplicada: {aliquota * 100:.0f}%")
print(f"Valor do imposto a ser pago: R$ {valor_imposto:.2f}")

print("===================================================================")