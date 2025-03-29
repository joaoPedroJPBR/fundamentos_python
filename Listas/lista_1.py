#primeira questão

graus = int(input('Digite um angulo em graus:'))
radianos = graus * 3.14 / 180
print('O angulo em radianos é:', radianos)

#segunda questão
name = input('Digite o nome do produto:')
preco = float(input('Digite o preço do produto:'))
valor_desconto = float(input('Digite o valor do desconto:'))
desconto = preco * (valor_desconto * 0.01)
novo_preco = float(preco) - float(desconto)
print('O preço de {}, com {}% de desconto é R${:.2f}'.format(name, valor_desconto, novo_preco))
