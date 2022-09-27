from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas', 'cadastrar novas Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteudo de um arquivo!!!
        lerArquivo(arq)
    elif resposta == 2:
        #Opção de cadastrar uma noma pessoa
        cabeçalho('Novo Cadastro')
        nome = str(input('nome: '))
        idade =leiaint('idade: ')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        cabeçalho('Saindo do Sistema. . . Até logo!')
        break
    else:
        cabeçalho('\033[31mErro! Digite uma opção vàlida!\033[m')
    sleep(2)