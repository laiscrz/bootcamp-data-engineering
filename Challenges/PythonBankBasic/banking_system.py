# Dicionário para armazenar os clientes
clientes = {}

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
    telefone = solicitar_inteiro('Telefone (apenas números): ')
    tipo = input('Tipo (Pessoa Física ou Jurídica): ')
    senha = solicitar_senha()  # Usar a nova função para solicitar senha
    clientes[cpf_cnpj] = {
        'nome': nome,
        'telefone': telefone,
        'tipo': tipo,
        'senha': senha,
        'saldo': 0,
        'extrato': []
    }
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
        print('[0] Depositar')
        print('[1] Sacar')
        print('[2] Extrato')
        print('[3] Sair da Conta')
        print('---------------------------------')

        acao = input('Opção: ')
        print('---------------------------------')

        if acao == '0':
            depositar(cpf_cnpj)
        elif acao == '1':
            sacar(cpf_cnpj)
        elif acao == '2':
            visualizar_extrato(cpf_cnpj)
        elif acao == '3':
            print('Saindo da conta...')
            break
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
    while True:
        valor = input('Valor a sacar: ')
        try:
            valor = float(valor)
            if 0 < valor <= clientes[cpf_cnpj]['saldo']:
                clientes[cpf_cnpj]['saldo'] -= valor
                clientes[cpf_cnpj]['extrato'].append(f'Saque: R$ {valor:.2f}')
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

# Loop principal do sistema
while True:
    print('---------------------------------')
    print('--- Sistema Bancário ---')
    print('---------------------------------')
    print('Escolha uma opção:')
    print('[0] Cadastrar Cliente')
    print('[1] Acessar Conta')
    print('[2] Sair')

    opcao = input('Opção: ')
    print('---------------------------------')

    if opcao == '0':
        cadastrar_cliente()
    elif opcao == '1':
        acessar_conta()
    elif opcao == '2':
        print('Obrigado por utilizar o PythonBank!')
        print('Até a próxima! Saindo do sistema...')
        break
    else:
        print('Opção inválida. Tente novamente.')
