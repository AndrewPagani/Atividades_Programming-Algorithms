n = int(input("Digite o limite: "))
l = []

if n <= 0:
    print("Não permitido")

for i in range(n):
    i += 1
    l.append(i)
    
print(*l)