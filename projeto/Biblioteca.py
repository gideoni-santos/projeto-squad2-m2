from datetime import datetime
import csv
import os

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

def verificacaoColunas(): 
    #CASO SEJA A PRIMEIRA VEZ EXECUTANDO O PROGRAMA ELE GRAVA AS COLUNAS. CASO CONTRARIO, SEGUE COM O CODIGO.
    coluna = ["Idade", "Genero", "Pergunta1", "Pergunta2", "Pergunta3", "Pergunta4", "Data/Hora"]
    if os.path.exists("bd.csv") and os.path.getsize("bd.csv") > 0:
        print("")
    else:
        with open("bd.csv", "a", newline="") as bd:
            writer = csv.writer(bd)
            writer.writerow(coluna)

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
