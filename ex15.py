# palindromo - Palavra ou Frase que se pode ler em qualquer sentido que é sempre igual

def veriricar_palindromo(texto):
    texto = texto.lower().replace(' ', '')
    
    return texto == texto[::-1]
    
#texto [::-1] inverte o texto

texto = 'Socorram me subi no onibus em Marrocos'

if veriricar_palindromo(texto):
    print(texto, 'é um palíndromo.')
else:
    print(texto, 'não é um palíndromo.')