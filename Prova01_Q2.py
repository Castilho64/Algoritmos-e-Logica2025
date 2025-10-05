#Nome: João Vitor Castilho Mattos
#RA: 0220482523041
print("João Vitor Castilho Mattos, RA: 0220482523041")
print("Questão 02")

gli_jejum = float(input("Informe o seu nível de glicose em jejum: "))

if gli_jejum < 100:
    print("Glicemia normal.")
elif gli_jejum >= 100 or gli_jejum <= 125:
    print("Pré-diabetes: Risco moderado.")
else:
    print("Diabetes: Nível alto!")