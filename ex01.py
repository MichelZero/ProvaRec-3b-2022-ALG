#
# autores:
# Michel Silva
# Cristiano Fontes
#
# data: 15/12/2022

# 1. Imprima todos os números múltiplos de 3 entre 0 e 100 usando 
# o laço de repetição while.

i = 0 # variável de controle
while i <= 100:
    if i % 3 == 0:
        print(i)
    i += 1
    
print('Fim do programa')