from datetime import datetime
import csv

def dataHora():
    dataHora = datetime.now()
    return dataHora.strftime("%d/%m/%Y %H:%M")

def verificarIdade():
    while True:
        idade = input("Idade: ")
        if idade == "00":
            print("-"*100)
            print("Você saiu do programa!")
            print("-"*100)
            exit()
        try:
            if int(idade) > 0 and int(idade) < 100:
                pass
            else:
                print("Por favor insira uma idade válida.")
                continue
        except ValueError:
            print("Por favor insira um número.")
            continue
        return idade
    
def verificarResposta(resposta):
    while True:
        resposta = resposta.lower()
        if resposta == "sim" or resposta == "não" or resposta == "não sei responder":
            return resposta
        else:
            resposta = input("Resposta inválida. Por favor, insira apenas 'sim', 'não' ou 'não sei responder': ")

class Entrevista():
    def __init__(self, idade, genero, resposta1, resposta2, resposta3, resposta4, dataHora):
        self._idade = idade
        self._genero = genero
        self._resposta1 = resposta1
        self._resposta2 = resposta2
        self._resposta3 = resposta3
        self._resposta4 = resposta4
        self._dataHora = dataHora()

    def get_mostrarDadosEntrevista(self):
        dadosEntrevista = {
            "Idade": self._idade,
            "Genero": self._genero,
            "Resposta 1": self._resposta1,
            "Resposta 2": self._resposta2,
            "Resposta 3": self._resposta3,
            "Resposta 4": self._resposta4,
            "Data/Hora": self._dataHora
        }
        return dadosEntrevista

    def gravarCsv(self, dados):
        with open("bd.csv", "a", newline="") as bd:
            writer = csv.writer(bd)
            writer.writerow(dados.values())

# INICIO ARQUIVO MAIN
print("Bem-vindo ao programa de cadastro de pesquisa")

while True:
    menu = input(
        "[1] Cadastrar entrevistados\n"
        "[2] Sair\n"
        "Insira a opção desejada: "
    )

    if menu == "1":
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
