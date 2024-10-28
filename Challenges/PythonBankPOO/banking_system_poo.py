from abc import ABC, abstractmethod

# Conjunto para armazenar CPF/CNPJ únicos
cnpj_set = set()

class Transacoes(ABC):
    @abstractmethod
    def sacar(self, valor):
        pass
    
    @abstractmethod
    def depositar(self, valor):
        pass

class Conta(Transacoes):
    def __init__(self, agencia, senha):
        self.agencia = agencia
        self.saldo = 0
        self.extrato = []
        self.senha = senha
        self.saques_realizados = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f'Depósito: R$ {valor:.2f}')
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('Valor de depósito deve ser positivo.')

    def visualizar_extrato(self):
        print(f'Saldo: R$ {self.saldo:.2f}')
        print('--- Extrato Bancário ---')
        for registro in self.extrato:
            print(registro)
        print(f'Saldo Atual: R$ {self.saldo:.2f}')
        
class ContaCorrente(Conta):
    LIMITE_SAQUE = 3

    def __init__(self, agencia, senha):
        super().__init__(agencia, senha)

    def sacar(self, valor):
        if self.saques_realizados >= self.LIMITE_SAQUE:
            print("Erro: Limite de saques por sessão atingido.")
            return

        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f'Saque: R$ {valor:.2f}')
            self.saques_realizados += 1
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('Valor de saque inválido ou saldo insuficiente.')

class Pessoa(ABC):
    def __init__(self, nome, cpf_cnpj, telefone, tipo):
        self.nome = nome
        self.cpf_cnpj = cpf_cnpj
        self.telefone = telefone
        self.tipo = tipo
        self.conta = None  # Relacionar com a conta

class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf, telefone, agencia, senha):
        super().__init__(nome, cpf, telefone, "Física")
        self.conta = ContaCorrente(agencia, senha)

class PessoaJuridica(Pessoa):
    def __init__(self, nome, cnpj, telefone, agencia, senha):
        super().__init__(nome, cnpj, telefone, "Jurídica")
        self.conta = ContaCorrente(agencia, senha)

# Dicionário para armazenar os clientes
clientes = {}

def cadastrar_cliente():
    nome = input('Nome: ')
    cpf_cnpj = input('CPF ou CNPJ: ')

    if cpf_cnpj in cnpj_set:
        print("Erro: CPF/CNPJ já cadastrado.")
        return 

    telefone = input('Telefone (apenas números): ')
    agencia = input('Agência: ')
    senha = solicitar_senha()

    tipo = input("Escolha o tipo de conta (F para Física, J para Jurídica): ").strip().upper()
    if tipo == "F":
        cliente = PessoaFisica(nome, cpf_cnpj, telefone, agencia, senha)
    elif tipo == "J":
        cliente = PessoaJuridica(nome, cpf_cnpj, telefone, agencia, senha)
    else:
        print("Erro: Tipo de conta inválido.")
        return

    clientes[cpf_cnpj] = cliente
    cnpj_set.add(cpf_cnpj)
    print('Cliente cadastrado com sucesso!')

# As demais funções (acessar_conta, menu_operacoes, etc.) devem ser atualizadas para trabalhar com a nova estrutura
def acessar_conta():
    cpf_cnpj = input('Digite o CPF ou CNPJ do cliente: ')
    if cpf_cnpj in clientes:
        tentativas = 0
        while tentativas < 3:
            senha_inserida = input('Digite sua senha: ')
            if senha_inserida == clientes[cpf_cnpj].conta.senha:
                print(f'Olá {clientes[cpf_cnpj].nome}, Bem-vindo ao PythonBank!')
                menu_operacoes(clientes[cpf_cnpj].conta)
                break
            else:
                tentativas += 1
                print(f'Senha incorreta. Tentativa {tentativas} de 3.')

        if tentativas == 3:
            print('Número máximo de tentativas atingido. Acesso encerrado.')
    else:
        print('Cliente não encontrado.')

def menu_operacoes(conta):
    while True:
        print('--- Realize suas Operações Bancárias ---')
        print('[0] Sair da Conta')
        print('[1] Depositar')
        print('[2] Sacar')
        print('[3] Extrato')
        acao = input('Opção: ')

        if acao == str(0):
            print('Saindo da conta...')
            break
        elif acao == str(1):
            valor = float(input('Valor a depositar: '))
            conta.depositar(valor)
        elif acao == str(2):
            valor = float(input('Valor a sacar: '))
            conta.sacar(valor)
        elif acao == str(3):
            conta.visualizar_extrato()
        else:
            print('Opção inválida. Tente novamente.')

while True:
    print('--- Sistema Bancário ---')
    print('[1] Cadastrar Cliente')
    print('[2] Acessar Conta')
    print('[0] Sair')

    opcao = input('Opção: ')

    if opcao == str(1):
        cadastrar_cliente()
    elif opcao == str(2):
        acessar_conta()
    elif opcao == str(0):
        print('Obrigado por utilizar o PythonBank! Até a próxima!')
        break
    else:
        print('Opção inválida. Tente novamente.')
