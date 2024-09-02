#for x in range(10):
   # print(x)

#for: loop que percorre sequências repetindo ações para cada elemento

#while: Loop que executa ações enquanto a condição for verdadeira

#exemplo com for:
#notas = []

#for x in range(5):
    #codigo_aluno = input("RM: ")
    #nota = float(input("Nota:"))
    #resultado = [codigo_aluno, nota]
    #notas.append(resultado)

#print(  "Quantidade De Notas", len(notas)   )

#for n in notas:
    #codigo_aluno = n[0]
    #nota = n[1]
    #print("O RM", codigo_aluno, "Tirou a nota:", nota)

#exemplo com while:

notas = []

contador = 1

while contador <= 5:
    codigo_aluno = input('RM: ')
    nota = float(input('Nota; '))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

    #alternativa contador += 1
    contador = contador + 1

print( "quantidade de notas",  len(notas))