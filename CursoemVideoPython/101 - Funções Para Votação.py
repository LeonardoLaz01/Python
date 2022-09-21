def voto(ano):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - ano
    if idade < 16:
        return f"Com {idade} anos: Voto negado."
    elif 16 <= idade < 18 or idade > 65:
        return f"Com {idade} anos: Voto opcional."
    else:
        return f"Com {idade} anos: Voto obrigatório."
    


print('-' * 40)
ano = int(input("Em que ano você nasceu? "))
print(voto(ano))
