def soma_imposto(taxa_imposto, custo):
    tax = (taxa_imposto/100) + 1
    return(custo * tax)

custo = float(input("Digite o valor do produto: "))
taxa_imposto = float(input("Digite a porcentagem do imposto: "))

preco = soma_imposto(taxa_imposto, custo)
print(f'{preco:.2f}')