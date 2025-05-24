# Construa um programa onde o usuário digitará o seu peso e a sua altura e o programa
# irá calcular o IMC correspondente, Cao ele seja maior do que 25, ele deverá exibir:
# "Acima do peso ideal". Caso seja menor que 18, exibir "Abaixo do peso ideal". Por fim,
# se o resultado do cálculo entregar um valor entre 18 e 25, informar ao usuário que "O seu peso está OK".


#Solicitando peso e altura
Peso = float(input("Digite seu peso em Kg: "))
Altura = float(input("Digite sua altura em metros: "))

#Calculando IMC:
imc = Peso / (Altura ** 2)

#Resultado:
print(f"Seu IMC é: {imc:.2f}")

#Classificação:
if imc < 18:
    print("Abaixo do peso ideal")
elif 18.5 <= imc < 25:
    print("O seu peso está OK")
elif imc > 25:
    print("Acima do Peso ideal")
     