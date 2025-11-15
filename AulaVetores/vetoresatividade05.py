#Criando lista vazia para armazenar as notas
notas = []
#Número de notas a serem inseridas
num_notas = 5

#Primeiro FOR: Leitura e Armazenamento das notas na lista
for i in range(num_notas):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

#Segundo FOR: Exibição Organizada
print("\n--- Lista das Notas --- ")
for i in range(len(notas)):
    print(f"Nota {i + 1}: {notas[i]:.2f}")