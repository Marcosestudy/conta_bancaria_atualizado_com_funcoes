
# Sistema Bancário em Python

Este é um projeto de sistema bancário simples, implementado em Python, com funcionalidades básicas como criação de clientes e contas, depósitos, saques e exibição de extrato. O código utiliza conceitos de programação orientada a objetos, como herança, abstração e polimorfismo, além de um menu interativo para o usuário.

## Funcionalidades

- **Criar Cliente**: Cria um novo cliente no sistema, solicitando o nome, CPF, data de nascimento e endereço.
- **Criar Conta**: Associa uma nova conta corrente a um cliente já existente.
- **Depositar**: Realiza um depósito em uma conta associada a um cliente.
- **Sacar**: Realiza um saque, respeitando o saldo disponível e o limite de saques diários.
- **Exibir Extrato**: Mostra o histórico de transações (saques e depósitos) realizados na conta do cliente, além do saldo atual.
- **Listar Contas**: Lista todas as contas registradas no sistema com informações detalhadas sobre agência, número da conta e titular.
- **Limite de Saques**: Cada conta corrente possui um limite diário de saques e um limite de valor por saque.

## Estrutura do Projeto

O projeto é organizado em classes que representam os principais elementos do sistema bancário:

### Classes Principais

- `Cliente`: Classe base que armazena o endereço e as contas associadas ao cliente.
- `PessoaFisica`: Herda de `Cliente` e adiciona atributos como nome, CPF e data de nascimento.
- `Conta`: Representa uma conta bancária com métodos para saque, depósito e acesso ao histórico de transações.
- `ContaCorrente`: Herda de `Conta` e adiciona o controle de limite de saques e valor máximo de saque.
- `Historico`: Armazena todas as transações realizadas em uma conta.
- `Transacao`: Classe abstrata para definir o comportamento de transações como saque e depósito.
- `Saque` e `Deposito`: Implementações concretas de transações que herdam de `Transacao`.

### Estrutura de Arquivos

O projeto consiste em um único arquivo Python contendo todas as classes e funções.

### Exemplo de Uso

Ao iniciar o programa, você verá o seguinte menu:


1. **Criar Cliente**: Escolha a opção `nu` para adicionar um novo cliente. O sistema solicitará CPF, nome, data de nascimento e endereço.
   
2. **Criar Conta**: Depois de criar um cliente, você pode criar uma conta para ele utilizando a opção `nc`.

3. **Depositar**: Escolha a opção `d` para realizar um depósito na conta de um cliente.

4. **Sacar**: Escolha a opção `s` para realizar um saque na conta. Respeitando os limites de saque.

5. **Exibir Extrato**: A opção `e` exibe o extrato da conta, com o histórico de transações e o saldo atual.

6. **Listar Contas**: A opção `lc` lista todas as contas registradas no sistema.

7. **Sair**: A opção `q` encerra o programa.

### Exemplo de Execução

# Menu de Transações Bancárias

### Opções Disponíveis:
- **Depositar**
- **Sacar**
- **Extrato**
- **Nova Conta**
- **Listar Contas**
- **Novo Cliente**
- **Sair**

### Criar Novo Cliente
- **Informe o CPF (somente número):** 12345678908
- **Informe o nome completo:** João da Silva
- **Informe a data de nascimento (dd-mm-aaaa):** 01/01/2000
- **Informe o endereço:** Rua dos Bobos, nº 0

**Resultado:** Cliente criado com sucesso!

### Criar Nova Conta
- **Informe o CPF do cliente:** 12345678900

**Resultado:** Conta criada com sucesso!

### Realizar Depósito
- **Informe o CPF do cliente:** 12345678900
- **Informe o valor do depósito:** 1860

**Resultado:** Depósito realizado com sucesso!

### Realizar Saque
- **Informe o CPF do cliente:** 12345678900
- **Informe o valor do saque:** 500

**Resultado:** Saque realizado com sucesso!

### Consultar Extrato
- **Informe o CPF do cliente:** 12345678960

**Extrato:**
- **Depósito:** R$ 1808.69 em 21/11/2023 às 14:56:23
- **Saque:** R$ 580.00 em 21/11/2023 às 14:56:23
- **Saldo:** R$ 500.00

### Listar Contas
- **Informe o CPF do cliente:** 12345678900

**Resultado:** Contas listadas com sucesso!

### Detalhes da Conta
- **Agência:** 0001
- **Conta Corrente:** 
- **Titular:** João da Silva
