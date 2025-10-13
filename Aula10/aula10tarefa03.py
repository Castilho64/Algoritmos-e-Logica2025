print("Tarefa 03: Controle de Gastos com Combustível - Aula 10")
print("===================================================================")

quant_dias = int(input("Informe a quantidade em que houve viagem: "))
total_km_percorridos = 0.0

for i in range(1, quant_dias + 1):
    km_percorridos = float(input(f"Informe a quantidade de KM percorridos no dia {i}: "))
    total_km_percorridos += km_percorridos

#Calcular os litros consumidos(considerando que o carro faz 12km/litro)
litros_consumidos = total_km_percorridos / 12

#Calcular o gasto total com combustivel
custo_total = litros_consumidos * 4.80

if custo_total > 500:
    print(f"Alerta de Gastos: O custo total com combustível foi alto!")

else:
    print(f"O Gasto sob controle: O custo com combustível foi baixo/moderado.")

print(f"\n Você percorreu um total de {total_km_percorridos:.2f} KM.")
print(f"Você consumiu um total de {litros_consumidos:.2f} litros de combustível.")
print(f"O custo total com combustível foi de R$ {custo_total:.2f}.")

print("===================================================================")