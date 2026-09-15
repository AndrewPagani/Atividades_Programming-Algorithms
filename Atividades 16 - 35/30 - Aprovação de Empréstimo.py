valor = float(input("Valor do Imóvel: R$"))
sal = float(input("Salário: R$"))
prazo = int(input("Prazo em anos: "))

prest = valor/(prazo*12)
lim = sal*0.30

print(f"Prestação: R${prest:.2f}")
print(f"Limite: R${lim:.2f}")

if prest > lim:
    print(f"Resultado: NEGADO")
else:
    print("Resultado: APROVADO")