import pygame ,os ,sys , funpygame
import pickle
import random
from datetime import*
from pygame.locals import*
pygame.init()
#musica nova
##pygame.mixer.music.load("bleachmusic.mp3") # Função que faz o load da música
##pygame.mixer.music.set_volume(.5) #Função que define o volume que a música vai ser executada
##pygame.mixer.music.play(-1) #Função que define o tempo que ficará sendo executada a música (-1) - fica infinita

arq = open("cartas.txt","r")
obtercartas1 = arq.read()
obtercartas1 = obtercartas1.split()
arq.close()
numdecartas = int(len(obtercartas1)/8)
cartasdividi = [[]]
for i in range(0,numdecartas):
    carta = i * 8
    cartasdividi[i] = [ obtercartas1[carta] , (int)(obtercartas1[carta + 1]) , (int)(obtercartas1[carta + 2]) , (int)(obtercartas1[carta + 3]) , (int)(obtercartas1[carta + 4]) , (int)(obtercartas1[carta + 5]) , obtercartas1[carta + 6] , obtercartas1[carta + 7] ] 
    cartasdividi.append(cartasdividi[i])
cartasdividi.pop(numdecartas)
    #Super trunfo
superTrunfo = cartasdividi[0][0]
print(superTrunfo)

random.shuffle(cartasdividi)
totaldecartas = int(len(cartasdividi))
n = metadecartas = int(totaldecartas / 2)
jogador1 = cartasdividi[0:metadecartas]
jogador2 = cartasdividi[metadecartas:totaldecartas]



partida = random.randint(0,1)
#----------------------------#
#pygame
tamanho = (900,700)
tela = pygame.display.set_mode(tamanho)
nome1 = ''
nome2 = ''
salvar = ''
nomedoarquivo = ''
background = pygame.image.load("imagens/fundoNome.png")
menufonte = pygame.font.SysFont('Arial.ttf',30)
nomeJogador1 = menufonte.render("Jogador1:" + nome1,True,(255,255,255))
desejaSalvar = menufonte.render("Deseja salvar ?:"+" "+salvar,True,(255,255,255))
nomArquivo = menufonte.render("Codigo do replay: " + nomedoarquivo.upper(),True,(255,255,255))

continuar = True
digitarNome1 = True
digitarNome2 = False
while continuar and digitarNome1:
    tela.blit(background,(0,0))
    tela.blit(nomeJogador1,(50,105))
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
    
            
            teclado = pygame.key.get_pressed()
            nome1 = nome1 + event.unicode
            nomeJogador1 = menufonte.render("Jogador1:" + nome1,True,(255,255,255))
            pygame.display.flip()
            if teclado[K_BACKSPACE]:
                numeroNome1 = len(nome1)
                nomeNovo = nome1[0:numeroNome1 - 2]
                nome1= nomeNovo
                nomeJogador1 = menufonte.render("Jogador1:" + nome1,True,(255,255,255))
                pygame.display.flip()
                
            elif teclado[K_RETURN]:
                numeroNome1 = len(nome1)
                nomeNovo = nome1[0:numeroNome1 - 1]
                nome1= nomeNovo
                digitarNome1= False
    pygame.display.flip()

digitarNome2 = True
while continuar and digitarNome2:
    tela.blit(background,(0,0))
    tela.blit(desejaSalvar,(50,105))
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            
            teclado = pygame.key.get_pressed()
            salvar = salvar + event.unicode
            desejaSalvar = menufonte.render("Deseja salvar ?:"+" "+salvar,True,(255,255,255))
            pygame.display.flip()
            if teclado[K_BACKSPACE]:
                numero = len(salvar)
                nomeNovoSalvar = salvar[0:numero - 2]
                salvar= nomeNovoSalvar
                desejaSalvar = menufonte.render("Deseja salvar ?:"+" "+salvar,True,(255,255,255))
                pygame.display.flip()

            if teclado[K_RETURN]:
                numero = len(salvar)
                nomeNovoSalvar = salvar[0:numero - 1]
                salvar= nomeNovoSalvar
                digitarNome2 = False
                
    pygame.display.flip()
salvar = salvar.upper()
print(salvar)


if salvar == "SIM":
    while True:
        tela.blit(background,(0,0))
        tela.blit(nomArquivo,(50,105))
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                teclado = pygame.key.get_pressed()
                nomedoarquivo = nomedoarquivo + event.unicode
                nomArquivo = menufonte.render("Codigo do replay: " + nomedoarquivo.upper(),True,(255,255,255))    
                pygame.display.flip()
                if teclado[K_BACKSPACE]:
                    numeroArq = len(nomedoarquivo)
                    nomeaqr = nomedoarquivo[0:numeroArq - 2]
                    nomedoarquivo = nomeaqr
                    nomArquivo = menufonte.render("Codigo do replay: " + nomedoarquivo.upper(),True,(255,255,255))
                    pygame.display.flip()
                if teclado[K_RETURN]:
                    numeroArq = len(nomedoarquivo)
                    nomeaqr  = nomedoarquivo[0:numeroArq - 1]
                    nomedoarquivo = nomeaqr
                    nomedoarquivo = nomedoarquivo.upper()
                    arq = open("arquivosreplay/"+ nomedoarquivo + ".txt","ab")
                    pickle.dump(cartasdividi,arq)
                    arq.close()
                    hora = datetime.now()
                    arqreplay = open("arquivosreplay/nomesreplay.txt","a")
                    arqreplay.write("%s%s%s%s" %(nomedoarquivo," ",hora," "))
                    arqreplay.close()
                    arq = open("arquivosreplay/"+nomedoarquivo+"1.txt","a")
                    arq.write(str(partida))
                    arq.write(" ")
                    arq.close()

                    import funpygamesingle
                    funpygamesingle.jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)
        pygame.display.flip()
    

else:
    del nomedoarquivo
    import funpygamesingle
    funpygamesingle.jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,"")
    



