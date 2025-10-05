print("Tarefa 02 - Aula 09 - Laços de Repetição")

# Programa que imprime os quadrados dos números de 1 a 10
# e informa se o resultado é par ou ímpar

for numero in range(1, 11):
    quadrado = numero ** 2  # calcula o quadrado do número
    if quadrado % 2 == 0:
        tipo = "par"
    else:
        tipo = "ímpar"
    print(f"O quadrado de {numero} é {quadrado} e é {tipo}.")

#O que é um laço de repetição FOR
# Um laço de repetição FOR é utilizado para iterar sobre uma sequência (como uma lista, tupla ou string)
# ou um intervalo de números. Ele permite executar um bloco de código várias vezes de forma
# controlada e é especialmente útil quando se sabe o número de iterações com antecedência.