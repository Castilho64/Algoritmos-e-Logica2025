# Nome: João Vitor Castilho Mattos
# RA: 0220482523041
print("Prova 2 - Questão 04: Análise de Desvio de Qualidade com Alerta de Risco")

padrao_qualid_ideal = 50.0
limite_max_desvio = 10.0
desvios_registrados = []
dias_consecutivos_baixo_padrao = 0
motivo_parada = "Encerrado pelo usuário (digitou 0)"

# Loop de registro das qualidades
medida_peca = float(input("Digite a medida da peça (0 para encerrar): "))
while medida_peca != 0:
    desvio = abs(medida_peca - padrao_qualid_ideal)
    desvios_registrados.append(desvio)
    if desvio > limite_max_desvio:
        dias_consecutivos_baixo_padrao += 1
    else:
        dias_consecutivos_baixo_padrao = 0

    # Verifica alerta máximo
    if dias_consecutivos_baixo_padrao >= 3:
        print("ALERTA MÁXIMO! Produção Paralisada por Risco de Qualidade!")
        motivo_parada = "Parada por qualidade (3 dias consecutivos fora do padrão)"
        break
    medida_peca = float(input("Digite a medida da peça (0 para encerrar): "))

# Calcular média dos desvios
media_desvios = sum(desvios_registrados) / len(desvios_registrados)

# Resumo
print("\n--- Resumo da Análise de Desvios de Qualidade ---")
print(f"Média de Desvio: {media_desvios:.2f}. \nMotivo da Parada: {motivo_parada}")
