#Função que realiza o deposito
def realizar_deposito(saldo, deposito, extrato, /):
    if deposito > 0:
        saldo += deposito
        extrato += f"Depósito: R$ {deposito:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

#Função que realiza o saque
def realizar_saque(*, saldo, saque, extrato, limite, numero_saques, limite_saques):

    if saque > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif saque > limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif saque > 0:
        saldo -= saque
        extrato += f"Saque: R$ {saque:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

#Função para exibir o extrato
def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO DA CONTA ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

#Função para criar um usuário
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ").strip()

    if filtrar_usuario(cpf, usuarios):
        print("Erro! Já existe um usuário cadastrado com esse CPF.")
        return

    nome = input("Informe o nome completo: ")
    nascimento = input("Informe a data de nascimento (no formato dd-mm-aaaa): ")
    endereco = input("Informe o endereço (no formato logradouro, num - bairro - cidade/UF): ")

    usuarios.append({"nome": nome, "data_nascimento": nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário adicionado com sucesso!")

#Função para criar conta
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario["nome"]}

    print("Usuário não encontrado, fluxo de criação de conta encerrado!")

#Função de validação dos CPFs já exitentes
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada!")
        return
    
    print("\n================ CONTAS CADASTRADAS ================")
    for conta in contas:
        texto = f"""
            Agência: {conta['agencia']}
            Número da conta: {conta["numero_conta"]}
            Titular: {conta["usuario"]}
        """
        print(texto)
        print("-------------------------------------------------")
    print("\n====================================================")

#Função principal que inicia o Sistema Bancário
def main():
    MENU = """
    ============== MENU ===============
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q] Sair

    => """

    LIMITE = 500
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    extrato = ""
    numero_saques = 0

    #Novas variáveis para usuarios e contas
    usuarios = []
    contas = []

    while(True):
        opcao = input(MENU)

        if(opcao == "d"):
            deposito = float(input("Informe o valor do depósito: "))

            saldo, extrato = realizar_deposito(saldo, deposito, extrato)

        elif(opcao == "s"):
            saque = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = realizar_saque(
                saldo = saldo,
                saque = saque,
                extrato = extrato,
                limite = LIMITE,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )
        
        elif(opcao == "e"):
            exibir_extrato(saldo, extrato = extrato)

        elif(opcao == "nu"):
            criar_usuario(usuarios)
        
        elif(opcao == "nc"):
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif(opcao == "lc"):
            listar_contas(contas)
        
        elif(opcao == "q"):
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

#Chamada da função principal do Sistema bancário
main()

print("Obrigado por usar nosso sistema. Até a próxima!")