print("Tarefa 02 - Aula 12 - Análise de Desempenho de Time")

n_dias = int(input("Digite o número de dias analisados: "))
producao_total = 0
dias_acima_meta = 0

print("Lembrete - Média Diária: 50 Unidades")
for i in range(1, n_dias + 1):
    meta_diaria = 50
    prod_dia = int(input(f"Digite a produção do dia {i}: "))
    producao_total += prod_dia
    if prod_dia >= meta_diaria:
        dias_acima_meta += 1

#Cálculos e Decisões Finais
media_diaria = producao_total / n_dias

#IF/Else para Determinar o bônus
if  media_diaria > 60 and dias_acima_meta >= 4:
    print("Bônus Máximo! (15% sobre a produção total.)")
    bonus =  producao_total * 0.15
elif media_diaria >= 50 or dias_acima_meta >= 3:
    print("Bônus Parcial! (5% sobre a produção toal.)")
    bonus = producao_total * 0.05
else:
    print("Sem Bônus. Metas de produtividade não foram atingidas.")
    bonus = 0

print("--- Resumo da Análise ---")
print(f"Média Diária de Prodcução: {media_diaria:.2f} unidades. \nValor Final do Bônus: R$ {bonus:.2f}")