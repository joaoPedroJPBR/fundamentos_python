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

#terceira questão
a = int(input('Digite o valor de a:'))
b = int(input('Digite o valor de b:'))
c = int(input('Digite o valor de c:'))

semiperimetro = (a + b + c) / 2 

heron = (semiperimetro * (semiperimetro - a) * (semiperimetro - b) * (semiperimetro - c)) ** 0.5

print('A área do triângulo é:', heron) 


#quarta questão
valor_inicial = float(input('Digite o valor inicial:'))
juros = float(input('Digite o valor do juros:'))
tempo = int(input('Digite o tempo em meses:'))

juros_simples = valor_inicial + (valor_inicial * (juros * 0.01) * tempo)
print('O valor final com juros simples é:', juros_simples)

#quinta questão
total_vendas = float(input('Digite o total de vendas do vendedor:'))
comissao = float(input('Qual a comissão do vendedor:'))
valor_final = total_vendas + (total_vendas * (comissao * 0.01))
print('O valor da comissáo foi de {}%, e o valor final das vendas foi R${:.2f}.'.format(comissao, valor_final))

#sexta questão
raio = int(input('Digite o raio do círculo:'))
area = 3.14 * (raio ** 2)

print('A área do círculo é:', area)


#sétima questão
nome_prod = input('Digite o nome do produto:')
custo_prod = float(input('Digite o custo de produção do produto:'))
valor_venda = float(input('Digite o valor de venda do produto:'))

lucro = valor_venda - custo_prod

print('O lucro obtido com a venda do produto {} foi de R${:.2f}'.format(nome_prod, lucro))


#oitava questão
temp = float(input('Digite a temperatura em graus Celsius:'))
fahrenheit = (temp * 9/5) + 32

print('A temperatura em Fahrenheit é:', fahrenheit)

#nona questão
valor_prod = float(input('Digite o valor do produto:'))
taxa_imposto = float(input('Digite a taxa de imposto:'))
valor_final = float(valor_prod) + (float(valor_prod) * (taxa_imposto * 0.01))
print('O valor final do produto com a taxa de imposto de {}% é R${:.2f}'.format(taxa_imposto, valor_final))

#décima questão
valor_compra = float(input('Digite o valor total da compra:'))
parcelas = int(input('Digite o número de parcelas:'))
valor_parcela = valor_compra / parcelas
print('O valor de cada parcela é R${:.2f}'.format(valor_parcela))