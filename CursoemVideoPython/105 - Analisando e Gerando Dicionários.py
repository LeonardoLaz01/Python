from itertools import count


def notas(*nota, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param nota: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    aluno = dict()
    aluno['Total'] = len(nota)
    aluno['Maior'] = max(nota)
    aluno['Menor'] = min(nota)
    aluno['Média'] = sum(nota) / len(nota)
    if sit:
        if aluno['Média'] >= 7:
            aluno['Situação'] = 'Boa'
        elif aluno['Média'] <= 5:
            aluno['Situação'] = 'Ruim'
        else:
            aluno['Situação'] = 'Razoável'
    return aluno


resp = notas(5.5, 2.5, 1.5, sit='True')
print(resp)
