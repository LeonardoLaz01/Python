from datetime import datetime
ano = int(input('Que ano quer analisar? coloque 0 para analisar o ano atual: '))
x = datetime.now()
if ano == 0:
    ano = x.year
if ano % 4 == 0:
    if ano % 100 != 0:
        print(f'O ano {ano} é bissexto')
    else:
        if ano % 400 == 0:
            print(f'O ano {ano} é bissexto')
        else:
            print(f'O ano {ano} não é bissexto')
else:
    print(f'O ano {ano} não é bissexto')
