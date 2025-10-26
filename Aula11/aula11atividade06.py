print("Atividade 06 - Aula 11")

custo_fixo = 500.00
custo_materia_prima = float(input("Informe o custo da matéria-prima por item R$"))

for i in range(100):
    desperdicio_material = custo_materia_prima - (0.05*100)
    custo_variavel = custo_materia_prima + desperdicio_material

custo_total_prod = custo_fixo + custo_variavel
if custo_total_prod < 3000:
    margem = 0.35
elif 5000 < custo_total_prod > 3000:
    margem = 0.20
else: 
    margem = 0.15

preco_minimo = (custo_total_prod/100) * (1 + margem)

print(f"O Custo Total de Produção foi de R${custo_total_prod} \nA Margem de Lucro Aplicada foi de {margem * 100}% \nE o Preço Mínimo de Venda por Item R${(preco_minimo):.2f}")