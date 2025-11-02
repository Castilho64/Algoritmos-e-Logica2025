print("Aula 13 - Atividade 02: Análise de Lote de Peças com Classificação de Erros")

total_pecas = int(input("Digite o número total de peças produzidas no lote: "))
custo_fixo_inpecao =  150.00
custo_retrabalho = 50.00 #Custo de Retrabalho por peça com Erro Crítico
erros_criticos = 0
erros_leves = 0
custo_variavel_rejeicao = 0.00 #Acumulador para custo total de peças rejeitadas

for i in range(1, total_pecas + 1):
    nivel_defeito = int(input(f"Informe o nível de defeito da peça {i}(0 a 10): "))
    if nivel_defeito > 8:
        erros_criticos += 1
        custo_variavel_rejeicao += custo_retrabalho
    elif 3 <= nivel_defeito <= 8:
        erros_leves += 1
    else:
        print("Peça aprovada sem defeitos.")

#Cálculos e Decisões Finais
taxa_rejeicao_total = (erros_criticos / total_pecas) * 100
custo_final_total = custo_fixo_inpecao + custo_variavel_rejeicao

#Classificar resultado do lote
if taxa_rejeicao_total > 10 and erros_leves > 5: #Taxa de rejeiçaõ maior que 10% E mais de 5 erros leves
    print("Lote Reprovado! Alta taxa de defeito e muitos erros leves.")
    lote = "Reprovado"
elif erros_criticos > 2 or taxa_rejeicao_total > 20: #Mais de 2 erros críticos OU taxa de rejeição maior que 20%
    print("Lote Crítico! Necessário reavaliação total.")
    lote = "Crítico"
else:
    print("Lote Aprovado! Custos sob controle.")
    lote = "Aprovado"

print("--- Resumo da Inspeção ---")

print(f"Taxa de Rejeição Total: {taxa_rejeicao_total:.2f}% \nCusto Final Total da Inspeção: R$ {custo_final_total:.2f} \nClassificação do Lote {lote}.")