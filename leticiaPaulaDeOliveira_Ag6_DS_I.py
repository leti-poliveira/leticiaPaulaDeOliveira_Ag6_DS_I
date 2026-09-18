# Solicita ao usuário o valor total da compra
valor_compra = float(input("Digite o valor da compra: R$ "))

# Define o percentual de desconto
if valor_compra < 200:
    percentual = 0.05
elif valor_compra < 300:
    percentual = 0.10
else:
    percentual = 0.15

# Calcula o desconto e o valor total
desconto = valor_compra * percentual
total = valor_compra - desconto

# Exibe os resultados
print(f"Seu desconto é de {percentual * 100:.0f}%!")
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Valor total da compra: R$ {total:.2f}")