print("Tarefa 04: Calculadora de Temperatura Média - Aula 10")
print("===================================================================")

quant_dias = int(input("Informe a quantidade de dias: "))
soma_temperaturas = 0.0

#Laço de repetição para ler a temperatura de cada dia
for i in range(1, quant_dias + 1):
    temperatura = float(input(f"Informe a temperatura do dia {i}: "))
    soma_temperaturas += temperatura

media_temperatura = soma_temperaturas / quant_dias

#Estrutura IF para classificar o clima
if media_temperatura > 28:
    print("Média de Temperatura: Clima Quente.")
elif 18 <= media_temperatura <= 28:
    print("Média de Temperatura: Clima Agradável.")
else:
    print("Média de Temperatura: Clima Frio.")

print(f"\nMédia de Temperatura foi de {media_temperatura:.2f}°C")
print("===================================================================")