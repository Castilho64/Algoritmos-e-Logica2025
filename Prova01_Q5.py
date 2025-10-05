#Nome: João Vitor Castilho Mattos
#RA: 0220482523041
from imp import init_builtin


print("João Vitor Castilho Mattos, RA: 0220482523041")
print("Questão 05")

c_inicial = float(input("Informe o custo inicial do material R$"))
q_itens =  int(input("Informe a quantidade de itens produzidos: "))
dias = int(input("Informe o dias de atraso: "))
perc_def =  float(input("Informe o percentual de defeitos (%): "))

if q_itens > 1000 and c_inicial > 5000:
    f_comp = 1.15
else:
    f_comp = 1.05

c_corrigido = c_inicial * f_comp

if perc_def > 0.10 or dias > 5:
    c_final = c_corrigido * 1.25
    print(f"Penalidade Alta: 20% na redução de lucro")
elif perc_def >=0.05 and perc_def <= 0.10 and dias > 0:
    c_final = c_corrigido * 1.10
    print(f"Penalidade Média: 10% de redução no lucro.")
else:
    print(f"Sem penalidade. Custo final apenas com correção.")
    c_final = c_corrigido

print(f"O custo corrigido foi de R${c_corrigido} e o custo final foi de R${c_final}")