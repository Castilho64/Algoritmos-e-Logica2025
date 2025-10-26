print("Atividade 04 - Aula 11")

total_meses = int(input("Informe o número total de meses para análise: "))

consumo_total_kwh = 0
valor_total_pago = 0

for i in range(1, total_meses + 1):
    consumo_kwh = float(input(f"Informe o consumo de kWh do mês {i}: "))
    
    if consumo_kwh <= 100:
       custo_mensal = consumo_total_kwh + consumo_kwh * 0.55
    elif 200<= consumo_kwh > 100:
        custo_mensal = consumo_total_kwh + consumo_kwh * 0.70
    else:
        custo_mensal = consumo_total_kwh + consumo_kwh * 0.95

consumo_total_kwh += consumo_kwh
valor_total_pago += custo_mensal

media_mensal = consumo_total_kwh / total_meses

if media_mensal > 180:
    print("Alerta! O consumo médio está elevado. Sugerir medidas de economia.")
else:
    print("Consumo médio dentro dos limites normais.")

print(f"O Consumo Total em kWh foi de {consumo_total_kwh} \nO Valor Total Pago foi de R${round(valor_total_pago)}")