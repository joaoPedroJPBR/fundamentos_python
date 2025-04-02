#primeira questao

total_idade = 0
soma_idade = 0
media_idade = 0.0
maiores_vinte_e_cinco = 0
menores_vinte_e_cindo = 0

while True: 
    idade = int(input('Digite a idade o usuário:'))
    if idade == -1:
        break
    else:
        total_idade += 1
        soma_idade += idade
        media_idade = soma_idade / total_idade
        if idade >= 25:
            maiores_vinte_e_cinco += 1
        else:  
            menores_vinte_e_cindo += 1

print('Saída:')
print('O total de idades é:', total_idade)    
print('A média de idade dos usuários é:', media_idade)
print('O total de usuários com 25 anos ou mais é:', maiores_vinte_e_cinco)
print('O total de usuários com menos de 25 anos é:', menores_vinte_e_cindo)


#segunda questão
soma_notas = 0
qtd_notas = 0
media_notas = 0.0

while True: 
    nota = int(input('Digite a nota do produto:'))
    if nota == -1:
        print('Nota inválida!')
        break
    else:
        soma_notas += nota
        qtd_notas += 1
        media_notas = soma_notas / qtd_notas
        
print('Saída:')
print('A média das notas é:{:.2f}'.format(media_notas))


#terceira questão
qtd_tipo = 0 
qtd = 0

while True: 
    print('')
    produto = input('Digite o nome do produto ou FIM para sair do programa:')
    if produto == 'FIM':
        print('FIM:')
        break
    else:
        qtd = int(input('Digite a quantidade do produto:'))
        if qtd < 0:
            print('Não é possível cadastro de estoque negativo.')
        else:
            qtd_tipo += 1

print('Saída:')
print('Tipos de produtos cadastrados:', qtd_tipo)
print('Obrigado por acessar o PythonCenter!')


#quarta questão 
print('1 - Banho;',
      '2 - Tosa;',
      '3 - Banho e Tosa;',
      '4 - Outros;')

banho = 0
tosa = 0
banho_e_tosa = 0
outros = 0

cont = 10
while cont > 0:
    cont -= 1
    servico = int(input('Digite o serviço desejado:'))
    if servico == 1:
       banho += 1
    elif servico == 2:
        tosa += 1
    elif servico == 3:
        banho_e_tosa += 1
    elif servico == 4:
        outros += 1
    else:
        print('Serviço inválido!')
    
print('Saída:')
print('Banho:', banho)
print('Tosa:', tosa)
print('Banho e Tosa:', banho_e_tosa)
print('Outros:', outros)
print('Volte sempre ao PetPython!')