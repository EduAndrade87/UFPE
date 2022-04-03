pilha = []
expressao = str(input())
for simb in expressao:
    if simb in '{[(':
        pilha.append(simb)
    elif simb in ')]}':
        if len(pilha) == 0:
            pilha.append(simb)
        else:
            pilha.pop()
            break

if len(pilha) == 0:
    print('bem formado')
else:
    print('mal formado')
