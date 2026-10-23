import json

livros =[]

def cadastrar_livro():
    livro = {

    "titulo": input("Digite o título do livro: "),

    "autor": input("Digite o nome do autor do livro: "),

    "ano": int(input("Digite o ano de publicação do livro: ")),
    "disponivel": True
    }

    livros.append(livro)
    salvar_livros()
    
    print("livro cadastrado com sucesso!")

def salvar_livros():
    with open("livros.json", "w", encoding="utf-8") as arquivo:
        json.dump(livros, arquivo, indent=4, ensure_ascii=False)


def carregar_livros():
    global livros

    try:
        with open("livros.json", "r", encoding="utf-8") as arquivo:
            livros = json.load(arquivo)

    except FileNotFoundError:
        livros = []


def listar_livros():
   if not livros:
        print("Não existem livros cadastrados.")

   else:
        for livro in livros:
            print("---------------------")
            print("Título:", livro["titulo"])
            print("Autor:", livro["autor"])
            print("Ano:", livro["ano"])
            if livro["disponivel"]:
                print("Disponibilidade: Sim")
            else:
                print("Disponibilidade: Não")

def buscar_livro():
    busca = input("Buscar livros por título ou autor: ")
    busca_maiusc_minusc = busca.strip().lower()

    if not busca_maiusc_minusc:
        print("Digite um título ou autor para pesquisar.")
        return

    encontrado = False

    for livro in livros:
        titulo_maiusc_minusc = livro["titulo"].strip().lower()
        autor_maiusc_minusc = livro["autor"].strip().lower()

        if busca_maiusc_minusc == titulo_maiusc_minusc or busca_maiusc_minusc == autor_maiusc_minusc:
            print("Título:", livro["titulo"])
            print("Autor:", livro["autor"])
            print("Ano:", livro["ano"])
            if livro["disponivel"]:
                print("Disponibilidade: Sim")
            else:
                print("Disponibilidade: Não")
            encontrado = True
    if not encontrado:
        print("Nenhum livro encontrado")


def realizar_emprestimo():
    titulo = input("Digite o título do livro: ").strip().lower()

    for livro in livros:
        if titulo == livro["titulo"].strip().lower():

            if livro["disponivel"] == False:
                print("Livro indisponível no momento")

            else:
                emprestimo = input("Deseja realizar o empréstimo? sim/não: ").strip().lower()

                if emprestimo == "sim":
                    livro["disponivel"] = False
                    salvar_livros()
                    print("Empréstimo realizado com sucesso!")
                else:
                    print("Empréstimo cancelado.")
            break

    else:
        print("Livro não encontrado.")


def registrar_devolucao():
    titulo_devolver = input("Digite o título do livro: ").strip().lower()

    for livro in livros:
        if titulo_devolver == livro["titulo"].strip().lower():
               
            if livro["disponivel"] == True:
                print("Esse livro não está emprestado.")

            else:
                devolver = input("Deseja realizar devolução? sim/não: ").strip().lower()

                if devolver == "sim":
                    livro["disponivel"] = True
                    salvar_livros()
                    print("Devolução registrada!")
                else:
                    print("Devolução cancelada.")

            break
    else:
        print("Livro fora do catálogo")
               

def exibir_menu():
        print("===== SISTEMA DE BIBLIOTECA =====")
        print()
        print("1 - Cadastrar livro")
        print("2 - Listar livros")
        print("3 - Buscar livro")
        print("4 - Realizar Emprestimo ")
        print("5 - Registar Devolução")
        print("0 - Sair")


carregar_livros()

opcao = -1
while opcao != 0:

    exibir_menu()
    
    opcao = int(input("\ndigite o número da opção desejada: "))

    if opcao == 1:
        cadastrar_livro()
    elif opcao == 2:
        listar_livros()
    elif opcao == 3:
        buscar_livro()
    elif opcao == 4:
        realizar_emprestimo()
    elif opcao == 5:
        registrar_devolucao()
    elif opcao == 0:
        print("Encerrando o sistema...")
    else:
        print("Opção inválida")
        


   








