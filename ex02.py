#
# autores:
# Michel Silva
# Cristiano Fontes
#
# data: 15/12/2022


# 2. solicite ao usuário um número inteiro positivo N, calcule a soma dos N primeiros 
# números pares usando o laço de repetição while.
# ex: N = 5 -> 0 + 2 + 4 + 6 + 8 = 20

numero = int(input('Digite um número inteiro positivo: '))

i = 0 # variável de controle (inicializada em 0), nesse caso, o número par atual (0, 2, 4, 6, 8, ...)
soma = 0 # variável acumuladora

while i < numero: # enquanto i for menor que o número digitado pelo usuário (numero) faça: 
    # print(i) # imprime o número par atual (opcional)
    soma += 2 * i # adiciona o próximo número par à soma atual (2 * i)
    # print(soma) # imprime a soma atual (opcional)
    i += 1 # incrementa a variável de controle (i) em 1 unidade (i += 1)
    
    
print('A soma dos números pares é: ', soma) # imprime a soma final (fora do laço)
print('Fim do programa')
