print("Aula 13 - Atividade 03: Classificador de Temperaturas")
qtd_dias = int(input("Digite a quantidade de dias que serão analisados: "))
soma_das_temperaturas = 0.0

for i in range(1, qtd_dias + 1):
    temp = float(input(f"Informe a temperatura(em °C) do dia {i}: "))
    soma_das_temperaturas += temp

media_temperaturas = soma_das_temperaturas / qtd_dias

#Média das temperaturas
print("--- Média das Temperaturas ---")
if media_temperaturas > 28:
    print(f"A média de temperatura: Clima Quente.")
elif 18 <= media_temperaturas <= 28:
    print(f"A média de temperatura: Clima Agradável.")
else:
    print(f"A média de temperatura: Clima Frio.")

print(f"A média das temperaturas nos {qtd_dias} dias foi de: {media_temperaturas:.2f} °C")