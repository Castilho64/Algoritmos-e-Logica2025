#Nome: João Vitor Castilho Mattos
#RA: 0220482523041


print("João Vitor Castilho Mattos, RA: 0220482523041")
print("Questão 06")

r_invest = float(input("Digite o retorno do investimento R$"))
r_livre = float(input("Digite a taxa livre de risco: "))
sigma = float(input("Informe o desvio-padrão da volatilidade: "))

if sigma == 0:
    print("Informe uma valor maior que 0")
else:
    sharp = round((r_invest - r_livre) / sigma)

spread = r_invest - r_livre

if sharp > 1.5 and spread > 0.05:
    classificacao = "Investimento Excelente: Alta performance ajustada ao risco."
elif sharp >= 0.5 and sharp <= 1.5 or spread > 0.02:
    classificacao = "Investimento Bom: Risco e retorno moderados."
elif sharp < 0.5 and r_invest > 0:
    classificacao = "Investimento Aceitável: Retorno positivo, mas risco alto para o ganho."
else: 
    classificacao = "Investimento Ruim: Não recomendado"

print(f"O valor do Sharp Ratio foi de: {sharp} e sua classificação foi de {classificacao}")