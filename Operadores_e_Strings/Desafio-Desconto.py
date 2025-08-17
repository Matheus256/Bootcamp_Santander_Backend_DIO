# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()

#Aplique o desconto se o cupom for válido:
preco = preco - preco*descontos[cupom]

print(f"{preco:.2f}")
