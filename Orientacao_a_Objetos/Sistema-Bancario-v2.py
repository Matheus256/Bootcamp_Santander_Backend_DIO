from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

#==================== Modelagem das classes ====================

class Cliente:
    def __init__(self,endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        #Método abstrato
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        #Contrutor da classe pai 
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        #Convenção para que esses atributos sejam privados
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico() #A instancia ed um cliente vai ter a instância de um histórico
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    #Os propertys são devido aos atributos serem privados
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    #Finalmente as operações
    def sacar(self, valor):
        if (valor > self.saldo):
            print("Operação inválida. Saldo insuficiente.")
        
        elif (valor > 0):
            self._saldo -= valor
            print("Saque realizado com sucesso.")
            return True
        
        else:
            print("Operação inválida. O valor infomado é inválido.")

        return False

    def depositar(self, valor):
        if (valor > 0):
            self._saldo += valor
            print("Deposito realizado com sucesso.")
        else:
            print("Operação inválida. O valor informado é inválido.")
            return False
        
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite = 500, limite_saques = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
    
    def sacar(self, valor):
        saques_realizados = len(
                [transacao for transacao in self.historico.transacoes 
                if (transacao["tipo"] == Saque.__name__)]
            )
        
        if (valor > self.limite):
            print("Operação inválida. Limite excedido.")
        
        elif (saques_realizados >= self.limite_saques):
            print("Operação inválida. Limite de saques excedido.")
        
        else:
            return super().sacar(valor) #A implementação da classe pai resolve o restante

        return False
    
    #Para usar no print
    def __str__(self):
        return f"""
            Agência: {self.agencia}
            Conta Corrente: {self.numero}
            Titular: {self.cliente.nome}
        """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):

    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

#================ Modelagem do funcionamento ======================

#Função que realiza o deposito
def realizar_deposito(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Erro. Cliente não encontrado")
        return

    valor = float(input("Informe o valor do deposito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def realizar_saque(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Erro. Cliente não encontrado")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Erro. Cliente não encontrado")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("=============== EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = "\n"
    if not transacoes:
        extrato = "Não foram realizadas transações"
    else:
        for transacao in transacoes:
            extrato += f"{transacao["tipo"]}: R${transacao["valor"]:.2f}\n"

    print(extrato)
    print(f"\nSaldo: R$ {conta.saldo:.2f}")
    print("========================================")

#Criando uma nova conta
def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Erro. Cliente não encontrado")
        return

    conta = ContaCorrente.nova_conta(cliente = cliente, numero = numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("Conta criada com suceso.")

def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(conta)

def criar_cliente(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("Erro. Cliente já existente")
        return
    
    nome = input("Infome o nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (no formato logradouro, num - bairro - cidade/UF): ")

    cliente = PessoaFisica(nome = nome,
                        data_nascimento = data_nascimento,
                        cpf = cpf,
                        endereco = endereco)
    
    clientes.append(cliente)
    print("Cliente criado com sucesso.")

#Função auxiliar de validação dos CPFs já exitentes
def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

#Função auxiliar para pegar contas de clientes
def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("Erro. O cliente não possui contas")
        return

    # FIXME: permitir o cliente escolher a conta
    return cliente.contas[0]

#A famosa (main)
def main():
    MENU = """
    ============== MENU ===============
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo cliente
    [q] Sair

    => """

    #Novas variáveis para usuarios e contas
    clientes = []
    contas = []

    while(True):
        opcao = input(MENU)

        if(opcao == "d"):
            realizar_deposito(clientes)

        elif(opcao == "s"):
            realizar_saque(clientes)
        
        elif(opcao == "e"):
            exibir_extrato(clientes)

        elif(opcao == "nu"):
            criar_cliente(clientes)
        
        elif(opcao == "nc"):
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif(opcao == "lc"):
            listar_contas(contas)
        
        elif(opcao == "q"):
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

#Chamada da função principal do Sistema bancário
main()

print("Obrigado por usar nosso sistema. Até a próxima!")