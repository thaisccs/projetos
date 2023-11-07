#CRIANDO FUNÇÕES PARA O MANAGER USERS PROGRAM

#função01: listar todas as opções do menu
def perguntar():
    print('\n-=-=-=-=-=-= MANAGER USERS PROGRAM -=-=-=-=-=-=\n')
    return input('O que deseja realizar?\n' +
            '<I> - Para INSERIR um usuário\n' +
            '<P> - Para PESQUISAR um usuário\n' +
            '<E> - Para EXCLUIR um usuário\n' +
            '<L> - Para LISTAR todos os usuários\n' +
            '<A> - Para EXCLUIR ARQUIVO com todos os usuários\n' +
            '<S> - Para SAIR do programa:  ').upper()


#função 02: inserindo os dados informado pelo usuário no dicionário de lista, onde a chave é o login do usuário e as demais informações preenchem a lista.
def inserir(dicionario):
    dicionario[input('Digite o login: ').upper()] = [input('Digite o nome: ').upper(),
                                                   input('Digite a última data de acesso: '),
                                                   input('Qual a última estação acessada: ').upper()]


#função 03: salvando cada usuário no arquivo txt e verificando se há usuários duplicados pelo login (info única de cada usuário)
def salvar(dicionario):
        #abrindo arquivo no modo read para ler cada linha como um registro da lista 
        with open('manager_users.txt', 'r') as leitura:
                conteudo = leitura.readlines()
                usuarios_existentes = [linha.split(':')[0] for linha in conteudo] #extraindo apenas o login do usuário
        
        #abrindo arquivo no modo append:
        with open('manager_users.txt', 'a') as arquivo:
            #para cada chave e valor será verificado se há login duplicado
            for chave, valor in dicionario.items():
                    if chave in usuarios_existentes:
                        print('\n====== ATENÇÃO! ======\n' +
                                'Usuário já cadastrado!')
                        break
                    else:
                        arquivo.write(chave + ':' + str(valor) + '\n')
                        print('\n====== CADASTRO REALIZADO! ======\n' +
                              f'O usuário {chave} foi cadastrado com sucesso!') 
                        break  

    
#função 04:  pesquisando usuários dentro dos registros do arquivo gerado
def pesquisar():
    import ast #avaliar expressões literais de Python contidas em strings de forma segura

    #abrindo arquivo no modo read:
    with open('manager_users.txt',  'r') as leitura:
        nome_pesq = input('Digite o nome do usuário que deseja pesquisar: ').upper()
        
        #lista com cada linha do arquivo:
        conteudo = leitura.readlines()

        #loop para verificar cada linha do arquivo:
        encontrado = False
        for valor in conteudo:

            #condição caso encontre o valor:
            if nome_pesq in valor:
                encontrado = True

                print('\n====== USUÁRIO ENCONTRADO! ======\n')

                #imprimindo o resultado:
                print(f'LOGIN: {valor.split(":")[0]}\n') #usando split() para delimitar a str e extrair apenas o login
                print('OUTRAS INFORMAÇÕES: (nome, data último acesso e última estação acessada)')
                dados = ast.literal_eval(valor.split(':')[1]) #ast.literal_eval() retorna a str de lista como uma lista de str

                for item in dados: #loop para percorrer a lista 'dados'
                     print(item, end='\n')
                break
        
        #condição caso NÃO encontre o valor: (está fora do loop principal para não emitir o alerta toda vez que não encontrar o usuário entre os registros)
        if encontrado == False:
            print('\n====== USUÁRIO NÃO ENCONTRADO! ======\n')


#função 05: excluindo um registro do arquivo
def excluir ():
    nome_exc = input('Digite o LOGIN do usuário a ser deletado dos registros: ').upper()
    with open('manager_users.txt', 'r') as arquivo:
         linhas = arquivo.readlines() #extraindo cada linha do arquivo no modo read

    with open('manager_users.txt', 'w') as arquivo:#abrindo arquivo no modo append
         encontrado = False #variável para verificar se o usuário for encontrado ou não
         for linha in linhas: #para cada item da lista:
            if nome_exc not in linha: #se o login indicado pelo usuário NÃO ESTIVER entre as informações:
                   arquivo.write(linha) #então a informação é adicionada no arquivo
            else:
                    encontrado = True #caso o login estiver entre as informações, ele não é adicionado no arquivo e muda a variável 'encontrado' para True

    #verificando o status da variável        
    if encontrado == True:
        print('\n====== OPERAÇÃO CONCLUÍDA COM SUCESSO ======\n' + 
             f'\nO usuário {nome_exc} foi excluído dos registros!')
    else:
        print('\n====== ATENÇÃO! ======\n' +
             f'O {nome_exc} não foi encontrado!')
        

#função 06: listando cada registro do arquivo
def listar ():
    import ast #importando a biblioteca ast para retornar a string de list para uma list de string
    with open ('manager_users.txt', 'r') as arquivo: 
         
        #lista com cada linha do arquivo no modo read:
        conteudo = arquivo.readlines()

        user = 1 #variável de contagem de users
        for valor in conteudo:
            print('\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            print(f'\nUsuário: {user}')
            user += 1 
            print(f'LOGIN: {valor.split(":")[0]}\n') #usando split() para delimitar a str e extrair apenas o login
            print('OUTRAS INFORMAÇÕES: (nome, data último acesso e última estação acessada)')
            dados = ast.literal_eval(valor.split(':')[1]) #ast.literal_eval() retorna a str de lista como uma lista de str

            for item in dados: #loop para percorrer a lista 'dados'
                    print(item, end='\n')

         
#função 07: excluindo arquivo com os registros dos usuários
def excluir_arq ():
    import os #importando a biblioteca OS para interagir com o arquivo 
    
    #confirmando a ação pelo usuário:
    conf_acao = input('\n====== ATENÇÃO! ======\n' +
                       'Deseja excluir o arquivo que contém todo os registros de usuários: (SIM/NÃO)').upper().strip()
    
    #em caso afirmativo:
    if conf_acao in ['S', 'SIM', 'SIM!', 'Y', 'YES', 'YES!']: 
          os.remove('manager_users.txt')
          print('\n====== OPERAÇÃO CONCLUÍDA COM SUCESSO ======\n' + 
             'O arquivo foi excluído!')
    #em caso negativo:
    elif conf_acao in ['N', 'NÃO', 'NÃO!', 'NOT', 'NOT!']:
         print('\n====== OPERAÇÃO CANCELADA COM SUCESSO ======\n' + 
             'O arquivo não foi excluído!')
    #em caso de erro: volta ao menu principal
    else:
         print('\n====== ATENÇÃO ======\n' + 
             'Não foi digitado uma opção válida, retorne ao menu principal!')
         

