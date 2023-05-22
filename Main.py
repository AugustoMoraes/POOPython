class Main:
    pass

print("Testando o Projeto...")

from Cliente import Cliente
from Conta import Conta

c1 = Cliente("Augusto", "9999")
conta = Conta(c1.nome, 5624, 0)

print(conta.titular," Número: ",conta.numero,"Seu Saldo: ", conta.saldo)