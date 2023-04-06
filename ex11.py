def calcular_fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * calcular_fatorial(numero-1)
        
numero = int(input('Insira um numero: '))
fatorial = calcular_fatorial(numero)
print('O fatorial de', numero, 'é', fatorial)