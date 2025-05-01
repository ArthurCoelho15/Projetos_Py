# Importando bibliotecas que auxiliarão no código
from models.cliente import Cliente
from utils.helper import formata_float


class Conta:

    id: int = 1001

    def __init__(self: object, cliente: Cliente) -> None:
        self.__num_conta: int = Conta.id
        self.__cliente: Cliente = cliente
        self.__saldo: float = 0.0
        self.__limite: float = 1000.00
        self.__saldo_disponivel: float = self._calculo_saldo_total
        Conta.id += 1

    def __str__(self: object) -> str:
        return (f'Numero da conta: {self.numero}\n'
                f'Cliente: {self.cliente.nome}\n'
                f'Saldo em conta: {formata_float(self.saldo_disponivel)}')

    @property
    def numero(self: object) -> int:
        return self.__num_conta

    @property
    def cliente(self: object) -> Cliente:
        return self.__cliente

    @property
    def saldo(self: object) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self: object, valor: float) -> None:
        self.__saldo = valor

    @property
    def limite(self: object) -> float:
        return self.__limite

    @limite.setter
    def limite(self: object, valor: float) -> None:
        self.__limite = valor

    @property
    def saldo_disponivel(self: object) -> float:
        return self.__saldo_disponivel


    @saldo_disponivel.setter
    def saldo_disponivel(self: object, valor: float) -> None:
        self.__saldo_disponivel = valor


    @property
    def _calculo_saldo_total(self: object) -> float:
        return self.saldo + self.limite

    def depositar(self: object, valor: float) -> None:
        if valor > 0:
            self.saldo = self.saldo + valor
            self.saldo_disponivel = self._calculo_saldo_total
            print(f'Deposito de {valor} efetuado com sucesso!')
        else:
            print('Erro ao efetuar depósito. Tente novamente')

    def sacar(self: object, valor: float) -> None:
        """
        calcularemos se há saldo na conta corrente + limite para a transação, caso houver, veremos se temos saldo suficiente
        na conta-corrente. Teremos duas situações:

        1º Saldo OK na conta-corrente: abateremos o valor da conta-corrente sem alterar o limite de crédito
        2º Saldo NOK na conta-correte: abateremos o valor total da conta corrente e o restante abaterá no limite de crédito

        """
        if valor > 0 and self.saldo_disponivel >= valor:
            if self.__saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_disponivel = self._calculo_saldo_total
            else:
                restante: float = self.saldo - valor
                self.limite = self.limite + restante
                self.saldo = 0
                self.saldo_disponivel = self._calculo_saldo_total
                print(f'Saque de {valor} realizado com sucesso!')
        else:
            print('Saque não realizado. Tente novamente.')

    def transferir(self: object, destino: object, valor: float) -> None:
        """
        self está relacionado com a conta de origem, destino a conta de destino, valor com o valor da transação.

        calcularemos se há saldo na conta corrente + limite para a transação, caso houver, veremos se temos saldo suficiente
        na conta-corrente. Teremos duas situações:

        1º Saldo OK na conta-corrente: abateremos o valor da conta-corrente sem alterar o limite de crédito
        2º Saldo NOK na conta-correte: abateremos o valor total da conta corrente e o restante abaterá no limite de crédito

        """
        if valor > 0 and self.saldo_disponivel >= valor:
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_disponivel = self._calculo_saldo_total
                destino.saldo = destino.saldo + valor
                destino.saldo_disponivel = destino._calculo_saldo_total
                print(f'Transferência de {valor} realizada com sucesso para {destino.Conta.nome}')
            else:
                restante: float = self.saldo - valor
                self.saldo = 0
                self.saldo_disponivel = self.saldo_disponivel
                print(f'Transferência de {valor} realizada com sucesso para {destino.Conta.nome}.\n'
                      f'Sua conta está zerada e você está atualmente utilizando o limite de crédito.')
        else:
            print('A transferência não pôde ser realizada. Tente novamente.')
