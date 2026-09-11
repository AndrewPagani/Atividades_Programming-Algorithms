def valida_string(word, val_min, val_max):
    if len(word) >= val_min and len(word) <= val_max:
        return(True)
    else:
        return(False)

word = input("Digite uma palavra: ")
val_min = input("Digite o mínimo de caracteres: ")
val_max = input("Digite o máximo de caracteres: ")

if val_min == "":
    val_min = 1
if val_max == "":
    val_max = 100

tamanho = valida_string(word, int(val_min), int(val_max))
print(tamanho)