#Nome: João Vitor Castilho Mattos
#RA: 0220482523041


print("João Vitor Castilho Mattos, RA: 0220482523041")
print("Questão 07")

p_lote = float(input("Informe a pureza do lote (ex: 0.95 para 95%):"))
m_total = float(input("Informe a massa total (em KG): "))
taxa_cont = float(input("Informe a taxa de contaminação (ex: 0.02 para 2%): "))

fd = (p_lote * 100) - (taxa_cont * 50)
if m_total > 1000:
    p_base = 10
else:
    p_base = 12.50

if fd > 90 and p_lote > 0.98:
    print("Classificação: PREMIUM (Venda Imediata).")
    p_final_kg = round(p_base * 1.50)
elif fd >= 70 and fd <= 90 and taxa_cont < 0.05:
    print("Classificação: PADRÃO (Venda Normal).")
    p_final_kg = round(p_base * 1.10)
elif fd < 70 or  p_lote < 0.90:
    print("Classificação: REPROVADO (Descarte ou Re-processamento).")
    p_final_kg = round(p_base * 0.25)
else:
    print("Classificação: ACEITÁVEL (Margem Mínima).")
    p_final_kg = round(p_base * 0.90)

preco_total_final = round(p_final_kg * m_total)
print(f"O preço total final foi de R${preco_total_final} e o preço base por KG foi de R${p_final_kg}")