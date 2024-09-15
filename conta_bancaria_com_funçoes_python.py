def criar_conta(banco):
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")
    senha = input("Digite a senha: ")
    numero_conta = len(banco.get(cpf, [])) + 1
    nova_conta = {
        "nome": nome,
        "numero_conta": numero_conta,
        "saldo": 0.0,
        "senha": senha,
    }
    if cpf in banco:
        banco[cpf].append(nova_conta)
    else:
        banco[cpf] = [nova_conta]
    print(f"Conta {numero_conta} criada com sucesso!")
    return nova_conta


def excluir_conta(banco):
    cpf = input("Digite o CPF: ")
    numero_conta = int(input("Digite o número da conta a ser excluída: "))
    senha = input("Digite a senha: ")
    if cpf in banco:
        conta = next(
            (conta for conta in banco[cpf] if conta["numero_conta"] == numero_conta),
            None,
        )
        if conta and conta["senha"] == senha:
            banco[cpf] = [
                conta for conta in banco[cpf] if conta["numero_conta"] != numero_conta
            ]
            if not banco[cpf]:
                del banco[cpf]
            print(f"Conta {numero_conta} excluída com sucesso!")
        else:
            print("Senha incorreta ou conta não encontrada.")
    else:
        print("CPF não encontrado.")


def listar_contas(banco):
    cpf = input("Digite o CPF: ")
    if cpf in banco:
        for conta in banco[cpf]:
            print(
                f"Conta {conta['numero_conta']} - Nome: {conta['nome']} - Saldo: R${conta['saldo']:.2f}"
            )
    else:
        print("CPF não encontrado.")


def depositar(conta, valor):
    conta["saldo"] += valor


def sacar(banco):
    cpf = input("Digite o CPF: ")
    numero_conta = int(input("Digite o número da conta: "))
    senha = input("Digite a senha: ")
    valor = float(input("Digite o valor a sacar: "))
    conta = next(
        (
            conta
            for conta in banco.get(cpf, [])
            if conta["numero_conta"] == numero_conta
        ),
        None,
    )
    if conta and conta["senha"] == senha:
        if valor <= conta["saldo"]:
            conta["saldo"] -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente.")
    else:
        print("Senha incorreta ou conta não encontrada.")


def menu():
    banco = {}
    while True:
        print("\nMenu de Opções:")
        print("1. Criar nova conta")
        print("2. Excluir conta")
        print("3. Listar contas")
        print("4. Depositar")
        print("5. Sacar")
        print("6. Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            criar_conta(banco)
        elif opcao == 2:
            excluir_conta(banco)
        elif opcao == 3:
            listar_contas(banco)
        elif opcao == 4:
            cpf = input("Digite o CPF: ")
            numero_conta = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor a depositar: "))
            conta = next(
                (
                    conta
                    for conta in banco.get(cpf, [])
                    if conta["numero_conta"] == numero_conta
                ),
                None,
            )
            if conta:
                depositar(conta, valor)
                print(f"Depósito de R${valor:.2f} realizado com sucesso!")
            else:
                print("Conta não encontrada.")
        elif opcao == 5:
            sacar(banco)
        elif opcao == 6:
            break
        else:
            print("Opção inválida. Tente novamente.")


# Executar o menu
menu()
