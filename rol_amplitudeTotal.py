#lista de dados brutos
#dados = [5, 8, 10, 12, 6, 7, 9, 5, 11, 15, 14, 7, 10, 6, 13, 9, 12, 8, 7, 10]

dados = []
while True:
    print('Insira o ' + str(len(dados)+1) + '° número: ')
    print('(para interromper o programa aperte ENTER)')
    numero = input()
    if numero == '':
        break
    dados.append(float(numero))

#organizar em rol (ordem crescente)
rol = sorted(dados)

#calcular amplitude total
amplitude_total = max(dados) - min(dados)

#exibir resultados
print(f'Rol (ordem crescente): {rol}')
print(f'A amplitude dos dados é: {amplitude_total}')