print("Atividade 07 - Aula 11")

salario_base = 800.00
limite_falha_tolerada = 1
cont_falhas = 0

for i in range(5):
    p_dia = int(input("Informe a Pontuação de Produtividade Diária(de 0 a 100): "))
    if p_dia < 60:
        cont_falhas += p_dia

prod_media = (p_dia * 5) / 5

if prod_media > 80 and cont_falhas <= 1:
    print("Pagamento Máximo: Bônus de 10% aplicado.")
    pag_final = salario_base * 1.10
elif 80 < prod_media > 60:
    print("Pagamento Padrão: Penalidade de 5% aplicada (Devido a falhas).")
    pag_final = salario_base * 0.95
else:
    print("Penalidade Severa: Pagamento reduzido em 25%.")
    pag_final = salario_base * 0.75

print(f"A Produtividade Média foi de {prod_media}. \nA Contagem de Falhas foi de: {cont_falhas}. \nE seu Pagamento Final foi de R${(pag_final):.2f}.")