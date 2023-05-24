class Conta:
    def __init__(self, titular, numero, saldo):
        self._titular = titular
        self._numero = numero
        self._saldo = 0

    def get_titular(self):
        self._titular

    def get_numero(self):
        self._numero

    @property
    def saldo(self):
        self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if(saldo<0):
            print("Saldo não pode ser negativo")
        else:
            self._saldo = saldo
    def get_saldo(self):
        self._saldo

    def set_titular(self, titular):
        self._titular = titular

    def set_numero(self, numero):
        self._numero = numero

    def set_saldo(self, saldo):
        if (saldo<0):
            print("O saldo não pode ser negativo")
        else:
            self._saldo = saldo

    def saque(self, valor):
        if(self._saldo >= valor):
            self._saldo -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente")

    def deposita(self, valor):
        self.saldo = self._saldo + valor

    def extrato(self):
        print(f"Nome: {self._titular}\nSaldo Atual: {self._saldo}")