salario = float(input('Informe o Salário: '))

if salario <= 3000:
    print('Programador Junior')
elif salario > 3000 and salario <= 6000:
    print('Programador Pleno')
elif salario > 6000 and salario <= 15000:
    print("programador senior")
else:
    print("gerente de projetos")

# Algoritmo escrito:

# variavel salario recebe Leia('informe o salario: ')

# se salario menor ou igual a 3000 então
# escreva programador junior

# ou senão se salario maior que 3000 e menor ou igual 6000
# escreva programador pleno 

# ou senão se salario maior que 6000 e menor ou igual a 15000
#Escreva Programador Senior

#senão 
#Escreva Product Manager

