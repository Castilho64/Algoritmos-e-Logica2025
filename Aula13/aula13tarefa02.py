print("Tarefa 02: Somatória de Pares até o Zero")

somas_pares = 0
numero_digitado = 1  # Inicializa com um valor diferente de zero para entrar no loop

while numero_digitado != 0:
    numero_digitado = int(input("Digite um número inteiro (0 para encerrar): "))
    if numero_digitado != 0 and numero_digitado % 2 == 0:
        somas_pares += numero_digitado
    else: #Se o número for ímpar ou zero
        print("Número ímpar será ignorado e zero (0) encerrará o programa.")

print(f"A soma total dos números pares digitados é: {somas_pares}")