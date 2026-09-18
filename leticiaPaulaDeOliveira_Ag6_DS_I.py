# Solicita ao usuário o valor total da compra
valor_compra = float(input("Digite o valor da compra: R$ "))

# Verifica qual percentual de desconto deve ser aplicado
if valor_compra < 200:
    percentual = 0.05
elif valor_compra < 300:
    percentual = 0.10
else:
    percentual = 0.15

# Calcula o valor do desconto
desconto = valor_compra * percentual

# Calcula o valor total após o desconto
total = valor_compra - desconto

# Exibe os resultados
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Valor total a pagar: R$ {total:.2f}")