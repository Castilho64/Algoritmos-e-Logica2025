print("Atividae 05 - Aula 11")

qtd_nota_fiscais = int(input("Informe a quantidade de Notas Fiscais: "))
soma_das_notas = 0

for i in range(1, qtd_nota_fiscais + 1):
    valor_nota = float(input(f"Informe o valor da nota {i} R$"))
    soma_das_notas += valor_nota

if soma_das_notas <= 100:
    aliquota = 0.05
    valor_imposto = soma_das_notas * 0.05
elif 4999 <= soma_das_notas >= 1000:
    aliquota = 0.09
    valor_imposto = soma_das_notas * 0.09
elif 14999 <= soma_das_notas >= 5000:
    aliquota = 0.12
    valor_imposto = soma_das_notas * 0.12
else: 
    aliquota = 0.16
    valor_imposto = soma_das_notas * 0.16

print(f"O Valor Total das Notas foi de R${round(soma_das_notas)} \nA Alíquota Aplicada foi de {aliquota * 100}% \nO Valor Total do Imposto a ser pago é de R${round(valor_imposto)}")