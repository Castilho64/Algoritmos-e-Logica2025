#Nome: João Vitor Castilho Mattos
#RA: 0220482523041
print("João Vitor Castilho Mattos, RA: 0220482523041")
print("Questão 01")

p_custo = float(input("Digite o preço de custo do produto R$ "))
p_venda = float(input("Digite o preço de venda do produto R$ "))

lucro = p_venda - p_custo

m_lucro = round((lucro/p_custo) * 100)

if m_lucro > 30:
    print(f"A margem é {m_lucro}% Margem Excelente!")
elif m_lucro >= 10 or m_lucro < 30:
    print(f"A margem é {m_lucro}% Margem Satisfatória.")
else:
    print(f"A margem é {m_lucro}% Margem Baixa: Avaliar preço de venda.")