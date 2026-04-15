#vCalcula media - 1 aluno

#n1 = float(input('Nota 1: '))
#n2 = float(input('Nota 2: '))
#media = (n1 + n2)/2
#print(media)

# Estrutura de repeticao - For

# for i in range(5):
#    print('Ola mundo!')

qtd = int(input('Quer contar ate quanto?: '))
for i in range(1, qtd):
    print(i, end= " ")


for u in range(3):
    print(f'\nRodada {u+1}')
    num1 = int(input('Informe numero: '))
    num2 = int(input('Informe o segundo numero: '))
    soma = num1 + num2
    print(f'O total e: {soma}')


# Variavel Acumuladora

soma = 0
for i in range(5):
    numero = float(input('Digite um numero: '))
    soma = soma + numero

print(f'Total e: {soma}')


soma = 0
for v in range(5):
    venda = float(input('Informe o valor: '))

    if venda > 100:
        #venda = soma + venda
        soma += venda
        print(f'Valor R$ {venda} somada')
    else:
        print('Valor no computado')
print(f'\n Total de R$ {soma}')


# Atividade01

n = int(input('Insira a quantidade de alunos: '))
r = int(input('Insira a quantidade de notas: '))

for i in range(n):
    p = 0
    print(f'Insira as notas do aluno {i+1}: ')   
    for j in range(r):
        m = int(input('Insira nota:' ))
        p = p + m
    total = p/r
    print(f'O promedio do aluno {i+1} e: {total}')

        

    