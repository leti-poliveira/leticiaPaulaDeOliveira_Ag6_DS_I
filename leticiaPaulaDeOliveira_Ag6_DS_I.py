# Solicita ao usuário o valor total da compra
valor_compra = float(input("Digite o valor da compra: R$ "))

# Verifica se a compra é menor que R$ 200,00
if valor_compra < 200:
    desconto = valor_compra * 0.05
    total = valor_compra - desconto

    print(f"Seu desconto é de 5%!")
    print(f"Valor do desconto: R$ {desconto:.2f}")
    print(f"Valor total da compra: R$ {total:.2f}")

# Verifica se a compra está entre R$ 200,00 e R$ 299,99
elif valor_compra < 300:
    desconto = valor_compra * 0.10
    total = valor_compra - desconto

    print(f"Seu desconto é de 10%!")
    print(f"Valor do desconto: R$ {desconto:.2f}")
    print(f"Valor total da compra: R$ {total:.2f}")

# Para compras de R$ 300,00 ou mais, aplica 15% de desconto
else:
    desconto = valor_compra * 0.15
    total = valor_compra - desconto

    print(f"Seu desconto é de 15%!")
    print(f"Valor do desconto: R$ {desconto:.2f}")
    print(f"Valor total da compra: R$ {total:.2f}")

