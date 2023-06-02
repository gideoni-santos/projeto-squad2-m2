from datetime import datetime
import csv

def dataHora():
    dataHora = datetime.now()
    return dataHora.strftime("%d/%m/%Y %H:%M")

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

#INICIO ARQUIVO MAIN
print("Bem-vindo ao programa de cadastro de pesquisa")

while True:
    menu = input(
        "[1] Cadastrar entrevistados\n"
        "[2] Sair\n"
        "Insira a opção desejada: "
    )

    if menu == "1":
        while True:
            idade = int(input("Idade: "))
            genero = input("Gênero: ")
            resposta1 = input("Pergunta 1: ")
            resposta2 = input("Pergunta 2: ")
            resposta3 = input("Pergunta 3: ")
            resposta4 = input("Pergunta 4: ")
            
            dados = Entrevista(idade, genero, resposta1, resposta2, resposta3, resposta4, dataHora)
            dados.gravarCsv(dados.get_mostrarDadosEntrevista())
            print("Dados da pesquisa inseridos com sucesso!")

    elif menu == "2":
        exit()

    else:
        print("Por favor insira uma opção válida")
        continue