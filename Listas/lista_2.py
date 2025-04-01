#primeira questao 
# est_civil = input('Digite o estado civil:')

# if est_civil == 's':
#     print('Estado civil: Solteiro!')
    
# elif est_civil == 'c':
#     print('Estado civil: Casado!')

# elif est_civil == 'v':
#     print('Estado civil: Viúvo!')
    
# elif est_civil == 'd':
#     print('Estado civil: Divorciado!')
    
# else :
#     print('Entrada inválida!')
        
        
#segunda questao  
# codigo = int(input('Digite o código do cargo:')) 
# salario =  float(input('Digite o salário do funcionário:'))
# aumento = 0
# cargo = ''

# if codigo == 1:
#     cargo = 'Secretário'
#     aumento = 45

# elif codigo == 2:
#     cargo = 'Tesoureiro'
#     aumento = 35

# elif codigo == 3:
#     cargo = 'Professor'
#     aumento = 25  
    
# elif codigo == 4:
#     cargo = 'Coordenador'
#     aumento = 15
    
# elif codigo == 5:
#     cargo = 'Diretor'
#     aumento = 0

# else: 
#     print('Código inválido!')
    
# reajuste = salario + (salario * (aumento * 0.01))

# print('O salário do funcionário com o cargo de {} foi reajustado para R${:.2f}'.format(cargo, reajuste))
    
    
#terceira questao
# dia = int(input('Digite o dia da semana:'))

# if dia == 1:
#     print('Domingo')

# elif dia == 2: 
#     print('Segunda-feira')

# elif dia == 3: 
#     print('Terça-feira')

# elif dia == 4: 
#     print('Quarta-feira')
    
# elif dia == 5: 
#     print('Quinta-feira')
    
# elif dia == 6: 
#     print('Sexta-feira')
    
# elif dia == 7:
#     print('Sábado')
    
# else: 
#     print('Valor inválido!')


#quarta questao
# infracao = int(input('Digite o número de infrações do motorista:'))

# if infracao == 0:
#     print('Motorista Exemplar!')
    
# elif infracao <= 3:
#     print('Motorista Atento!')
    
# elif infracao >= 4 and infracao <= 6:
#     print('Motorista Desatento!')
    
# elif infracao > 6:
#     print('Motorista Perigoso!')


#quinta questao
# suite = int(input('Digite o tipo de suíte:'))
# noites = int(input('Digite o número de noites que deseja ficar hospedado:'))
# valor_noites = 0.0
# valor_final = 0.0

# if suite == 1: 
#     if noites < 5:
#         print('O valor total da hospedagem é de R${:.2f}'.format(noites * 250))
#     elif noites >= 5 and noites <= 15:
#         valor_noites = noites * 250
#         valor_final = valor_noites - (valor_noites * 0.1)
#         print('O valor total da hospedagem é de R${:.2f}'.format(valor_final))  
#     else:
#         print('Limite de noites atingido.')

# elif suite == 2:
#     if noites < 5:
#         print('O valor total da hospedagem é de R${:.2f}'.format(noites * 500))
#     elif noites >= 5 and noites <= 10:
#         valor_noites = noites * 500
#         valor_final = valor_noites - (valor_noites * 0.1)
#         print('O valor total da hospedagem é de R${:.2f}'.format(valor_final))        
#     else:
#         print('Limite de noites atingido.')

# elif suite == 3:
#     if noites < 5:
#         print('O valor total da hospedagem é de R${:.2f}'.format(noites * 1200))
#     elif noites >= 5 and noites <= 7:
#         valor_noites = noites * 1200
#         valor_final = valor_noites - (valor_noites * 0.1)
#         print('O valor total da hospedagem é de R${:.2f}'.format(valor_final)) 
#     else:
#         print('Limite de noites atingido.')
    
# else: 
#     print('Tipo de suíte inválido!')
    
# print('Obrigado por escolher o Hotel Python!')


#sexta questao
# sessao = int(input('Digite o tipo da sessão:'))
# idade = int(input('Digite a idade do cliente:'))
# valor_ingresso = 0.0

# if sessao == 1: 
#     if idade < 12 or idade > 65:
#         valor_ingresso = 20 - (20 * 0.5)
#         print('O valor do ingresso é R${:.2f}'.format(valor_ingresso))
#     else: 
#         print('O valor do ingresso é R$20.00')
        
# elif sessao == 2: 
#     if idade < 12 or idade > 65:
#         valor_ingresso = 25 - (25 * 0.5)
#         print('O valor do ingresso é R${:.2f}'.format(valor_ingresso))
#     else: 
#         print('O valor do ingresso é R$25.00')
        
# elif sessao == 3: 
#     if idade < 12 or idade > 65:
#         valor_ingresso = 30 - (30 * 0.5)
#         print('O valor do ingresso é R${:.2f}'.format(valor_ingresso))
#     else: 
#         print('O valor do ingresso é R$30.00')

# else:
#     print('Tipo de sessão inválido!')
    
# print('Obrigado por escolher o Cine Python!')


#sétima questao
plano = input('Digite o tipo de plano:')
minutos = int(input('Digite a quantidade de minutos utilizados:'))
gigas = int(input('Digite a quantidade de gigas utilizados:'))
diferenca_gigas = 0.0
diferenca_tempo = 0.0  
tempo_final = 0.0
gigas_final = 0.0
valor_final = 0.0

if plano == 'basico':
    if minutos <= 100 and gigas <= 5:
        print('O valor total a ser pago é de R$50.00')
    else : 
        diferenca_tempo = minutos - 100
        tempo_final = 50 + diferenca_tempo * 1
        diferenca_gigas = gigas - 5
        gigas_final = diferenca_gigas * 10
        valor_final = tempo_final + gigas_final
        print(diferenca_gigas, diferenca_tempo, tempo_final, gigas_final)
        print('O valor total a ser pago é de R${:.2f}'.format(valor_final))

elif plano == 'intermediario':
    if minutos <= 300 and gigas <= 10:
        print('O valor total a ser pago é de R$80.00')
    else : 
        diferenca_tempo = minutos - 300
        tempo_final = 80 + diferenca_tempo * 1
        diferenca_gigas = gigas - 10
        gigas_final = diferenca_gigas * 10
        valor_final = tempo_final + gigas_final
        print('O valor total a ser pago é de R${:.2f}'.format(valor_final)) 
        
elif plano == 'avançado':
    if minutos <= 500 and gigas <= 20:
        print('O valor total a ser pago é de R$120.00')
    else : 
        diferenca_tempo = minutos - 500
        tempo_final = 120 + diferenca_tempo * 1
        diferenca_gigas = gigas - 20
        gigas_final = diferenca_gigas * 10
        valor_final = tempo_final + gigas_final
        print('O valor total a ser pago é de R${:.2f}'.format(valor_final))
        
else:
    print('Plano inválido!')
    
print('Obrigado por escolher a PythoNet!')
         