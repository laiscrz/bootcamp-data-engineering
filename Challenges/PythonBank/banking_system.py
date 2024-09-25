# Dicionário para armazenar os clientes
clientes = {}

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
        nome = input('Nome: ')
        cpf_cnpj = input('CPF ou CNPJ: ')
        telefone = input('Telefone: ')
        tipo = input('Tipo (Pessoa Física ou Jurídica): ')
        senha = input('Crie uma senha: ')
        clientes[cpf_cnpj] = {
            'nome': nome,
            'telefone': telefone,
            'tipo': tipo,
            'senha': senha,
            'saldo': 0,
            'extrato': []
        }
        print('Cliente cadastrado com sucesso!')

    elif opcao == '1':
        cpf_cnpj = input('Digite o CPF ou CNPJ do cliente: ')
        if cpf_cnpj in clientes:
            tentativas = 0
            while tentativas < 3:
                senha_inserida = input('Digite sua senha: ')
                if senha_inserida == clientes[cpf_cnpj]['senha']:
                    print('---------------------------------')
                    print(
                        f'Olá {clientes[cpf_cnpj]["nome"]}, Bem-vindo ao PythonBank!'
                    )
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
                            valor = float(input('Valor a depositar: '))
                            if valor > 0:
                                clientes[cpf_cnpj]['saldo'] += valor
                                clientes[cpf_cnpj]['extrato'].append(
                                    f'Depósito: R$ {valor:.2f}')
                                print(
                                    f'Depósito de R$ {valor:.2f} realizado com sucesso.'
                                )
                            else:
                                print('Valor de depósito deve ser positivo.')

                        elif acao == '1':
                            valor = float(input('Valor a sacar: '))
                            if 0 < valor <= clientes[cpf_cnpj]['saldo']:
                                clientes[cpf_cnpj]['saldo'] -= valor
                                clientes[cpf_cnpj]['extrato'].append(
                                    f'Saque: R$ {valor:.2f}')
                                print(
                                    f'Saque de R$ {valor:.2f} realizado com sucesso.'
                                )
                            else:
                                print('Valor de saque inválido.')

                        elif acao == '2':
                            print(
                                f'Saldo: R$ {clientes[cpf_cnpj]["saldo"]:.2f}')
                            print('---------------------------------')
                            print('--- Extrato Bancário ---')
                            for registro in clientes[cpf_cnpj]['extrato']:
                                print(registro)
                            print(f'Saldo Atual: R$ {clientes[cpf_cnpj]["saldo"]:.2f}')
                        elif acao == '3':
                            print('Saindo da conta...')
                            break

                        else:
                            print('Opção inválida. Tente novamente.')
                    break
                else:
                    tentativas += 1
                    print(f'Senha incorreta. Tentativa {tentativas} de 3.')

            if tentativas == 3:
                print(
                    'Número máximo de tentativas atingido. Acesso encerrado.')
        else:
            print('Cliente não encontrado.')

    elif opcao == '2':
        print('Obrigado por utilizar o PythonBank!')
        print('Até a próxima! Saindo do sistema...')
        break

    else:
        print('Opção inválida. Tente novamente.')
