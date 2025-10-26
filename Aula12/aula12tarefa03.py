print("Tarefa 03 - Aula 12 - Avaliação de Estoque com Fator de Risco")

n_produtos = int(input("Digite o número de produtos a serem avaliados: "))
valor_total_estoque = 0.0
produtos_alto_risco = 0

for i in range(1, n_produtos + 1):
    print(f"Produto {i}")
    preco_unitario = float(input("Preço unitário: R$ "))
    quant_estoque = int(input("Informe a quantidade em estoque:"))
    valor_bruto = preco_unitario * quant_estoque #Valor bruto do Item
    if quant_estoque > 100:
        valor_total_estoque += (valor_bruto * 1.05) #fator Otimização de 5%
    elif preco_unitario > 50 and quant_estoque <= 10:
        produtos_alto_risco += 1
        valor_total_estoque += valor_bruto
    else:
        valor_total_estoque += valor_bruto

print("--- Resultado da Avaliação de Estoque ---")
print(f"Valor Total Final do Estoque: R$ {valor_total_estoque:.2f} \nNúmero de Produtos Classificados como Alto Risco: {produtos_alto_risco}")
