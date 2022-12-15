#
# autores:
# Michel Silva
# Cristiano Fontes
#
# data: 12/12/2022

# 4.	Escreva um programa que pergunte ao usuário se deseja 
# continuar executando o programa e só saia do laço while se 
# o usuário responder "não".

# Iniciamos o laço while
while True:
    # Pergunta ao usuário se deseja continuar executando o programa
    continuar = input("Deseja continuar executando o programa (s/n)? ")
    # Verifica se a resposta do usuário é "não"
    if continuar == "n":
        # Se for "não", sai do laço while
        break
    # Se a resposta for diferente de "não", o programa continua executando
    # ...
