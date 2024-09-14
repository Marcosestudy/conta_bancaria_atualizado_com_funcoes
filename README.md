# conta_bancaria_atualizado_com_funcoes
engenharia de dados

```python
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): "
    )

    usuarios.append(
        {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco,
            "contas": [],
            "senha": input("Digite a senha: "),
        }
    )

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(usuarios):
    cpf = input("Digite o CPF: ")
    senha = input("Digite a senha: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario and usuario["senha"] == senha:
        numero_conta = len(usuario["contas"]) + 1
        nova_conta = {
            "numero_conta": numero_conta,
            "saldo": 0.0,
            "limite": 1000.0,
            "extrato": "",
            "numero_saques": 0,
            "limite_saques": 3,
        }
        usuario["contas"].append(nova_conta)
        print(f"Conta {numero_conta} criada com sucesso!")
    else:
        print("CPF ou senha incorretos.")


def excluir_conta(usuarios):
    cpf = input("Digite o CPF: ")
    numero_conta = int(input("Digite o número da conta a ser excluída: "))
    senha = input("Digite a senha: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario and usuario["senha"] == senha:
        contas = usuario["contas"]
        conta = next(
            (conta for conta in contas if conta["numero_conta"] == numero_conta), None
        )
        if conta:
            contas.remove(conta)
            print(f"Conta {numero_conta} excluída com sucesso!")
        else:
            print("Conta não encontrada.")
    else:
        print("CPF ou senha incorretos.")


def listar_contas(usuarios):
    cpf = input("Digite o CPF: ")
    senha = input("Digite a senha: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario and usuario["senha"] == senha:
        for conta in usuario["contas"]:
            print(
                f"Conta {conta['numero_conta']} - Saldo: R${conta['saldo']:.2f} - Limite: R${conta['limite']:.2f}"
            )
    else:
        print("CPF ou senha incorretos.")


def depositar(conta, valor):
    conta["saldo"] += valor


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato, numero_saques


def verificar_limite(conta, valor):
    if valor > conta["limite"]:
        print("Valor excede o limite da conta.")
        return False
    return True


def menu():
    usuarios = []
    while True:
        print("\nMenu de Opções:")
        print("1. Criar novo usuário")
        print("2. Criar nova conta")
        print("3. Excluir conta")
        print("4. Listar contas")
        print("5. Depositar")
        print("6. Sacar")
        print("7. Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            criar_usuario(usuarios)
        elif opcao == 2:
            criar_conta(usuarios)
        elif opcao == 3:
            excluir_conta(usuarios)
        elif opcao == 4:
            listar_contas(usuarios)
        elif opcao == 5:
            cpf = input("Digite o CPF: ")
            numero_conta = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor a depositar: "))
            usuario = filtrar_usuario(cpf, usuarios)
            conta = next(
                (
                    conta
                    for conta in usuario["contas"]
                    if conta["numero_conta"] == numero_conta
                ),
                None,
            )
            if conta:
                depositar(conta, valor)
                print(f"Depósito de R${valor:.2f} realizado com sucesso!")
            else:
                print("Conta não encontrada.")
        elif opcao == 6:
            cpf = input("Digite o CPF: ")
            numero_conta = int(input("Digite o número da conta: "))
            senha = input("Digite a senha: ")
            valor = float(input("Digite o valor a sacar: "))
            usuario = filtrar_usuario(cpf, usuarios)
            conta = next(
                (
                    conta
                    for conta in usuario["contas"]
                    if conta["numero_conta"] == numero_conta
                ),
                None,
            )
            if conta and usuario["senha"] == senha:
                saldo, extrato, numero_saques = sacar(
                    saldo=conta["saldo"],
                    valor=valor,
                    extrato=conta["extrato"],
                    limite=conta["limite"],
                    numero_saques=conta["numero_saques"],
                    limite_saques=conta["limite_saques"],
                )
                conta["saldo"] = saldo
                conta["extrato"] = extrato
                conta["numero_saques"] = numero_saques
            else:
                print("Senha incorreta ou conta não encontrada.")
        elif opcao == 7:
            break
        else:
            print("Opção inválida. Tente novamente.")


# Executar o menu
menu()

# Explicação do Código

## Função `criar_usuario`

Esta função adiciona um novo usuário à lista de usuários, após garantir que o CPF fornecido não está em uso.

- **Entrada do CPF**: O usuário fornece o CPF.
- **Verificação de Existência**: Usa `filtrar_usuario` para verificar se o CPF já está registrado.
- **Cadastro de Novo Usuário**: Se o CPF não estiver em uso, coleta o nome, data de nascimento e endereço do usuário, além de criar uma senha.
- **Armazenamento**: Adiciona um novo dicionário de usuário à lista `usuarios`.
- **Mensagem de Sucesso**: Confirma a criação do usuário.

## Função `filtrar_usuario`

Essa função busca e retorna um usuário com o CPF especificado.

- **Busca**: Filtra a lista `usuarios` para encontrar um usuário com o CPF fornecido.
- **Retorno**: Retorna o primeiro usuário encontrado ou `None` se não houver correspondência.

## Função `criar_conta`

Cria uma nova conta para um usuário, se o CPF e a senha fornecidos forem válidos.

- **Entrada de CPF e Senha**: O usuário fornece CPF e senha.
- **Verificação de Usuário**: Verifica se o CPF e a senha estão corretos usando `filtrar_usuario`.
- **Criação da Conta**: Se válidos, cria uma nova conta e a adiciona à lista de contas do usuário.
- **Mensagem de Sucesso**: Confirma a criação da conta.

## Função `excluir_conta`

Remove uma conta específica de um usuário, dado o CPF e a senha corretos.

- **Entrada de Dados**: O usuário fornece CPF, número da conta e senha.
- **Verificação de Usuário e Conta**: Verifica a validade do CPF, senha e se a conta existe.
- **Remoção da Conta**: Se válidos, remove a conta da lista de contas do usuário.
- **Mensagem de Sucesso ou Erro**: Informa se a conta foi removida ou não encontrada.

## Função `listar_contas`

Lista todas as contas de um usuário específico após verificar o CPF e a senha.

- **Entrada de CPF e Senha**: O usuário fornece CPF e senha.
- **Verificação de Usuário**: Checa se o usuário existe e a senha está correta.
- **Listagem de Contas**: Imprime informações sobre cada conta do usuário.

## Função `depositar`

Adiciona um valor ao saldo da conta fornecida.

- **Entrada de Valores**: Recebe a conta e o valor a ser depositado.
- **Atualização do Saldo**: Adiciona o valor ao saldo da conta.

## Função `sacar`

Realiza um saque da conta, verificando saldo, limite e número de saques.

- **Verificações**: Confirma se o valor do saque não excede o saldo, o limite da conta e o número máximo de saques.
- **Atualização**: Deduz o valor do saldo e atualiza o extrato e o número de saques.
- **Mensagens de Erro ou Sucesso**: Informa se o saque foi realizado ou se houve falhas.

## Função `verificar_limite`

Verifica se um valor de saque excede o limite da conta.

- **Verificação**: Compara o valor do saque com o limite da conta.
- **Retorno**: Retorna `False` se o valor exceder o limite, caso contrário, `True`.

## Função `menu`

Exibe um menu de opções e executa as funções correspondentes com base na escolha do usuário.

- **Loop Infinito**: Mantém o menu ativo até que o usuário escolha sair.
- **Escolhas**: Dependendo da opção escolhida, chama as funções `criar_usuario`, `criar_conta`, `excluir_conta`, `listar_contas`, `depositar` ou `sacar`.
- **Saída**: Encerra o loop e o programa quando o usuário escolhe sair.

## Execução do Menu

Ao final do código, a função `menu` é chamada para iniciar a interação com o usuário e permitir a execução das opções disponíveis.

