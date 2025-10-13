print("Tarefa 02 - Aula 10: Calculo de Imposto e Taxa sobre Vendas")
print("===================================================================")

quant_dias = int(input("Informe a quantidade de dias para analise: "))
vendas_totais = 0.0

for i in range(1, quant_dias + 1):
    vendas_dia = float(input(f"Informe o valor total de vendas do dia {i}: R$ "))
    vendas_totais += vendas_dia

media_diaria = vendas_totais / quant_dias  # Calculo da media diaria

# Definir imposto fixo
if media_diaria > 1500:
    imposto_fixo = 200.0
else:
    imposto_fixo = 50.0

# Calcular a taxa de serviço sobre o imposto fixo
if vendas_totais > 10000:
    taxa_servico = imposto_fixo * 0.08
else:
    taxa_servico = imposto_fixo * 0.05

valor_liquido = vendas_totais - imposto_fixo - taxa_servico

print("\n=== RESULTADO ===")
print(f"Total de vendas: R$ {vendas_totais:.2f}")
print(f"Imposto fixo: R$ {imposto_fixo:.2f}")
print(f"Taxa de serviço: R$ {taxa_servico:.2f}")
print(f"Valor líquido: R$ {valor_liquido:.2f}")

print("===================================================================")