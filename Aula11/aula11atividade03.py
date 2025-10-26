print("Atividade 03 - Aual 11")

v_inicial = float(input("Informe o valor do investimento incial R$ "))
n_meses =  int(input("Informe o Número de Meses a serem simulados: "))

valor_acumulado = v_inicial
juros_totais = 0

for i in range(1, n_meses + 1):
    taxa_cresc_mensal =  float(input("Informe a Taxa de Crescimento Mensal(em decimal, ex: 0.02 para 2%: "))
    if taxa_cresc_mensal > 0.015:
        juros = valor_acumulado * taxa_cresc_mensal
    elif 0.015 > taxa_cresc_mensal < 0.005:
        juros = valor_acumulado * taxa_cresc_mensal * 0.9
    else:
        juros = 0.0

valor_acumulado += juros
juros_totais += juros

if juros_totais > (v_inicial * 0.10):
    print("Investimento de Alto Sucesso! (Retorno superior a 10%)")
else: 
    print("Investimento Moderado. Retorno abaixo do esperado.")

print(f"O Valor Acumulado Final foi de R${valor_acumulado} \nE os Juros Totais foram de R${round(juros_totais)}")