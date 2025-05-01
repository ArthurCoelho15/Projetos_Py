# Importando bibliotecas que auxiliarão no código
from time import sleep
from typing import List

# Importando pacotes python onde foram criadas as classes Cliente e Conta
from models.cliente import Cliente
from models.conta import Conta


contas: List[Conta] = []


def main() -> None:
    menu()

def menu() -> None:
    print('======================================================')
    print('---------__________ Bank of Recife __________---------')
    print('======================================================')

    print('Selecione uma opção no menu:\n'
          '1- Criar Conta\n'
          '2- Efetuar saque\n'
          '3- Efetuar deposito\n'
          '4- Efetuar transferência\n'
          '5- Listar contas\n'
          '6- Sair do sistema.')

    opcao: int = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Volte sempre')
        sleep(2)
        exit(0)
    else:
        print('Selecione uma opção válida!')
        menu()

def criar_conta() -> None:
    """

        * Cria a conta do usuário no banco *

        A função criar_conta necessitará de variáveis relacionadas ao nome, email, cpf e data de nascimento do usuário.

        Para a data de nascimento deverá estar no formato dd/mm/aaaa.

        Com o retorno da função o usuário poderá verificar as informações da sua conta.

    """
    print('Informe os dados do cliente\n')

    nome: str = input('Digite o nome do cliente: ')
    email: str = input('Digite o seu email: ')
    cpf: str = input('Digite seu CPF: ')
    data_nascimento: str = input('Utilize o formato dd/mm/aaaa para informar sua data de nascimento: ')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)
    conta: Conta = Conta(cliente)
    contas.append(conta)

    print('Conta criada com sucesso!')
    print('Dados da conta:')
    print('________________________')
    print(conta)
    sleep(2)
    menu()

def efetuar_saque() -> None:
    """

        * Efetua o saque na conta bancária do usuário *

        A função de saque apenas estará disponível para utilização caso houver contas criadas no banco.

        Nota-se que a função apenas funcionará caso um valor positivo seja fornecido pelo usuário.

    """
    if len(contas) <= 0:
        print('Ainda não há contas disponíveis...')
    else:
        numero: int = int(input('Informe o numero da sua conta: '))
        conta: Conta = buscar_conta_by_num(numero)

        if conta:
            valor: float = float(input('Informe o valor de saque: '))
            conta.sacar(valor)
        else:
            print(f'Não foram encontradas contas com esse número: {numero}')

    sleep(2)
    menu()

def efetuar_deposito() -> None:
    """

        * Efetua o depósito na conta bancária do usuário *

        A função de depósito apenas estará disponível para utilização caso houver contas criadas no banco.

        Nota-se que a função apenas funcionará caso um valor positivo seja fornecido pelo usuário.

        """
    if len(contas) <= 0:
        print('Ainda não há contas disponíveis...')
    else:
        numero: int = int(input('Informe o numero da sua conta: '))
        conta: Conta = buscar_conta_by_num(numero)

        if conta:
            valor: float = float(input('Informe o valor de depósito: '))
            conta.depositar(valor)
        else:
            print(f'Não foram encontradas contas com esse número: {numero}')

    sleep(2)
    menu()

def efetuar_transferencia() -> None:
    """

        * Faz a transferência de um valor monetário de uma conta de origem para uma conta de destino *

        A função utilizará variáveis para conta de origem, destinatário e valor de transferência.

        Nota-se que apenas poderá ser realizada corretamente caso houver contas criadas no banco, como também
        se os números das contas de origem e destinatário estiverem corretos.

        Para uma melhor utilização da função pode-se utilizar a função listar_contas como auxílio para o número das contas.

    """
    if len(contas) <= 0:
        print('Ainda não há contas disponíveis...')
        sleep(2)
        menu()
    else:
        main_conta: int = int(input('Informe o numero da sua conta: '))

        busca_main: Conta = buscar_conta_by_num(main_conta)

        if busca_main:
            dest_conta: int = int(input('Informe o numero da conta de destino: '))
            busca_dest: Conta = buscar_conta_by_num(dest_conta)

            if busca_dest:
                valor_transf: float = float(input('Informe o valor o qual deseja trasnferir: '))

                main_conta.transferir(dest_conta, valor_transf)
            else:
                print(f'Não foram encontradas contas com esse número: {busca_dest}!')
                efetuar_transferencia()
        else:
            print(f'Não foram encontradas contas com esse número!')
            efetuar_transferencia()

def listar_contas() -> None:
    """

        * Lista todas as contas cadastradas no banco *

    """
    if len(contas) <= 0:
        print('Ainda não há contas disponíveis...')
    else:
        for conta in contas:
            print('____________')
            print(conta)
            print('____________')
            sleep(1)
    sleep(2)
    menu()

def buscar_conta_by_num(numero: int) -> Conta:
    """

        * Realiza a busca da conta baseado no número (id) fornecido *

        Função de suporte para outras funções do código, como a função transferência

    """
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


if __name__ == '__main__':
    main()
