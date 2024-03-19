# Mensagem de boas-vindas
print("Bem-vindo ao sistema de gerenciamento de livros da livraria.")
# Inicialização das variáveis
lista_livro = []
id_global = 0
# Função para cadastrar livro
def cadastrar_livro(id):
    global id_global
    id_global += 1
    nome = input("Nome do livro: ")
    autor = input("Autor do livro: ")
    editora = input("Editora do livro: ")
    livro = {'id': id, 'nome': nome, 'autor': autor, 'editora': editora}
    lista_livro.append(livro)
# Função para consultar livro
def consultar_livro():
    opcao = input("1. Consultar Todos\n2. Consultar por Id\n3. Consultar por Autor\n4. Retornar ao menu\n>> ")
    if opcao == '1':
        print("\nTodos os livros cadastrados:")
        for livro in lista_livro:
            print(livro)
    elif opcao == '2':
        id_consulta = int(input("Digite o ID do livro: "))
        for livro in lista_livro:
            if livro['id'] == id_consulta:
                print("\nLivro encontrado:")
                print(livro)
                break
        else:
            print("Livro não encontrado.")
    elif opcao == '3':
        autor_consulta = input("Digite o nome do autor: ")
        print("\nLivros do autor", autor_consulta)
        for livro in lista_livro:
            if livro['autor'] == autor_consulta:
                print(livro)
    elif opcao == '4':
        return
    else:
        print("Opção inválida.")
# Função para remover livro
def remover_livro():
    id_remover = int(input("Digite o ID do livro a ser removido: "))
    for livro in lista_livro:
        if livro['id'] == id_remover:
            lista_livro.remove(livro)
            print("Livro removido com sucesso.")
            return
    print("Livro não encontrado.")
# Menu principal
while True:
    print("\nMenu:")
    print("1. Cadastrar Livro")
    print("2. Consultar Livro")
    print("3. Remover Livro")
    print("4. Encerrar Programa")
    opcao_menu = input(">> ")
    if opcao_menu == '1':
        cadastrar_livro(id_global)
    elif opcao_menu == '2':
        consultar_livro()
    elif opcao_menu == '3':
        remover_livro()
    elif opcao_menu == '4':
        print("Encerrando o programa. Obrigado!")
        break
    else:
        print("Opção inválida. Tente novamente.")
