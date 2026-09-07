peso = float(input("Digite seu peso em Kg: "))
altura = float(input("Digite sua altura em Metros: "))

imc = peso/(altura**2)
print(f"IMC: {imc:.2f}")

if imc < 18.5:
    print("ABAIXO DA FAIXA")
elif imc >= 18.5 and imc < 25:
    print("FAIXA NORMAL")
elif imc >= 25 and imc < 30:
    print("ACIMA DA FAIXA")
else:
    print("FAIXA ELEVADA")