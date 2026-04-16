# Estrutura de repeticao While
# Numeros ate 10

i = 1
while i <= 10:
    print(i)
    i += 1


# Exemplo 02

n = 1
soma = 0
while n != 0:
    n = int(input('Digite um numero: '))
    soma += n

print(f'O total foi: {soma}') 

# Exemplo 03

resposta = 'S'
soma = 0
while resposta != 'N':
    n = int(input('Informe um numero: '))
    soma += n 
    resposta = input('Quer continuar? [S/N]: ').upper().strip()[0]
print(f'O total da soma e: {soma}')


# Atividade 02

print('Insira os valores da venda')

resposta = 'S'
while resposta != 'N':
    v = float(input("Insira o valor da venda: "))
    if v > 1000:
        d = 0.1*v 
        v -= d 
        print(f'O valor da venda e: {v}')
        print(f'O valor de desconto e: {d}')
    else: 
        print(f'O valor da venda e: {v}')
    resposta = input('Quer continuar? [S/N]: ').upper().strip()[0]
print('Programa encerrado')

