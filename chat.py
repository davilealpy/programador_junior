import os

mensagens = []

nome = input("Nome: ")

while True:

    #limpando terminal
    os.system('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])
    
    print("___________________")

    # obtendo texto
    texto = input("mensagens: ")
    if texto == "fim":
        break

    # adicionando mensagem na lista
    mensagens.append({
        "nome": nome,
        "texto": texto
    })