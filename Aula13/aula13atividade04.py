print("Aula 13 - Atividade 04: Simulação de Produção e Venda com Dupla Análise.")

#Primeira parte: Simulação da Produção(Geração dos Dados)
n_lotes_prod = int(input("Digite o número de lotes a serem simulados: "))
custo_fixo = 100.00 #Custo Fixo por Lote R$100,00
lista_custos_por_lote = []

for i in range(1, n_lotes_prod + 1):
    n_unidades_prod = int(input(f"Informe o número de Unidades Produzidas no lote {i}: "))
    #Estrura IF para determinar o Custo Variável por Unidade (c_var_unid)
    if n_unidades_prod > 50:
        c_var_unid = 1.50 #Custo Variável por Unidade R$1,50
    elif 20 <= n_unidades_prod <= 50:
        c_var_unid = 2.00 #Custo Variável por Unidade R$2,00
    else:
        c_var_unid = 3.00 #Custo Variável por Unidade R$3,00
    custo_lote = custo_fixo + (n_unidades_prod * c_var_unid)
    lista_custos_por_lote.append(custo_lote)

# Segunda Parte: Análise da Venda e Classificação (Processamento dos Dados Gerados)
preco_base_venda = 5.00  # Preço Base de Venda por Unidade R$5,00
lucro_total_acumulado = 0.00
lotes_com_lucro_alto = 0 

for i in range(1, n_lotes_prod + 1):
    custo_lote = lista_custos_por_lote[i - 1]
    n_unidades_vend = int(input(f"Informe o número de Unidades Vendidas do lote {i}: "))
    receita_venda = n_unidades_vend * preco_base_venda
    
    n_unidades_prod = int(input(f"Informe novamente o número de Unidades Produzidas no lote {i} (para cálculo do custo unitário): "))
    custo_unitario = custo_lote / n_unidades_prod
    lucro = (preco_base_venda - custo_unitario) * n_unidades_vend
    
    lucro_total_acumulado += lucro
    
    if lucro > 100.00:  # Se o Lucro for maior que R$100,00
        lotes_com_lucro_alto += 1
        print(f"Lote {i} Aprovado: Lucro Alto.")
    elif lucro > 0.00:  # Se o Lucro for maior que R$0,00
        print(f"Lote {i} Aceitável: Lucro Mínimo.")
    else:  # Se o Lucro for menor ou igual a R$0,00
        print(f"Lote {i} Rejeitado: Prejuízo.")
#Resultados Finais
print("---- Resultados Finais ----")
print(f"Lucro Total Acumulado R${lucro_total_acumulado:.2f} \nQuantidade de Lotes com Lucro Alto: {lotes_com_lucro_alto}")