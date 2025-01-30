import numpy as np
import pandas as pd

dados = [12, 25, 32, 45, 51, 29, 38, 42, 55, 60, 15, 22, 30, 50, 48, 35, 40, 43, 57, 20, 18, 36, 41, 47, 52, 39, 33, 44, 37, 19]

amplitude_total = max(dados) - min(dados)

#regra de Sturges para determinar o número adequado de intervalos de classe
#np.ceil arredonda para cima
n = len(dados)
k = int(np.ceil(1 + 3.322 * np.log10(n)))

#definir intervalos de classe - divide o intervalo total em k partes
#np.linspace cria uma sequência de números igualmente espaçados entre dois números: um valor inicial e um valor final
intervalos = np.linspace(min(dados), max(dados), k + 1)

#exibir os intervalos de classe
print('Intervalos de Classe: \n')
print(f'-> amplitude = {k}')
print()
for i in range(len(intervalos) - 1):
    print(f'({intervalos[i]:.1f}, {intervalos[i+1]:.1f})')


