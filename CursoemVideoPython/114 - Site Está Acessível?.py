import urllib.request

try:
    x = (urllib.request.urlopen('http://pudim.com.br/').getcode())
except:
    print('Não consegui acessar o site')
else:
    print('Consegui acessar o site Pudim com sucesso!')
