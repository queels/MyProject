#Contrua um programa que faça uma contagem regressiva de 10 até 0 e no final dela, exiba uma mensagem
# de sua preferencia.
#Use For e While.

#Contagem regressiva de 10 - 0 usando For:
Numero = int(input("Digite o numero DEZ: "))
for Contador in range(Numero, -1, -1):
    print("Numero", Contador)
print("Parabéns, você conseguiu esperar!")

#Contagem regressiva usando While:
import time
i = 10
while i >= 0:
    print(i)
    time.sleep(1)
    i -= 1
print("Parabéns, você esperou a contagem!")
