print("Tarefa 04 - Aula 12 - Avaliador de Lançamentos Financeiros")

n_total_lancamentos = int(input("Digite o número total de lançamentos financeiros: "))
saldo_final = 0.0 #Acumular valor final após todas as transações
total_receitas = 0.0 #Somar apenas os valores positivos
total_despesas = 0.0 #Somar apenas valores negativos

for i in range(1, n_total_lancamentos + 1):
    valor_transacao = float(input(f"Digite o valor da transação {i} (positivo para receita, negativo para despesa): R$ "))
    if valor_transacao > 0:
        total_receitas += valor_transacao
    else:
        total_despesas += valor_transacao
    saldo_final += valor_transacao
#IF/Else para aplicar Taxa ou Bônus
if saldo_final > 0 and total_receitas > abs(total_despesas) * 2:
    print("Situação Excelente: Bônus de 5% sobre o saldo aplicado.")
    saldo_ajustado = saldo_final * 1.05
elif saldo_final >= 0:
    print("Situação Boa: Sem bônus ou taxa.")
    saldo_ajustado = saldo_final
else:
    print("Situação Ruim: Taxa de serviço de 2% aplicada.")
    saldo_ajustado = saldo_final * 0.98

print("--- Resumo Financeiro ---")
print(f"Total de Receitas: R$ {total_receitas:.2f} \nTotal de Despesas: R$ {total_despesas:.2f} \nSaldo Final ajustado: R$ {saldo_ajustado:.2f}")