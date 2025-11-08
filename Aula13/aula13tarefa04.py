print("Tarefa 04: Somatória Separada de Pares e Ímpares até o Zero")

cont_pares = 0
cont_impares = 0
numero_digitado = 1  # Inicializa com um valor diferente de zero para entrar no loop

while numero_digitado != 0:
    numero_digitado = int(input("Digite um número inteiro (0 para encerrar): "))
    if numero_digitado != 0 and numero_digitado % 2 == 0:
        cont_pares += numero_digitado
        print(f"Número {numero_digitado} é par. Continuando..")
    else: #Se for ímpar e diferente de zero
        cont_impares += numero_digitado
        print(f"Número {numero_digitado} é ímpar. Continuando..")
print(f"Números pares digitados: {cont_pares}. \nNúmeros ímpares digitados: {cont_impares}.")