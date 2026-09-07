l1,l2,l3 = list(map(int, input("Digite os lados: ").split(",")))

if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):
    print("FORMAM UM TRIÂNGULO")
else:
    print("NÃO FORMAM UM TRIÂNGULO")