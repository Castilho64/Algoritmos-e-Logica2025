print("Tarefa 01: Jogo de Advinhar o Número")

import random

numero_secreto =  random.randint(1, 10)#Gera um número aleatório entre 1 e 10
acertou = False
tentativas = 0

while not acertou:
    palpite = int(input("Digite um número entre 1 e 10: "))
    tentativas += 1

    if palpite == numero_secreto:
        acertou = True
        print("Parabéns você acertou!")
    elif palpite > numero_secreto:
        print("Seu paplpite foi muito alto. Tente um número menor.")
    else:
        print("Seu palpite foi muito baixo. Tente um número maior.")

print(f"O número secreto era {numero_secreto}. Você acertou em {tentativas} tentativas.")