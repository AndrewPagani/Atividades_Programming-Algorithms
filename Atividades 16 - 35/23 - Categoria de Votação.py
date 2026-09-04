idade = int(input("Digite sua idade: "))

if idade >= 18 and idade <= 69:
    print("VOTO OBRIGATÓRIO")
elif idade >= 16 and idade <= 17 or idade >= 70:
    print("VOTO OPCIONAL")
else:
    print("NÃO PODE VOTAR")