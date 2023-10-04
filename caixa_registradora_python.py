saldo = 1000

print("escreva o que deseja realizar: \n1 - saque \n2 - deposito \n3 - verificação saldo")
opcao = int(input("informe a operação desejada: "))


if opcao == 1:
    saque = float(input("digite o valor de retirada: "))
    while saque > saldo:
        print("saldo insuficiente, saldo atual: ",saldo)
        saque = float(input("digite o valor de retirada: "))
    saldo -= saque
    print("seu novo saldo é: ",saldo)

elif opcao == 2:
    deposito = float(input("insira o valor do deposito: "))
    saldo += deposito
    print("seu novo valor de saldo é: ",saldo)
elif opcao == 3: 
    print("seu saldo é: ", saldo)
else:
    print("opcao invalida")
