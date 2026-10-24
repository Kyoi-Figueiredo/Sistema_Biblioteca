#importar o módulo JSON do Python. 
# Vai fazer com que os livros cadastrados continuem salvos mesmo depois de fechar o programa.
import json

# Armazena os livros cadastrados durante a execução
livros =[]

# Cadastra um livro e salva os dados no arquivo JSON
def cadastrar_livro():

    titulo = input("Digite o título do livro: ")
    autor = input("Digite o nome do autor do livro: ")

    try:
        ano = int(input("Digite o ano de publicação do livro: "))
    except ValueError:
        print("Ano inválido. Digite um número inteiro.")
        return

    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "disponivel": True
    }

    livros.append(livro)
    salvar_livros()

    print("Livro cadastrado com sucesso!")


# Salva a lista de livros no arquivo JSON
def salvar_livros():
    with open("livros.json", "w", encoding="utf-8") as arquivo:
        json.dump(livros, arquivo, indent=4, ensure_ascii=False)


# Carrega os livros salvos anteriormente
def carregar_livros():
    global livros

    try:
        with open("livros.json", "r", encoding="utf-8") as arquivo:
            livros = json.load(arquivo)

# O primeiro e segundo "except": trata possíveis erros durante o carregamento: se o arquivo não existir,
# inicia uma lista vazia; se o conteúdo não for um JSON válido,
# informa o problema e também inicia uma lista vazia.
    except FileNotFoundError:
        livros = []

    except json.JSONDecodeError:
        print("Arquivo JSON inválido. Iniciando catálogo vazio.")
        livros = []


# Exibe os detalhes de um livro e salva esses dados na função evitando de repetir todos eles em outras.
# Basta chamar a função
def exibir_detalhes_livro(livro):
    print("---------------------")
    print("Título:", livro["titulo"])
    print("Autor:", livro["autor"])
    print("Ano:", livro["ano"])

    if livro["disponivel"]:
        print("Disponibilidade: Sim")
    else:
        print("Disponibilidade: Não")


# Lista todos os livros cadastrados
def listar_livros():
   if not livros:
        print("Não existem livros cadastrados.")

   else:
       for livro in livros:
           exibir_detalhes_livro(livro)
        
# Busca livros pelo título ou nome do autor
# A palavra "normalizada" pra indicar que o texto está com caracteres padronizados
def buscar_livro():
    busca = input("Buscar livros por título ou autor: ")
    busca_normalizada = busca.strip().lower()

    if not busca_normalizada:
        print("Digite um título ou autor para pesquisar.")
        return

    encontrado = False

    for livro in livros:
        titulo_normalizado = livro["titulo"].strip().lower()
        autor_normalizado = livro["autor"].strip().lower()

        if busca_normalizada == titulo_normalizado or busca_normalizada == autor_normalizado:
            exibir_detalhes_livro(livro)
            encontrado = True

    if not encontrado:
        print("Nenhum livro encontrado")

# Solicita confirmação de uma ação ao usuário
def confirmar_acao(mensagem):
    while True:
        resposta = input(mensagem).strip().lower()

        if resposta == "sim" or resposta == "não" or resposta == "nao":
            return resposta

        print("Resposta inválida. Digite sim ou não.")


# Realiza o empréstimo de um livro disponível
def realizar_emprestimo():
    titulo = input("Digite o título do livro: ").strip().lower()

    for livro in livros:
        if titulo == livro["titulo"].strip().lower():

            if not livro["disponivel"]:
                print("Livro indisponível no momento")

            else:
                emprestimo = confirmar_acao("Deseja realizar o empréstimo? sim/não: ")

                if emprestimo == "sim":
                    livro["disponivel"] = False
                    salvar_livros()
                    print("Empréstimo realizado com sucesso!")
                else:
                    print("Empréstimo cancelado.")
            break

    else:
        print("Livro não encontrado.")


# Registra a devolução de um livro emprestado
def registrar_devolucao():
    titulo_devolver = input("Digite o título do livro: ").strip().lower()

    for livro in livros:
        if titulo_devolver == livro["titulo"].strip().lower():
               
            if livro["disponivel"]:
                print("Esse livro não está emprestado.")

            else:
                devolver = confirmar_acao("Deseja realizar devolução? sim/não: ")

                if devolver == "sim":
                    livro["disponivel"] = True
                    salvar_livros()
                    print("Devolução registrada!")
                else:
                    print("Devolução cancelada.")

            break
    else:
        print("Livro fora do catálogo")

# Exibe o total de livros, disponíveis e emprestados
def contar_acervo():
    total = len(livros)
    disponiveis = 0
    emprestados = 0

    for livro in livros:

        if livro["disponivel"]:
            disponiveis += 1
        else:
            emprestados += 1

    print("===== CONTADOR DO ACERVO =====")
    print("Total de livros:", total)
    print("Livros disponíveis:", disponiveis)
    print("Livros emprestados:", emprestados)


# Ordena os livros por título ou ano de publicação
def ordenar_livros():

    if not livros:
        print("Não existem livros cadastrados.")
        return

    print("===== ORDENAR LIVROS =====")
    print("1 - Ordem alfabética por título")
    print("2 - Ordem cronológica por ano")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        livros_ordenados = sorted(livros, key=lambda livro: livro["titulo"].lower())
    elif opcao == "2":
        livros_ordenados = sorted(livros, key=lambda livro: livro["ano"])
    else:
        print("Opção inválida.")
        return

    for livro in livros_ordenados:
        print("---------------------")
        print("Título:", livro["titulo"])
        print("Autor:", livro["autor"])
        print("Ano:", livro["ano"])


# Remove um livro do catálogo
def remover_livros():
    remover = input("Digite o nome do livro que deseja remover: ").strip().lower()

    for livro in livros:
        if livro["titulo"].strip().lower() == remover:
            resposta = confirmar_acao("Deseja realmente remover este livro? sim/não: ")
            if resposta == "sim":
                livros.remove(livro)
                salvar_livros()
                print("Livro removido com sucesso!")
            break

    else:
        print("Livro não encontrado.")
          

# Exibe as opções disponíveis no sistema
def exibir_menu():
        print("===== SISTEMA DE BIBLIOTECA =====")
        print()
        print("1 - Cadastrar livro")
        print("2 - Listar livros")
        print("3 - Buscar livro")
        print("4 - Realizar Emprestimo ")
        print("5 - Registar Devolução")
        print("6 - Consultar contador do acervo")
        print("7 - Ordenar livros")
        print("8 - Remover livros")
        print("0 - Sair")


carregar_livros()

opcao = -1
while opcao != 0:

    exibir_menu()
    
    try:
        opcao = int(input("\ndigite o número da opção desejada: "))
    except ValueError:
        print("Você precisa digitar um número inteiro.")
        continue

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
    elif opcao == 6:
        contar_acervo()
    elif opcao == 7:
        ordenar_livros()
    elif opcao == 8:
        remover_livros()
    elif opcao == 0:
        print("Encerrando o sistema...")
    else:
        print("Opção inválida")
        


   








