# Nome: João Vitor Castilho Mattos
# RA: 0220482523041
print("Prova 2 - Questão 02: Análise de Temperaturas Críticas")

registros_temperaturas = []
dias_criticos = 0

temperatura = float(input("Digite a temperatura em Celsius/Cº (0 para encerrar): "))

# Loop de registro das temperaturas
while temperatura != 0:
    print(f"Temperatura registrada: {temperatura}Cº")
    registros_temperaturas.append(temperatura)

    temperatura = float(input("Digite a temperatura em Celsius/Cº (0 para encerrar): "))

# Análise dos dias
for i in range(len(registros_temperaturas)):
    if registros_temperaturas[i] > 30:
        print(f"Dia {i + 1}: Alerta Dia Quente!")
        dias_criticos += 1
    elif registros_temperaturas[i] < 10:
        print(f"Dia {i + 1}: Alerta Dia Frio!")
        dias_criticos += 1
    else:
        print(f"Dia {i + 1}: Temperatura Agradável.")

print("\n--- Resumo das Temperaturas Registradas ---")
print(f"Temperaturas registradas: {registros_temperaturas}")
print(f"Total de Dias Críticos: {dias_criticos}")