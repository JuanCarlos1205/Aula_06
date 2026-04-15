print('Insira os valores da venda')

resposta = 'S'
while resposta != 'N':
    v = float(input("Insira o valor da venda: "))
    if v >= 1000:
        d = 0.1*v 
        print(f'O valor da venda e: {v}')
        print(f'O valor de desconto e: {d}')
    else: 
        print(f'O valor da venda e: {v}')
    resposta = input('Quer continuar? [S/N]: ').upper().strip()[0]