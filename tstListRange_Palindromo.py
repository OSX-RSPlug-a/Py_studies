

def result(palavra):
    palavra_min = palavra.lower()
    palavra_invertida = palavra_min[::-1]
    if palavra_min == palavra_invertida:
        print("É palíndromo.")
    else:
        print("Não é palíndroma.")
    print()
    print('Sua palavra: ', end='')
    print(palavra)
    print('Inversão: ', end='')
    print(palavra_invertida)


word=input('Digite uma palavra: ')
print(result(word))