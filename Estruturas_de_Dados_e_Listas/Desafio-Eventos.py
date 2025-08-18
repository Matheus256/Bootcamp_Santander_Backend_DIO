# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

#Cria um loop para armazenar participantes e seus temas:
for _ in range(n):
  linha = input().strip().split(",")

  try:
    eventos[linha[1].strip()].append(linha[0].strip())
  except:
    eventos[linha[1].strip()] = [linha[0].strip()]

# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")