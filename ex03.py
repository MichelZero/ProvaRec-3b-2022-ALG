#
# autores:
# Michel Silva
# Cristiano Fontes
#
# data: 15/12/2022

# 3. Leia 10 números do teclado e imprima o maior deles usando
# o laço de repetição for ou while.
#######################################################
#####    for    #####

# Inicializamos a variável que irá armazenar o maior número com o
# primeiro número digitado pelo usuário
maior = int(input("Digite o primeiro número: "))
# ou maior = 0

# Iniciamos o laço for que irá ler os próximos 9 números digitados pelo usuário
for i in range(1, 10):
    # Lê o próximo número digitado pelo usuário
    num = int(input(f"Digite o {i + 1}º número: "))
    # Verifica se o número é maior que o maior número armazenado até agora
    if num > maior:
        # Se for maior, atualiza o valor da variável maior
        maior = num

# Depois de ler e comparar todos os números, imprimimos o maior número encontrado
print(f"O maior número digitado foi {maior}.")






########################################################
# outra forma de fazer o exercício 3 usando o laço while
#####    while    #####

# Inicializamos a variável que irá armazenar o maior número com o primeiro 
# número digitado pelo usuário
maior = int(input("Digite o primeiro número: "))

# ou maior = 0

# Inicializamos a variável contadora com 1, já que o primeiro número foi lido acima
contador = 1

# Iniciamos o laço while
while contador < 10:
    # Lê o próximo número digitado pelo usuário
    num = int(input(f"Digite o {contador + 1}º número: "))
    # Verifica se o número é maior que o maior número armazenado até agora
    if num > maior:
        # Se for maior, atualiza o valor da variável maior
        maior = num
    # Incrementa a variável contadora
    contador += 1

# Depois de ler e comparar todos os números, imprimimos o maior número encontrado
print(f"O maior número digitado foi {maior}.")
