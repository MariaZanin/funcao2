def ano_bi(ano):
    if ano % 4 !=0:
        return False
    elif ano % 100 !=0:
        return True
    elif ano % 400 !=0:
        return False
    else:
        return True

# Anos para comparar

dados_teste = [1900,2002,2008,2012,2023]

# Resultado real

resultados_reais = [True, True, True, True, True]

# Checar função

for i in range(len(dados_teste)):
    yr = dados_teste[i]
    print(yr, '->', end='')
    result=ano_bi(yr)
    if result == resultados_reais[i]:
        print('É bissexto')
    else:
        print('Não é bissexto')
    