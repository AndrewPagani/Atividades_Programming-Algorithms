sal = float(input("Digite o salário atual: R$"))

if sal <= 1500:
    print(f"Novo salário: R${sal*1.15:.2f}\nAumento de 15%")
elif sal > 1500 and sal <= 3000:
    print(f"Novo salário: R${sal*1.10:.2f}\nAumento de 10%")
else:
    print(f"Novo salário: R${sal*1.05:.2f}\nAumento de 5%")
