print("Tarefa 01 - Aula 12 - Análise de Bônus de Vendas e Desempenho")

v_base = float(input("Informe o Valor Base do Bônus: "))
p_ind = float(input(" Informe a Pontuação de Performance Individual(0 a 100): "))
p_equipe = float(input(" Informe a Pontuação de Performance da Equipe(0 a 100): "))

#Fator de Ajust de Performance(FAP)
if p_ind > 90:
    fap = 1.25
elif p_ind > 70:
    fap = 1.10
elif p_ind > 50:
    fap = 1.00
else:
    fap = 0.80

#Valor do Bônus Ajustado
b_ajustado = v_base * fap

#Bônus Final com base na Performance da Equipe
if p_equipe > 85:
    if p_ind  > 95 or b_ajustado > 5000:
        print("Bônus Máximo (30% Extra)")
        b_final = b_ajustado * 1.30
    else:
        print("Bônus Padrão (10% Extra)")
        b_final = b_ajustado * 1.10
elif 85 >= p_equipe >= 60:
    if p_ind < 60:
        print("Penalidade por Desempenho Individual (15% de Redução)")
        b_final = b_ajustado * 0.85
    else:
        print("Sem alteração Adicional")
        b_final = b_ajustado
else:
    print("Penalidade Severa (25% de Redução)")
    b_final = b_ajustado * 0.75

print("----------------------------------------------------")
print(f"O Valor Base do Bônus é: R$ {v_base:,.2f} \nO Fator de Ajuste de Performance(FAP) é: {fap:.2f} \nO Valor do Bônus Final é: R$ {b_final:,.2f}")