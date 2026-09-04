val = list(map(int, input("Digite 3 números: ").split(",")))

if val[0] > val[1]:
    val[0],val[1] = val[1], val[0]
  
if val[1] > val[2]:
    val[1], val[2] = val[2], val[1]
  
if val[0] > val[1]:
    val[0],val[1] = val[1], val[0]
    
print(f" Maior: {val[2]}\n Menor: {val[0]}")
