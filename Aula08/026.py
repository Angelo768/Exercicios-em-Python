frase = input("Escreva uma frase: ").lower().strip().split()
junto = ''.join(frase)
A = junto.count('a')
first = junto.find('a')
last = junto[::-1].find('a')
print(f'Letra A aparece {A} vezes na frase')
print(f'A primeira aparição de A é na posição {first}')
print(f'A última aparição de A é na posição {last}')
