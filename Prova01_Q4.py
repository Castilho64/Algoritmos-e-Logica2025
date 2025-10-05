#Nome: João Vitor Castilho Mattos
#RA: 0220482523041
print("João Vitor Castilho Mattos, RA: 0220482523041")
print("Questão 04")

p = float(input("Digite o valor inicial de investimento R$ "))
t = int(input("Digite o prazo do investimento (em Meses): "))

if t < 6:
    j = t * 0.005

elif t >= 6 and t <= 12:
    j = t * 0.008

else: 
    j = t * 1.2

r_total = p * j * t
print(f"A taxa de juros aplicada foi de R${j} e o rendimento total obtido foi de R${r_total}")