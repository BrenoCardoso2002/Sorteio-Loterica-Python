# importações:
import random


# função que realiza os jogos:
def RealizaJogos(Jogos, Numeros, Arquivo):
    Lista = []
    while Jogos > 0:
        Jogos -= 1
        texto = ''
        for n in range(Numeros):
            sorteado = random.randint(1, 80)
            texto = texto + '{};'.format(sorteado)
        texto = texto[:-1]
        Lista.append(texto)
        # print(texto)
    # LancaTxt(Lista, Arquivo)
    LancaExcel(Arquivo, Lista)


# Função que faz um arquivo .txt com todos os numeros e jogos:
def LancaTxt(lista, Arquivo):
    f = open("{}.txt".format(Arquivo), "w")
    for n in range(len(lista)):
        print(lista[n])
        f.writelines('{}\n'.format(lista[n]))
    f.close()

	
# Função que faz um arquivo .csv com todos os numeros e jogos:
def LancaExcel(Arquivo, lista):
    f = open("{}.csv".format(Arquivo), "w")
    for n in range(len(lista)):
        print(lista[n])
        f.writelines('{}\n'.format(lista[n]))
    f.close()

# Tratamento de erro para o programa (verifica se o usuario não digitou um numero inteiro):
try:
    QJogos = int(input('Qual é a quantidade de jogos?\nR: '))
    QNumeros = int(input('Qual é a quantidade de numeros por jogos?\nR: '))
    Nome = input('Qual o nome do arquivo?\nR: ')
	
	# Exibe na tela os jogos:
    print('\nTodos os Jogos:')
    RealizaJogos(QJogos, QNumeros, Nome)

    print('\n<== FIM ==>')
except ValueError:
	# Menssagem de erro:
    print('Apenas numeros inteiros podem ser digitado!!!')
