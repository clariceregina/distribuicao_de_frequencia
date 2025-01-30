from collections import Counter

dados = [0, 2, 3, 1, 2, 1, 4, 0, 3, 2, 1, 5, 4, 2, 3, 1, 0, 2, 1, 3]

#retorna um dicionário com chave igual ao número e valor igual a frequência com que aparece
frequencia_absoluta = Counter(dados)

print('Número | Frequência')
print('-------------------')

#key=lambda x: x[1] informa ao python para ordenar por valores e não pelas chaves
for chave, valor in sorted(frequencia_absoluta.items(), key=lambda x: x[1], reverse=True):
    print(f'   {chave}   |     {valor}')