# 💳 Sistema Bancário em Python

Este projeto é um sistema bancário simples desenvolvido em Python. O sistema permite o cadastro de clientes, gerenciamento de contas e operações bancárias como depósito, saque e visualização de extratos. Utiliza conceitos de Programação Orientada a Objetos, incluindo herança, encapsulamento e interfaces.

## 🚀 Funcionalidades

- 📝 Cadastrar clientes (pessoa física e jurídica).
- 🔑 Acessar contas bancárias.
- 💵 Realizar depósitos e saques.
- 📊 Visualizar extrato da conta.
- 📋 Listar todos os clientes cadastrados.

## 📊 Diagrama de Classes

```mermaid
classDiagram
    class Transacoes {
        +sacar(valor: float)
        +depositar(valor: float)
    }
    
    class Conta {
        -agencia: str
        -saldo: float
        -extrato: list
        -senha: str
        -saques_realizados: int
        +depositar(valor: float)
        +visualizar_extrato()
    }
    
    class ContaCorrente {
        +sacar(valor: float)
    }
    
    class Pessoa {
        -nome: str
        -cpf_cnpj: str
        -telefone: str
        -tipo: str
        +conta: Conta
    }
    
    class PessoaFisica {
        +PessoaFisica(nome: str, cpf: str, telefone: str, agencia: str, senha: str)
    }
    
    class PessoaJuridica {
        +PessoaJuridica(nome: str, cnpj: str, telefone: str, agencia: str, senha: str)
    }
    
    Transacoes <|-- Conta
    Conta <|-- ContaCorrente
    Pessoa <|-- PessoaFisica
    Pessoa <|-- PessoaJuridica
