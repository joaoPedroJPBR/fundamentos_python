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


# #sexta questão

lista = []
numero = 0

for i in range (10): 
    print('')
    numero = int(input('Digite um número: '))

    if numero % 2 == 0:
        lista.append(numero)

maior_par = max(lista)

print('O maior número par da lista é {}.'.format(maior_par))


#sétima questão

#codigo
codigo_mais_alto = codigo_mais_baixo = codigo_mais_pesado = codigo_mais_leve = None

#altura
altura_mais_alto = altura_mais_baixo = altura_mais_leve = altura_mais_pesado = 0.0

#peso 
peso_mais_alto = peso_mais_baixo = peso_mais_pesado = peso_mais_leve = 0

#soma
soma_alturas = soma_pesos = 0

qtd_clientes = int(input('Digite a quantidade de clientes: '))

for i in range (qtd_clientes):
    print(f"")
    cod = int(input('Digite o código do cliente: '))
    altura = float(input('Digite a altura do cliente: '))
    peso = float(input('Digite o peso do cliente: '))
    
    soma_alturas += altura
    soma_pesos += peso
    
    if i == 0:
        codigo_mais_alto = codigo_mais_baixo = codigo_mais_pesado = codigo_mais_leve = cod
        altura_mais_alto = altura_mais_baixo = altura_mais_leve = altura_mais_pesado = altura
        peso_mais_pesado = peso_mais_leve = peso_mais_alto = peso_mais_baixo = peso
    else:
        if altura > altura_mais_alto:
            codigo_mais_alto = cod
            altura_mais_alto = altura
            peso_mais_alto = peso
            
        if altura < altura_mais_baixo:
            codigo_mais_baixo = cod
            altura_mais_baixo = altura
            peso_mais_baixo = peso
            
        # Verificando mais pesado e mais leve
        if peso > peso_mais_pesado:
            codigo_mais_pesado = cod
            peso_mais_pesado = peso
            altura_mais_pesado = altura
        if peso < peso_mais_leve:
            codigo_mais_leve = cod
            peso_mais_leve = peso
            altura_mais_leve = altura
            
media_alturas = soma_alturas / qtd_clientes
media_pesos = soma_pesos / qtd_clientes

print('O cliente mais alto tem: Código {}, altura {} e peso {}.'.format(codigo_mais_alto, altura_mais_alto, peso_mais_alto))
print('O cliente mais baixo tem: Código {}, altura {} e peso {}.'.format(codigo_mais_baixo, altura_mais_baixo, peso_mais_baixo))
print('O cliente mais pesado tem: Código {}, altura {} e peso {}.'.format(codigo_mais_pesado, altura_mais_pesado, peso_mais_pesado))
print('O cliente mais leve tem: Código {}, altura {} e peso {}.'.format(codigo_mais_leve, altura_mais_leve, peso_mais_leve))
print('A média de altura dos clientes é: {:.2f}.'.format(media_alturas))
print('A média de peso dos clientes é: {:.2f}.'.format(media_pesos))
print('Obrigado por frequentar a Python Academy!')


#oitava questão

qtd_clientes = int(input('Digite a quantidade de clientes: '))
qtd_clientes_contemplados = 0
bonus = 0.0

for i in range (qtd_clientes):
    print(f"")
    nome = input('Digite o nome do cliente: ')
    valor_total_compras = float(input('Digite o valor total das compras: '))
    
    if valor_total_compras > 2000:
        bonus = bonus + (valor_total_compras * 0.15)
        qtd_clientes_contemplados += 1
        print('Cliente apto para receber o bonus!')
    
print('A quantidade de clientes contemplados é: {}.'.format(qtd_clientes_contemplados))
print('O valor total do bônus é: {:.2f}.'.format(bonus))



#nona questão
mes =  0
total_vendas = maior_venda = mes_maior_venda = 0.0

for i in range (20):
    print(f"")
    mes += 1
    valor = float(input('Digite o valor do mês: '))
    total_vendas += valor
    
    if i == 0:
        maior_venda = valor
        mes_maior_venda = mes
    else: 
        if valor > maior_venda:
            maior_venda = valor
            mes_maior_venda = mes
        else:
            menor_venda = valor
            mes_menor_venda = mes

if mes_maior_venda == 1:
    mes_maior_venda = 'Janeiro'
elif mes_maior_venda == 2:  
    mes_maior_venda = 'Fevereiro'
elif mes_maior_venda == 3:  
    mes_maior_venda = 'Março'
elif mes_maior_venda == 4:   
    mes_maior_venda = 'Abril'
elif mes_maior_venda == 5:                  
    mes_maior_venda = 'Maio'
elif mes_maior_venda == 6:  
    mes_maior_venda = 'Junho'
elif mes_maior_venda == 7:   
    mes_maior_venda = 'Julho'
elif mes_maior_venda == 8:  
    mes_maior_venda = 'Agosto'
elif mes_maior_venda == 9:  
    mes_maior_venda = 'Setembro'
elif mes_maior_venda == 10:  
    mes_maior_venda = 'Outubro'
elif mes_maior_venda == 11:  
    mes_maior_venda = 'Novembro'
elif mes_maior_venda == 12:  
    mes_maior_venda = 'Dezembro'

if mes_menor_venda == 1:
    mes_menor_venda = 'Janeiro'
elif mes_menor_venda == 2:
    mes_menor_venda = 'Fevereiro'
elif mes_menor_venda == 3:
    mes_menor_venda = 'Março'
elif mes_menor_venda == 4:
    mes_menor_venda = 'Abril'
elif mes_menor_venda == 5:
    mes_menor_venda = 'Maio'
elif mes_menor_venda == 6:
    mes_menor_venda = 'Junho'
elif mes_menor_venda == 7:
    mes_menor_venda = 'Julho'
elif mes_menor_venda == 8:
    mes_menor_venda = 'Agosto'
elif mes_menor_venda == 9:
    mes_menor_venda = 'Setembro'
elif mes_menor_venda == 10:
    mes_menor_venda = 'Outubro'
elif mes_menor_venda == 11:
    mes_menor_venda = 'Novembro'
elif mes_menor_venda == 12:
    mes_menor_venda = 'Dezembro'
    
print('O mês com maior venda foi {} com o valor de {:.1f}.'.format(mes_maior_venda, maior_venda))
print('O mês com menor venda foi {} com o valor de {:.1f}.'.format(mes_menor_venda, menor_venda))
print('O total de vendas no ano foi de {:.1f}.'.format(total_vendas))


# décima questão
lista_num = []

for i in range (2):
   num = int(input('Digite um número: '))
   lista_num.append(num)

for i in range (20):
    prox = lista_num[-1] + lista_num[-2]#a lista começa do 0, então o -1 é o último elemento e o -2 é o penúltimo
    lista_num.append(prox)

print('Fibonacci:')
print(lista_num)


