def calcular_media(notas):
    total = sum(notas)
    media = total/len(notas)  #colocar len pra nao ter que defindir o numero exato de elementos a se dividir. len puxa a lista inteira independente do tamanhao.
    return media
    
notas = [7.5,8.0,6.5,9.0]
media = calcular_media(notas)
print('A média é: ', media)