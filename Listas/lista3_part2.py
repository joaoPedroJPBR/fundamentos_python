#quinta questão   

nome = ''
idade = 0
altura = 0.0
altura_mais_alto = 0.0
idade_mais_alto = 0
nome_mais_alto = ''

for i in range(5):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    altura = float(input('Digite sua altura: '))
    
     # Verifica se essa pessoa é a mais alta até agora
    if altura > altura_mais_alto:
        nome_mais_alto = nome
        idade_mais_alto = idade
        altura_mais_alto = altura

print(f'A pessoa mais alta é {nome_mais_alto} com {altura_mais_alto}m de altura e {idade_mais_alto} anos.')


#sexta questão

lista = []
numero = 0

for i in range (10): 
    print('')
    numero = int(input('Digite um número: '))

    if numero % 2 == 0:
        lista.append(numero)

maior_par = max(lista)

print('O maior número par da lista é {}.'.format(maior_par))


