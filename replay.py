import pygame , sys
from pygame.locals import*
import pickle
import riplei
pygame.init()



def replayRodada(nomedoarquivo):
    #Pegar a sequencia digitada pelo usuario
    arq = open("arquivosreplay/"+nomedoarquivo+"1.txt","r")
    obtercartas1 = arq.read()
    obtercartas1 = obtercartas1.split()
    arq.close()
    numdenumeros = int(len(obtercartas1))
    sequencia = []
    for i in range(0,numdenumeros):
        cartasdividi1 = int (obtercartas1[i]) 
        sequencia.append(cartasdividi1)

    #---------------------#
    arquivo = open("arquivosreplay/"+nomedoarquivo+".txt","rb")
    listadascartas= pickle.load(arquivo)
    totaldecartas = int(len(listadascartas))
    metadecartas = int(totaldecartas / 2)
    jogador1 = listadascartas[0:metadecartas]
    jogador2 = listadascartas[metadecartas:totaldecartas]
    partida = sequencia[0]
    sequencia.pop(0)
    superTrunfo = "SUPER_TRUNFO"
    riplei.replay(jogador1,jogador2,partida,sequencia,superTrunfo)




        


