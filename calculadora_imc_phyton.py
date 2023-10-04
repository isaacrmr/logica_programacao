peso = float(input("insira seu peso em (kg): "))
altura = float(input("insira sua altura (m): "))
imc = peso/(altura*2)
print("seu imc é igual a:",round(imc,2))

if imc < 18.5:
    print("abaixo do peso")
elif imc < 24.9:
    print("pessoa normal")
elif imc < 29.9:
    print("sobrepeso")
else:
    print("obeso")