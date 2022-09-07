velocidade = float(input('Qual é a velocidade atual do carro? '))
multa = 0
if velocidade > 80:
    multa = (velocidade - 80) * 7.00
    print(f'MULTADO! Você excedeu o limite permitido que é de 80km/h\n'
          f'Você deve pagar uma multa de R${multa:.2f}!')
else:
    print('Tenha um bom dia! Dirija com segurança!')
