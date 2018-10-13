num = int(input("Digite um inteiro:  "))
u = num%10
d = (num%100)//10
c = (num%1000)//100
m = (num%10000)//1000
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
