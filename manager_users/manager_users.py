from functions_manager_users import *

usuarios = {}
op = perguntar()

while op != "S":
        if op in ["I", "P", "E", "L", "T"]:
            #condição para Inserir (funções inserir e salvar registros)
            if op == "I":
                inserir(usuarios) 
                salvar(usuarios)
            
            #condição para Pesquisar
            elif op == "P":
                pesquisar()
        
            #condição para Excluir e salvar os usuários
            elif op == "E":
                excluir()
                
        
            #condição para Listar todos os usuários
            elif op == "L":
                listar()
            
            #condição para Excluir todos os registros do arquivo
            elif op == "T":
                limpar_arq()

        #Se o usuário não digitar uma opção válida, cai no loop infinito até digitar "S"
        else:
            print('\n======== ERRO ======== ' +
                   '\nNão foi digitada uma opção válida, por favor, tente novamente!'
                )
        op = perguntar()

print('\n-=-=-=-=-=-= SESSÃO ENCERRADA -=-=-=-=-=-=')
