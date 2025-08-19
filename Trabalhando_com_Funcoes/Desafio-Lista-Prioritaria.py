#Ordene por prioridade: urgente > idosos > demais:
def organizar_atendimento(pacientes):
    ordenada = []

    for i in range(len(pacientes)):
        nome, idade, status = pacientes[i]

        # Define prioridade:
        if status == "urgente":
            if(idade >= 60):
                prioridade = - 100 - (idade - 60)
            else:
                prioridade = -100
        elif idade >= 60:
            prioridade = 60 - idade
        else:
            prioridade = 3

        ordenada.append((prioridade, i, nome))  # i é usado para manter a ordem de chegada

    # Ordena por prioridade e ordem de chegada
    ordenada.sort()
    return [pasciente[2] for pasciente in ordenada]


# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

#Exiba a ordem de atendimento com título e vírgulas:
ordem_atendimento = organizar_atendimento(pacientes)

print("Ordem de Atendimento:", ", ".join(ordem_atendimento))