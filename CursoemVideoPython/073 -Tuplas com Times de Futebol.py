times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético',
         'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba',
         'Avaí', 'Ponte Preta', 'Atlético-GO')
print('Lista do Brasileirão:', times)
print('-=' * 10)
print('Os 5 primeiros são', times[0:5])
print('-=' * 10)
print('Os 4 últimos são', times[-4:])
print('-=' * 10)
print('Times em ordem alfabética:', sorted(times))
print('-=' * 10)
print(f'O chapecoense está na {times.index("Chapecoense")+1}ª posição')
