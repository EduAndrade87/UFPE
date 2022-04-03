somapares = somaimpares = n = 0
lista = []
num= []
for c in range(0,2):
    lista.append(float(input('numero: ')))

for i, v in enumerate(lista):
        num.append(int(v))

print(num)
for i, v in enumerate(num):
    if v % 2 == 0:
        somapares = somapares + v
    else:
        somaimpares = somaimpares + v
lista.clear()
print((-1) * somapares * somaimpares)
print(lista)