# 💳 Sistema Bancário em Python

> Este projeto tem como objetivo exercitar a lógica em Python, simulando a criação de um sistema bancário completo.

## 📜 Descrição
O **Sistema Bancário** é um projeto desenvolvido em Python que permite aos usuários:
- Cadastrar clientes com informações básicas.
- Acessar contas de forma segura.
- Realizar operações bancárias como depósitos e saques.
- Visualizar extratos detalhados.

Esse projeto é uma excelente oportunidade para praticar programação em Python e compreender conceitos de segurança e manipulação de dados.

## 🚀 Funcionalidades
- **Cadastro de Clientes**: 
  - Cadastrar clientes com nome, CPF/CNPJ, telefone e senha.
  
- **Acesso à Conta**: 
  - Os clientes podem acessar suas contas usando CPF/CNPJ e senha.

- **Operações Bancárias**:
  - 💵 **Depositar**: Adiciona valor à conta do cliente.
  - 💳 **Sacar**: Permite a retirada de valores da conta.
  - 📊 **Extrato**: Mostra o saldo atual e o histórico de transações.

## 📊 Diagrama Lógico
```mermaid
flowchart TD
    A[Início] --> B[Mostrar Menu Principal]
    B --> C{Escolher Opção}
    C -->|Cadastrar Cliente| D[Input: Nome, CPF/CNPJ, Telefone, Tipo, Senha]
    D --> E[Armazenar Cliente no Dicionário]
    E --> B

    C -->|Acessar Conta| F[Input: CPF/CNPJ]
    F --> G{Cliente Encontrado?}
    G -->|Sim| H[Input: Senha]
    H --> I{Senha Correta?}
    I -->|Sim| J[Mostrar Menu de Operações]
    J --> K{Escolher Ação}
    
    K -->|Depositar| L[Input: Valor a Depositar]
    L --> M[Atualizar Saldo e Extrato]
    M --> J
    
    K -->|Sacar| N[Input: Valor a Sacar]
    N --> O{Valor Válido?}
    O -->|Sim| P[Atualizar Saldo e Extrato]
    P --> J

    K -->|Extrato| Q[Mostrar Saldo e Extrato]
    Q --> J

    K -->|Sair| R[Encerrar Acesso]
    R --> B

    G -->|Não| S[Mostrar Cliente Não Encontrado]
    S --> B

    C -->|Sair| T[Encerrar Sistema]
    T --> U[Fim]
```

## 📦 Tecnologias Utilizadas
- **Python 3.x**: A linguagem de programação utilizada para desenvolver o sistema.
- **Dicionários**: Estruturas de dados que armazenam informações dos clientes.

## 🛠️ Como Executar
Para executar o sistema bancário, siga os passos abaixo:

1. **Baixe o Projeto**:
   - Use o botão de download ou clone o repositório.

2. **Navegue até o diretório do projeto**:
   ```bash
   cd PythonBank
   ```

3. **Execute o script**:
   ```bash
   python banking_system.py
   ```
