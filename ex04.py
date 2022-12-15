#
# autores:
# Michel Silva
# Cristiano Fontes
#
# data: 12/12/2022

# 4. Faça um programa que leia vários inteiros positivos e mostre,
# no final, a soma dos números pares e a
# soma dos números ímpares. O programa deve parar
# quando entrar um número maior que 1000.

somaPar = 0 # soma dos números pares
somaImpar = 0 # soma dos números ímpares

valor = 0  # iniciando o valor com 0 para entrar no while
while (valor >= 0 and valor <= 1000): # enquanto o valor for positivo e menor que 1000
  valor = int(input("informe um valor: ")) # leia o valor
  if (valor >= 0 and valor <= 1000): # se o valor for positivo e menor que 1000
    if (valor % 2 == 0): # se o valor for par
      somaPar += valor
    elif (valor % 2 != 0): # se o valor for impar
      somaImpar += valor
  else:
    print(f"foi informado {valor}, saindo do laço de repetição") # se o valor for maior que 1000, saia do laço
    break

print(f"soma pares ={somaPar} e soma impares ={somaImpar}")
print("fim do programa")