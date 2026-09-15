l1, l2, l3 = list(map(int, input("Digite os lados do Triângulo: ").split(",")))

if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):
    if l1 == l2 == l3:
        print("Triângulo Equilátero")
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("NÃO FORMAM UM TRIÂNGULO")
