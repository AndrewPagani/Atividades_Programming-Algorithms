age = int(input("Digite a idade: "))
est = input("Estudante: ")

if (age < 12 and age > 0) or age >= 60 or est.lower() == "sim":
    print("Valor do ingresso: R$15,00")
else:
    print("Valor do ingresso: R$30,00")