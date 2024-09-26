# Dicionário para armazenar os clientes
clientes = {}

# Conjunto para armazenar CPF/CNPJ únicos
cnpj_set = set()

# Tupla com os tipos de conta disponíveis
tipos_conta = ("Física", "Jurídica")

LIMITE_SAQUE = 3

opcoes_menu_principal = [
    '[1] Cadastrar Cliente',
    '[2] Acessar Conta',
    '[0] Sair'
]

opcoes_menu_operacoes = [
    '[0] Sair da Conta',
    '[1] Depositar',
    '[2] Sacar',
    '[3] Extrato',
    '[4] Listar Clientes'  
]

def solicitar_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido.")

def solicitar_senha():
    while True:
        senha = input('Crie uma senha (apenas números, mínimo 4 dígitos): ')
        if senha.isdigit() and len(senha) >= 4:
            return senha
        else:
            print("Erro: A senha deve conter apenas números e ter pelo menos 4 caracteres.")

def cadastrar_cliente():
    nome = input('Nome: ')
    cpf_cnpj = input('CPF ou CNPJ: ')

    if cpf_cnpj in cnpj_set:
        print("Erro: CPF/CNPJ já cadastrado.")
        return 

    telefone = solicitar_inteiro('Telefone (apenas números): ')

    while True:
        tipo = input("Escolha o tipo de conta (F para Física, J para Jurídica): ").strip().upper()
        if tipo == "F":
            tipo = tipos_conta[0] 
            break
        elif tipo == "J":
            tipo = tipos_conta[1]  
            break
        else:
            print("Erro: Opção inválida. Digite 'F' para Física ou 'J' para Jurídica.")

    agencia = input('Agência: ')  
    senha = solicitar_senha()  
    clientes[cpf_cnpj] = {
        'nome': nome,
        'telefone': telefone,
        'tipo': tipo,
        'agencia': agencia,
        'senha': senha,
        'saldo': 0,
        'extrato': [],
        'saques_realizados': 0 
    }
    
    cnpj_set.add(cpf_cnpj)
    
    print('Cliente cadastrado com sucesso!')

def acessar_conta():
    cpf_cnpj = input('Digite o CPF ou CNPJ do cliente: ')
    if cpf_cnpj in clientes:
        tentativas = 0
        while tentativas < 3:
            senha_inserida = input('Digite sua senha: ')
            if senha_inserida == clientes[cpf_cnpj]['senha']:
                print('---------------------------------')
                print(f'Olá {clientes[cpf_cnpj]["nome"]}, Bem-vindo ao PythonBank!')
                menu_operacoes(cpf_cnpj)
                break
            else:
                tentativas += 1
                print(f'Senha incorreta. Tentativa {tentativas} de 3.')

        if tentativas == 3:
            print('Número máximo de tentativas atingido. Acesso encerrado.')
    else:
        print('Cliente não encontrado.')

def menu_operacoes(cpf_cnpj):
    while True:
        print('---------------------------------')
        print('Realize suas Operações Bancárias')
        for i in range(len(opcoes_menu_operacoes)):
            print(opcoes_menu_operacoes[i])
        print('---------------------------------')

        acao = input('Opção: ')
        print('---------------------------------')

        if acao == str(0):
            print('Saindo da conta...')
            break
        elif acao == str(1):
            depositar(cpf_cnpj)
        elif acao == str(2):
            sacar(cpf_cnpj)
        elif acao == str(3):
            visualizar_extrato(cpf_cnpj)
        elif acao == str(4):
            listar_clientes() 
        else:
            print('Opção inválida. Tente novamente.')

def depositar(cpf_cnpj):
    while True:
        valor = input('Valor a depositar: ')
        try:
            valor = float(valor)
            if valor > 0:
                clientes[cpf_cnpj]['saldo'] += valor
                clientes[cpf_cnpj]['extrato'].append(f'Depósito: R$ {valor:.2f}')
                print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
                break
            else:
                print('Valor de depósito deve ser positivo.')
        except ValueError:
            print('Erro: Por favor, digite um número válido para o valor do depósito.')

def sacar(cpf_cnpj):
    if clientes[cpf_cnpj]['saques_realizados'] >= LIMITE_SAQUE:
        print("Erro: Limite de saques por sessão atingido.")
        return

    while True:
        valor = input('Valor a sacar: ')
        try:
            valor = float(valor)
            if 0 < valor <= clientes[cpf_cnpj]['saldo']:
                clientes[cpf_cnpj]['saldo'] -= valor
                clientes[cpf_cnpj]['extrato'].append(f'Saque: R$ {valor:.2f}')
                clientes[cpf_cnpj]['saques_realizados'] += 1 
                print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
                break
            else:
                print('Valor de saque inválido ou saldo insuficiente.')
        except ValueError:
            print('Erro: Por favor, digite um número válido para o valor do saque.')

def visualizar_extrato(cpf_cnpj):
    print(f'Saldo: R$ {clientes[cpf_cnpj]["saldo"]:.2f}')
    print('---------------------------------')
    print('--- Extrato Bancário ---')
    for registro in clientes[cpf_cnpj]['extrato']:
        print(registro)
    print(f'Saldo Atual: R$ {clientes[cpf_cnpj]["saldo"]:.2f}')

def listar_clientes():
    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        print("--- Lista de Clientes ---")
        for cpf_cnpj, info in clientes.items():
            print(f"CPF/CNPJ: {cpf_cnpj}, Nome: {info['nome']}, Tipo: {info['tipo']}, Agência: {info['agencia']}")  # Mostrar agência

while True:
    print('---------------------------------')
    print('--- Sistema Bancário ---')
    print('---------------------------------')
    print('Escolha uma opção:')
    for i in range(len(opcoes_menu_principal)):
        print(opcoes_menu_principal[i])

    opcao = input('Opção: ')
    print('---------------------------------')

    if opcao == str(1):
        cadastrar_cliente()
    elif opcao == str(2):
        acessar_conta()
    elif opcao == str(0):
        print('Obrigado por utilizar o PythonBank! Até a próxima! Saindo do sistema...')
        break
    else:
        print('Opção inválida. Tente novamente.')
