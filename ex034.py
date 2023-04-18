salario = float(input("Informe seu salário para vizualizar o aumento: R$"))
if salario > 1250.00:
    print(f"Você teve um aumento de 10%, seu salario com aumento ficou: R${salario*1.1:s.2f}!")
else:
    print(f"Você teve um aumento de 15%, seu salario com aumento ficou: R${salario*1.15:.2f}!")