num = int(input("Digite um número: "))

if num % 3 == 0 and num % 5 == 0:
    print("DIVISÍVEL POR 3 E 5")
elif num % 5 == 0:
    print("DIVISÍVEL POR 5")
elif num % 3 == 0:
    print("DIVISÍVEL POR 3")
else:
    print("NÃO DIVISÍVEL POR 3 OU 5")