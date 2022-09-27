def notas(*n,sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita varias)
    :param sit: Valor opcional, indicando se deve ou naõ adicionar a situação.
    :return: dicionario com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'Boa'
        elif r['média'] >= 5:
            r['situação'] = 'Razoavel'
        else:
            r['situação'] = 'Ruim'
    return r


#Programa Principal
resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)