from Biblioteca import *
print("Bem-vindo ao programa de cadastro de pesquisa")

while True:
    menu = input(
        "[1] Cadastrar entrevistados\n"
        "[2] Sair\n"
        "Insira a opção desejada: "
    )

    if menu == "1":
        verificacaoColunas()

        while True:
            idade = verificarIdade()
            genero = input("Gênero: ").capitalize()
            resposta1 = verificarResposta(input("Você acredita que a pandemia mudou a forma como as pessoas buscam propósito de vida? "))
            resposta2 = verificarResposta(input("Você sentiu a necessidade de reavaliar seu propósito profissional durante a pandemia? "))
            resposta3 = verificarResposta(input("Você sentiu a necessidade de buscar ensino EAD durante pandemia? "))
            resposta4 = verificarResposta(input("Você considera ou considerou buscar o ensino EAD para um curso livre ou um curso técnico pós-pandemia? "))

            dados = Entrevista(idade, genero, resposta1, resposta2, resposta3, resposta4, dataHora)
            dados.gravarCsv(dados.get_mostrarDadosEntrevista())
            print("-"*100)
            print("Dados da pesquisa inseridos com sucesso!")
            print("-"*100)

    elif menu == "2":
        print("-"*100)
        print("Você saiu do programa!")
        print("-"*100)
        exit()

    else:
        print("-"*100)
        print("Por favor, insira uma opção válida")
        print("-"*100)
        continue
