# Leitura do salário do funcionário
salario = float(input("Informe o salário do funcionário: "))

# Cálculo do novo salário, do dinheiro ganho e do percentual de aumento
percentual_aumento = 0.15
dinheiro_ganho = salario * percentual_aumento
novo_salario = salario + dinheiro_ganho

# Impressão dos resultados
print("Novo salário:", format(novo_salario, ".2f"))
print("Reajuste ganho:", format(dinheiro_ganho, ".2f"))
print("Em percentual:", format(percentual_aumento * 100, ".2f"), "%")
