num = int(input("Insira um número correspondente a algum dia da semana: "))

match num:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda-Feira")
    case 3:
        print("Terça-Feira")
    case 4:
        print("Quarta-Feira")
    case 5:
        print("Quinta-Feira")
    case 6:
        print("Sexta-Feira")
    case 7:
        print("Sábado")
    case default:
        print("Opção inválida")