nome = input('Nome Completo: ')
print(f'Em minusculo: {nome.lower()}')
print(f'Em maiusculo: {nome.upper()}')
junto = "".join(nome.split())
print(f'Seu nome tem {len(junto)} letras')
print(f'Seu primeiro nome tem {len(nome.split()[0])} letras')
