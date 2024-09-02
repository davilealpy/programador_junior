def minha_funcao(valor1, valor2):
    return valor1 + valor2

while True:
    print("="*50)
    valor1 = int(input("Valor1: "))
    valor2 = int(input("Valor2: "))

    resposta = minha_funcao(valor1, valor2)
    print(valor1,"+",valor2,"=", resposta)
    print("="*50)
