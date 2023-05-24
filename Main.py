class Main:
    pass

print("Testando o Projeto...")

from Cliente import Cliente
from Conta import Conta

c1 = Cliente("Augusto", "9999")
conta = Conta(c1._nome, 5624, 0)

print(conta._titular," Número: ",conta._numero,"Seu Saldo: ", conta._saldo)

conta.deposita(100)
conta.saque(50)
conta.extrato()