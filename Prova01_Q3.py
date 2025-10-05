#Nome: João Vitor Castilho Mattos
#RA: 0220482523041
print("João Vitor Castilho Mattos, RA: 0220482523041")
print("Questão 03")

peso_encom = float(input("Insira o peso da encomenda em KG: "))
dist_entrega = float(input("Insira a distância da entrega  em KM: "))

custo_base = (peso_encom * 1.5)  + (dist_entrega * 0.25)

if custo_base > 200:
    disconto = custo_base - (custo_base * 0.10)
    print(f"O custo base original era de R${custo_base} mas o preço final foi de {disconto}")
elif custo_base >= 50 and custo_base <= 200:
     print(f"O preço final foi de R${custo_base}. Não teve alterações no preço.")
else:
    taxa = custo_base + 5
    print(f"O custo original era de R${custo_base} e foi aplicada uma pequena taxa, o preço final foi de R${taxa}")