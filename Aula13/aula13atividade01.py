print("Aula 13 - Atividade 01: Classificador de Desempenho de Vendedores com Bônus Condicional")

n_vendedores = int(input("Digite o número de vendedores a serem avaliados: "))
bonus_vendedor = 500.0 #Valor fixo do bônus por vendedor
pont_total_equipe = 0.0 #Pontuação total da equipe
vendedores_acima_meta = 0 #Contador de vendedores que atingiram a meta
botoes_alerta_ativados = 0 #Contador para vendedores com desempenho muito baixo

for i in range(1, n_vendedores + 1):
    pont_final_vendas = float(input(f"Informe a pontuação final de vendas do vendedor {i}(0 a 100): "))
    pont_total_equipe += pont_final_vendas

    #Classificar e contabilizar o desempenho individual
    if pont_final_vendas >= 90:
        vendedores_acima_meta += 1
    elif pont_final_vendas < 50:
        botoes_alerta_ativados += 1

#Cálculo de Bônus da Equipe
media_equipe = pont_total_equipe / n_vendedores
bonus_base_total = n_vendedores * bonus_vendedor

#Fator de Multiplicação do Bônus(FMB)
if media_equipe > 80 and botoes_alerta_ativados == 0:
    fmb = 1.2 #20% de bônus
elif vendedores_acima_meta > (n_vendedores / 2) or 70 <= media_equipe < 80:
    fmb = 1.05 #5% de bônus
else:
    fmb = 1.00 #Sem bônus adicional

#Calcular o Valor Final a Pagar
valor_final_total = bonus_base_total * fmb

print("---Resumo do Desempenho da Equipe---")
print(f"Média de Pontuação da Equipe: {media_equipe:.2f} \nNúmero de Alertas: {botoes_alerta_ativados} \nValor Final a pagar R${valor_final_total:.2f}")