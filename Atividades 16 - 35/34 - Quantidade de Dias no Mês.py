mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))
bissexto = (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)

match mes:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("31 Dias")
    case 4 | 6 | 9 | 11:
        print("30 Dias")
    case 2:
        if bissexto:
            print("29 Dias")
        else:
            print("28 Dias")
    case _:
        print("Mês Inválido")