print("Tarefa 06 - Aula 12 - Análise de Dados de Produção")#Convertido o loop FOR em WHILE

n_total_pecas =  int(input("Digite o número total de peças a serem inspecionadas: "))
tolerancia_desvio = 0.5  # Tolerância de desvio 0.5cm
tamanho_ideal = 15.0     # Tamanho ideal 15cm
soma_dos_tamanhos = 0.0
pecas_fora_tolerancia = 0

i = 1
while i <= n_total_pecas:
    tamanho_medido = float(input(f"Digite o tamanho da peça {i} em cm: "))
    soma_dos_tamanhos += tamanho_medido
    desvio = abs(tamanho_medido - tamanho_ideal)
    if desvio > tolerancia_desvio:
        pecas_fora_tolerancia += 1
    i += 1  # Incrementa a variável de iteração

#Cálculos e Decisões Finais
media_tamanho = soma_dos_tamanhos / n_total_pecas
if pecas_fora_tolerancia == 0:
    print("Lote Aprovado: Qualidade perfeita (0 peças fora da tolerância).")
elif pecas_fora_tolerancia <= 2:
    print("Lote Aceitável: Pequena correção necessária.")
else:
    print("Lote Reprovado: Alta taxa de defeito.")

print("--- Estatísticas Finais ---")
print(f"Média de tamanho das Peças: {media_tamanho:.2f} cm \nQuantidade de Peças Fora da Tolerância: {pecas_fora_tolerancia}")
