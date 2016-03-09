import pygame , random ,sys , os
from pygame.locals import*
pygame.init()

montanteEmpate = []
espaco = 10
espaco1 = 485

mostrarEmpate = 700
def mostrarMontante(imagemContador,tela,montanteEmpate,contadorEmpate):
    mostrarEmpate = 800
    if (len(montanteEmpate) > 0):
        for i in range(1,(len(montanteEmpate)+1)):
            mostrarEmpate = mostrarEmpate + 8
            tela.blit(imagemContador,(mostrarEmpate,10))
    pygame.draw.rect(tela,(0,0,0),(800,70,30,30))
    tela.blit(contadorEmpate,(805,70))
    return

def mostrarContador(jogador1,tela,imagemContador):
    espaco = 10
    for i in range (1,len(jogador1)+1):
        espaco = espaco + 8
        tela.blit(imagemContador,(espaco,10))
        
    return
def mostrarContador2(jogador2,tela,imagemContador2):
    espaco1 = 485
    for i in range (1,len(jogador2)+1):
        espaco1 = espaco1 + 8
        tela.blit(imagemContador2,(espaco1,10))
    return

def vitoria1(jogador1,jogador2):
    jogador1.append(jogador2[0])
    jogador1.append(jogador1[0])
    jogador1.pop(0)
    jogador2.pop(0)     
    print(" Jogador 1 ganhou")

def empate(jogador1,jogador2):
    montanteEmpate.append(jogador1[0])
    montanteEmpate.append(jogador2[0])
    print(montanteEmpate)
    jogador1.pop(0)
    jogador2.pop(0)
    print("Empatou")
    

def derrotaJogador1(jogador1,jogador2):
    jogador2.append(jogador1[0])
    jogador2.append(jogador2[0])
    jogador2.pop(0)
    jogador1.pop(0)                   
    print("Jogador 1 perdeu")

def vitoria2(jogador1,jogador2):
    jogador2.append(jogador1[0])
    jogador2.append(jogador2[0])
    jogador1.pop(0)
    jogador2.pop(0)
    print(" Jogador 2 ganhou")

def derrotaJogador2(jogador1,jogador2):
    jogador1.append(jogador2[0])
    jogador1.append(jogador1[0])
    jogador2.pop(0)
    jogador1.pop(0)                   
    print("Jogador 2 perdeu")

def chamarsuperTrunfo(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo,montanteEmpate):
    #super Trunfo

    if (jogador1[0][6] != "A1" and jogador1[0][6] != "B1" and jogador1[0][6] != "C1"   and jogador1[0][6] != "D1") and   jogador2[0][0] == superTrunfo:
        print("Super Trunfo")
        derrotaJogador1(jogador1,jogador2)
        partida = 1
        if (len(montanteEmpate) > 0):
            for i in range(0,len(montanteEmpate)):
                jogador2.append(montanteEmpate[0])
                montanteEmpate.pop(0)
        jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)

    elif (jogador1[0][6] == "A1" or jogador1[0][6] == "B1" or jogador1[0][6] == "C1" or jogador1[0][6] == "D1" ) and jogador2[0][0] == superTrunfo:
        print("Tipo A1")
        vitoria1(jogador1,jogador2)
        partida = 0
        if (len(montanteEmpate) > 0):
            for i in range(0,len(montanteEmpate)):
                jogador1.append(montanteEmpate[0])
                montanteEmpate.pop(0)
        jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)
    return #Se não for retorna para o jogar
    #------------------------------------------------#    
       
def chamarsuperTrunfo1(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo,montanteEmpate):
    if (jogador2[0][6] != "A1" and jogador2[0][6] != "B1" and jogador2[0][6] != "C1"   and jogador2[0][6] != "D1") and   jogador1[0][0] == superTrunfo:
        print("supertrunfo")
        derrotaJogador2(jogador1,jogador2)
        partida = 0
        if (len(montanteEmpate) > 0):
            for i in range(0,len(montanteEmpate)):
                jogador1.append(montanteEmpate[0])
                montanteEmpate.pop(0)
        jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)
    elif (jogador2[0][6] == "A1" or jogador2[0][6] == "B1" or jogador2[0][6] == "C1" or jogador2[0][6] == "D1" ) and jogador1[0][0] == superTrunfo:
        print("Tipo A1")
        vitoria2(jogador1,jogador2)
        partida = 1
        if (len(montanteEmpate) > 0):
            for i in range(0,len(montanteEmpate)):
                jogador2.append(montanteEmpate[0])
                montanteEmpate.pop(0)
        jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)
             
    return #Se não tiver retorna para o jogar
def mostrarCarta1(tela,fotoCarta,nomePersonagem,nomeAtributo1,nomeAtributo2,nomeAtributo3,nomeAtributo4,nomeAtributo5,nomeAtributo6,personagem1):
    tela.blit(fotoCarta,(0,120))      
    tela.blit(nomePersonagem,(5,155))
    tela.blit(nomeAtributo1,(150,237))
    tela.blit(nomeAtributo2,(150,282))
    tela.blit(nomeAtributo3,(150,327))
    tela.blit(nomeAtributo4,(150,374))
    tela.blit(nomeAtributo5,(150,420))
    tela.blit(nomeAtributo6,(150,465))             
    tela.blit(personagem1,(153,130))

def mostrarCarta2(tela,fotoCarta,nomePersonagem2,nomeAtributo7,nomeAtributo8,nomeAtributo9,nomeAtributo10,nomeAtributo11,nomeAtributo12,personagem2):
    tela.blit(fotoCarta,(480,120))
    tela.blit(nomePersonagem2,(485,155))
    tela.blit(nomeAtributo7,(630,237))
    tela.blit(nomeAtributo8,(630,282))
    tela.blit(nomeAtributo9,(630,327))
    tela.blit(nomeAtributo10,(630,374))
    tela.blit(nomeAtributo11,(630,420))
    tela.blit(nomeAtributo12,(630,465))
    tela.blit(personagem2,(630,130))
 
                


def jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo):
    
    #-------Pygame---------#
    tamanho = (900,700)
    tela = pygame.display.set_mode(tamanho)
    pygame.display.set_caption("Super Trunfo")
    
    #imagens
    background = pygame.image.load("imagens/fundo.png").convert()
    vitoria = pygame.image.load("imagens/fundovitoria.png").convert()
    continuar = True    
    if len(jogador1)== 0 or len(jogador2)== 0:        
        if len(jogador1) > 0:
            while continuar:
                textofont = pygame.font.Font('dc_o.1.ttf',35)
                fonteVenceu = pygame.font.SysFont('Arial.ttf',50)
                textoReplay = textofont.render('Replay',True,(255,255,255))
                textoReplayRec = textoReplay.get_rect().move(700,650)
                textoVoltar = textofont.render('Sair',True,(255,255,255))
                textoVoltarRec = textoVoltar.get_rect().move(50,650)
                textoVenceu = fonteVenceu.render('Jogador 1 venceu',True,(255,255,255)) 
                tela.blit(vitoria,(0,0))
                tela.blit(textoReplay,(700,650))
                tela.blit(textoVoltar,(50,650))
                tela.blit(textoVenceu,(350,230))
                if textoReplayRec.collidepoint(pygame.mouse.get_pos()):
                    textoReplay = textofont.render('Replay',True,(255,255,255))
                    tela.blit(textoReplay,(700,650))     
                    if pygame.mouse.get_pressed()[0]:
                        if nomedoarquivo != "":
                            import replay
                            replay.replayRodada(nomedoarquivo)
                        print("Não foi gravado")
                if textoVoltarRec.collidepoint(pygame.mouse.get_pos()):
                    textoVoltar = textofont.render('Sair',True,(255,255,255))
                    tela.blit(textoVoltar,(50,650))
                    if pygame.mouse.get_pressed()[0]:
                        exit()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()
                pygame.display.flip()
                
        elif len(jogador2)>0:
            while continuar:
                fonteVenceu = pygame.font.SysFont('Arial.ttf',50)
                textofont = pygame.font.Font('dc_o.1.ttf',35)
                textoReplay = textofont.render('Replay',True,(255,255,255))
                textoReplayRec = textoReplay.get_rect().move(700,650)
                textoVoltar = textofont.render('Sair',True,(255,255,255))
                textoVoltarRec = textoVoltar.get_rect().move(50,650)
                textoVenceu = fonteVenceu.render('Jogador 2 venceu',True,(255,255,255))
                tela.blit(vitoria,(0,0))
                tela.blit(textoReplay,(700,650))
                tela.blit(textoVoltar,(50,650))
                tela.blit(textoVenceu,(350,230))
                if textoReplayRec.collidepoint(pygame.mouse.get_pos()):
                    textoReplay = textofont.render('Replay',True,(255,255,255))
                    tela.blit(textoReplay,(700,650))     
                    if pygame.mouse.get_pressed()[0]:
                        if nomedoarquivo != "":
                            import replay
                            replay.replayRodada(nomedoarquivo)
                        print("Não foi gravado")
                if textoVoltarRec.collidepoint(pygame.mouse.get_pos()):
                    textoVoltar = textofont.render('Sair',True,(255,255,255))
                    tela.blit(textoVoltar,(50,650))
                    if pygame.mouse.get_pressed()[0]:
                        exit()
                
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()
                print("Jogador 2 ganhou")
                pygame.display.flip()
    fotoCarta = pygame.image.load("imagens/carta.png").convert_alpha()
    fotoCarta1 = pygame.image.load("imagens/carta1.png").convert_alpha()
    fotoCarta2 = pygame.image.load("imagens/carta2.png").convert_alpha()
    if os.path.exists("imagens/"+jogador1[0][0]+".png") == True:
        personagem1 = pygame.image.load("imagens/" + jogador1[0][0]+".png").convert_alpha()
    else:
        personagem1 = pygame.image.load("imagens/SEMFOTO.png").convert_alpha()   
    if os.path.exists("imagens/"+jogador2[0][0]+".png") == True:
        personagem2 = pygame.image.load("imagens/" + jogador2[0][0]+".png").convert_alpha()
    else:
        personagem2 = pygame.image.load("imagens/SEMFOTO.png").convert_alpha()
    selecionar   = pygame.image.load("imagens/fogo.png").convert_alpha()
    #vez1 = pygame.image.load("imagens/vez1.png").convert_alpha()
    #vez2 = pygame.image.load("imagens/vez2.png").convert_alpha()
    
    #Click cartas 1#
    imagemclick1 = pygame.image.load("imagens/CARD2.png").convert()
    imagemclick1REC = imagemclick1.get_rect().move(0,240)
    imagemclick2 = pygame.image.load("imagens/CARD2.png").convert()
    imagemclick2REC = imagemclick2.get_rect().move(0,285)
    imagemclick3 = pygame.image.load("imagens/CARD2.png").convert()
    imagemclick3REC = imagemclick3.get_rect().move(0,330)
    imagemclick4 = pygame.image.load("imagens/CARD2.png").convert()
    imagemclick4REC = imagemclick4.get_rect().move(0,375)
    imagemclick5 = pygame.image.load("imagens/CARD2.png").convert()
    imagemclick5REC = imagemclick5.get_rect().move(0,420)
    #---Click cartas 2----#
    imagemclick6 = pygame.image.load("imagens/CARD2.png").convert()
    imagemclick6REC = imagemclick6.get_rect().move(480,240)
    imagemclick7 = pygame.image.load("imagens/CARD2.png").convert()
    imagemclick7REC = imagemclick7.get_rect().move(480,285)
    imagemclick8 = pygame.image.load("imagens/CARD2.png").convert()
    imagemclick8REC = imagemclick8.get_rect().move(480,330)
    imagemclick9 = pygame.image.load("imagens/CARD2.png").convert()
    imagemclick9REC = imagemclick9.get_rect().move(480,375)
    imagemclick10 = pygame.image.load("imagens/CARD2.png").convert()
    imagemclick10REC = imagemclick10.get_rect().move(480,420)
    
    #textos

    
    #Jogador 1
    menufont = pygame.font.Font('dc_o.1.ttf',35)
    topoNome = pygame.font.Font('dc_o.ttf',25)
    fonteContador = pygame.font.SysFont('SHOWG.TTF',40)
    #contador
    contador1 = fonteContador.render(str (len(jogador1)),True,(255,255,255))
    contador2 = fonteContador.render(str(len(jogador2)),True,(255,255,255))
    contadorEmpate = fonteContador.render(str(len(montanteEmpate)),True,(255,255,255))
    imagemContador = pygame.image.load('imagens/contador.png').convert_alpha()
    imagemContador2 = pygame.image.load('imagens/contador.png').convert_alpha()
    nomePersonagem = topoNome.render(jogador1[0][0],True,(255,255,255))
    
    nomeAtributo1 = menufont.render(str (jogador1[0][1]),True,(255,255,255))
    nomeAtributo2 = menufont.render(str (jogador1[0][2]),True,(255,255,255))
    nomeAtributo3 = menufont.render(str (jogador1[0][3]),True,(255,255,255))
    nomeAtributo4 = menufont.render(str (jogador1[0][4]),True,(255,255,255))
    nomeAtributo5 = menufont.render(str (jogador1[0][5]),True,(255,255,255))
    nomeAtributo6 = menufont.render(str (jogador1[0][6]),True,(255,255,255))
    #Textos jogador 2
    nomePersonagem2 = topoNome.render(jogador2[0][0],True,(255,255,255))
    
    nomeAtributo7 = menufont.render(str (jogador2[0][1]),True,(255,255,255))
    nomeAtributo8 = menufont.render(str (jogador2[0][2]),True,(255,255,255))
    nomeAtributo9 = menufont.render(str (jogador2[0][3]),True,(255,255,255))
    nomeAtributo10 = menufont.render(str (jogador2[0][4]),True,(255,255,255))
    nomeAtributo11 = menufont.render(str (jogador2[0][5]),True,(255,255,255))
    nomeAtributo12 = menufont.render(str (jogador2[0][6]),True,(255,255,255))
    
    if partida == 0:
        continuar = True
        while continuar:
            
            #Aparecer na tela
            tela.blit(background,(0,0))
            pygame.draw.rect(tela,(0,0,0),(30,70,40,30))
            pygame.draw.rect(tela,(0,0,0),(503,70,40,30))
            #tela.blit(vez1,(0,700))
            tela.blit(contador1,(30,70))
            tela.blit(contador2,(505,70))
            tela.blit(fotoCarta2,(480,120))
            mostrarCarta1(tela,fotoCarta,nomePersonagem,nomeAtributo1,nomeAtributo2,nomeAtributo3,nomeAtributo4,nomeAtributo5,nomeAtributo6,personagem1)
            mostrarContador(jogador1,tela,imagemContador)
            mostrarContador2(jogador2,tela,imagemContador2)
            mostrarMontante(imagemContador,tela,montanteEmpate,contadorEmpate)
            #testar supertrunfo para jogador 1

            if jogador1[0][0] == superTrunfo and (jogador2[0][6] != "A1" and jogador2[0][6] != "B1" and jogador2[0][6] != "C1" and jogador2[0][6] != "D1"): #se supertrunfo tiver com o jogador  1 mostra a carta 2 
                mostrarCarta2(tela,fotoCarta,nomePersonagem2,nomeAtributo7,nomeAtributo8,nomeAtributo9,nomeAtributo10,nomeAtributo11,nomeAtributo12,personagem2)
                pygame.display.flip()
                pygame.time.wait(3000)
        
                print("superTrunfo")
                vitoria1(jogador1,jogador2)
                partida = 0
                if (len(montanteEmpate) > 0):
                    for i in range(0,len(montanteEmpate)):
                        jogador1.append(montanteEmpate[0])
                        montanteEmpate.pop(0)
                jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)

            elif jogador1[0][0] == superTrunfo and (jogador2[0][6] == "A1" or jogador2[0][6] == "B1" or jogador2[0][6] == "C1" or jogador2[0][6] == "D1"):
                mostrarCarta2(tela,fotoCarta,nomePersonagem2,nomeAtributo7,nomeAtributo8,nomeAtributo9,nomeAtributo10,nomeAtributo11,nomeAtributo12,personagem2)
                pygame.display.flip()
                pygame.time.wait(3000)
        
                print("Tipo A1")
                derrotaJogador1(jogador1,jogador2)
                partida = 1
                if (len(montanteEmpate) > 0):
                    for i in range(0,len(montanteEmpate)):
                        jogador2.append(montanteEmpate[0])
                        montanteEmpate.pop(0)
                jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)
            #Atributo 1
            if imagemclick1REC.collidepoint(pygame.mouse.get_pos()):
                tela.blit(selecionar,(120,235))
                if pygame.mouse.get_pressed()[0]:
                    if nomedoarquivo != "":
                        arq = open("arquivosreplay/"+nomedoarquivo+"1.txt","a")
                        arq.write("1")
                        arq.write(" ")
                        arq.close()
                    mostrarCarta2(tela,fotoCarta,nomePersonagem2,nomeAtributo7,nomeAtributo8,nomeAtributo9,nomeAtributo10,nomeAtributo11,nomeAtributo12,personagem2)
                    tela.blit(selecionar,(600,235))
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    chamarsuperTrunfo(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo,montanteEmpate)

                    if jogador1[0][1] > jogador2[0][1]:
                        vitoria1(jogador1,jogador2)
                        
                        if len(montanteEmpate) > 0:
                            jogador1.append(montanteEmpate)
                            for i in range(0,len(montanteEmpate)):
                                montanteEmpate.pop(0)
                        partida = 0
                        jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)
                        
                    elif jogador1[0][1] == jogador2[0][1]:
                        empate(jogador1,jogador2)
                        partida = 0
                        jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)
                        print("empatou")

                    elif jogador1[0][1] < jogador2[0][1]:
                        derrotaJogador1(jogador1,jogador2)
                        if len(montanteEmpate) > 0:
                            jogador2.append(montanteEmpate)
                            for i in range(0,len(montanteEmpate)):
                                montanteEmpate.pop(0)
                        partida = 1
                        jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)
                    
                
            #Atributo 2
            if imagemclick2REC.collidepoint(pygame.mouse.get_pos()):
                tela.blit(selecionar,(120,280))
                if pygame.mouse.get_pressed()[0]:
                    if nomedoarquivo != "":
                        arq = open("arquivosreplay/"+nomedoarquivo+"1.txt","a")
                        arq.write("2")
                        arq.write(" ")
                        arq.close()
                    mostrarCarta2(tela,fotoCarta,nomePersonagem2,nomeAtributo7,nomeAtributo8,nomeAtributo9,nomeAtributo10,nomeAtributo11,nomeAtributo12,personagem2)
                    tela.blit(selecionar,(600,280))
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    chamarsuperTrunfo(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo,montanteEmpate)
                    
                    if jogador1[0][2] > jogador2[0][2]:
                        vitoria1(jogador1,jogador2)
                        partida = 0
                        if (len(montanteEmpate) > 0):
                            for i in range(0,len(montanteEmpate)):
                                jogador1.append(montanteEmpate[0])
                                montanteEmpate.pop(0)
                        jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)
                        
                    elif jogador1[0][2] == jogador2[0][2]:
                        empate(jogador1,jogador2)
                        partida = 0
                        jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)
                        print("empatou")

                    elif jogador1[0][2] < jogador2[0][2]:
                        derrotaJogador1(jogador1,jogador2)
                        partida = 1
                        if (len(montanteEmpate) > 0):
                            for i in range(0,len(montanteEmpate)):
                                jogador2.append(montanteEmpate[0])
                                montanteEmpate.pop(0)
                        jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)

            #Atributo 3
            if imagemclick3REC.collidepoint(pygame.mouse.get_pos()):
                tela.blit(selecionar,(120,325))
                
                if pygame.mouse.get_pressed()[0]:
                    if nomedoarquivo != "":
                        arq = open("arquivosreplay/"+nomedoarquivo+"1.txt","a")
                        arq.write("3")
                        arq.write(" ")
                        arq.close()
                    mostrarCarta2(tela,fotoCarta,nomePersonagem2,nomeAtributo7,nomeAtributo8,nomeAtributo9,nomeAtributo10,nomeAtributo11,nomeAtributo12,personagem2)
                    tela.blit(selecionar,(600,325))
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    chamarsuperTrunfo(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo,montanteEmpate)
                    
                    if jogador1[0][3] > jogador2[0][3]:
                        vitoria1(jogador1,jogador2)
                        partida = 0
                        if (len(montanteEmpate) > 0):
                            for i in range(0,len(montanteEmpate)):
                                jogador1.append(montanteEmpate[0])
                                montanteEmpate.pop(0)
                        jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)
                        
                    elif jogador1[0][3] == jogador2[0][3]:
                        empate(jogador1,jogador2)
                        partida = 0
                        jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)
                        print("empatou")

                    elif jogador1[0][3] < jogador2[0][3]:
                        derrotaJogador1(jogador1,jogador2)
                        partida = 1
                        if (len(montanteEmpate) > 0):
                            for i in range(0,len(montanteEmpate)):
                                jogador2.append(montanteEmpate[0])
                                montanteEmpate.pop(0)
                        jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)
                
            #Atributo 4
            if imagemclick4REC.collidepoint(pygame.mouse.get_pos()):
                tela.blit(selecionar,(120,373))
                if pygame.mouse.get_pressed()[0]:
                    if nomedoarquivo != "":
                        arq = open("arquivosreplay/"+nomedoarquivo+"1.txt","a")
                        arq.write("4")
                        arq.write(" ")
                        arq.close()
                    mostrarCarta2(tela,fotoCarta,nomePersonagem2,nomeAtributo7,nomeAtributo8,nomeAtributo9,nomeAtributo10,nomeAtributo11,nomeAtributo12,personagem2)
                    tela.blit(selecionar,(600,373))
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    chamarsuperTrunfo(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo,montanteEmpate)
                    
                    if jogador1[0][4] > jogador2[0][4]:
                        vitoria1(jogador1,jogador2)
                        partida = 0
                        if (len(montanteEmpate) > 0):
                            for i in range(0,len(montanteEmpate)):
                                jogador1.append(montanteEmpate[0])
                                montanteEmpate.pop(0)
                        jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)
                        
                    elif jogador1[0][4] == jogador2[0][4]:
                        empate(jogador1,jogador2)
                        partida = 0
                        jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)
                        print("empatou")

                    elif jogador1[0][4] < jogador2[0][4]:
                        derrotaJogador1(jogador1,jogador2)
                        if (len(montanteEmpate) > 0):
                            for i in range(0,len(montanteEmpate)):
                                jogador2.append(montanteEmpate[0])
                                montanteEmpate.pop(0)
                        partida = 1
                        jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)
                
            #Atributo 5
            if imagemclick5REC.collidepoint(pygame.mouse.get_pos()):
                tela.blit(selecionar,(120,420))
                if pygame.mouse.get_pressed()[0]:
                    if nomedoarquivo != "":
                        arq = open("arquivosreplay/"+nomedoarquivo+"1.txt","a")
                        arq.write("5")
                        arq.write(" ")
                        arq.close()
                    mostrarCarta2(tela,fotoCarta,nomePersonagem2,nomeAtributo7,nomeAtributo8,nomeAtributo9,nomeAtributo10,nomeAtributo11,nomeAtributo12,personagem2)
                    tela.blit(selecionar,(600,420))
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    chamarsuperTrunfo(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo,montanteEmpate)
                    
                    if jogador1[0][5] > jogador2[0][5]:
                        vitoria1(jogador1,jogador2)
                        if (len(montanteEmpate) > 0):
                            for i in range(0,len(montanteEmpate)):
                                jogador1.append(montanteEmpate[0])
                                montanteEmpate.pop(0)
                        partida = 0
                        jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)
                        
                    elif jogador1[0][5] == jogador2[0][5]:
                        empate(jogador1,jogador2)
                        partida = 0
                        jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)
                        print("empatou")

                    elif jogador1[0][5] < jogador2[0][5]:
                        derrotaJogador1(jogador1,jogador2)
                        if (len(montanteEmpate) > 0):
                            for i in range(0,len(montanteEmpate)):
                                jogador2.append(montanteEmpate[0])
                                montanteEmpate.pop(0)
                        partida = 1
                        jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)

            for event in pygame.event.get():
                if (event.type==QUIT):
                    continuar = False
            pygame.display.flip()
        pygame.quit()
    else:
        atributoComputador = random.randint(1,5)
        continuar = True
        while continuar:
            #Mostrar na tela
            tela.blit(background,(0,0))
            pygame.draw.rect(tela,(0,0,0),(30,70,40,30))
            pygame.draw.rect(tela,(0,0,0),(503,70,40,30))
            #tela.blit(vez2,(600,600))
            tela.blit(contador1,(30,70))
            tela.blit(contador2,(505,70))
            tela.blit(fotoCarta1,(0,120))
            mostrarCarta2(tela,fotoCarta,nomePersonagem2,nomeAtributo7,nomeAtributo8,nomeAtributo9,nomeAtributo10,nomeAtributo11,nomeAtributo12,personagem2)
            mostrarContador(jogador1,tela,imagemContador)
            mostrarContador2(jogador2,tela,imagemContador)
            mostrarMontante(imagemContador,tela,montanteEmpate,contadorEmpate)
            pygame.display.flip()
            pygame.time.wait(2000)

            if jogador2[0][0] == superTrunfo and (jogador1[0][6] != "A1" and jogador1[0][6] != "B1" and jogador1[0][6] != "C1" and jogador1[0][6] != "D1"):
                mostrarCarta1(tela,fotoCarta,nomePersonagem,nomeAtributo1,nomeAtributo2,nomeAtributo3,nomeAtributo4,nomeAtributo5,nomeAtributo6,personagem1)
                pygame.display.flip()
                pygame.time.wait(3000)
                print("Super trunfo")
                vitoria2(jogador1,jogador2)
                partida = 1
                if (len(montanteEmpate) > 0):
                    for i in range(0,len(montanteEmpate)):
                        jogador2.append(montanteEmpate[0])
                        montanteEmpate.pop(0)
                jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)
            elif jogador2[0][0] == superTrunfo and (jogador1[0][6] == "A1" or jogador1[0][6] == "B1" or jogador1[0][6] == "C1" or jogador1[0][6] == "D1"):
                mostrarCarta(tela,fotoCarta,nomePersonagem,nomeAtributo1,nomeAtributo2,nomeAtributo3,nomeAtributo4,nomeAtributo5,nomeAtributo6,personagem1)
                pygame.display.flip()
                pygame.time.wait(3000)
                    
                print("Tipo A1 venceu")
                derrotajogador2(jogador1,jogador2)
                partida = 0
                if (len(montanteEmpate) > 0):
                    for i in range(0,len(montanteEmpate)):
                        jogador1.append(montanteEmpate[0])
                        montanteEmpate.pop(0)
                jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)

            if atributoComputador == 1:
                if nomedoarquivo != "":
                    arq = open("arquivosreplay/"+nomedoarquivo+"1.txt","a")
                    arq.write("1")
                    arq.write(" ")
                    arq.close()
                tela.blit(selecionar,(600,235))
                mostrarCarta1(tela,fotoCarta,nomePersonagem,nomeAtributo1,nomeAtributo2,nomeAtributo3,nomeAtributo4,nomeAtributo5,nomeAtributo6,personagem1)
                tela.blit(selecionar,(120,235))
                pygame.display.flip()
                pygame.time.wait(3000)
                chamarsuperTrunfo1(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo,montanteEmpate)
                if jogador2[0][1] > jogador1[0][1]:
                    vitoria2(jogador1,jogador2)
                    partida = 1
                    if (len(montanteEmpate) > 0):
                        for i in range(0,len(montanteEmpate)):
                            jogador2.append(montanteEmpate[0])
                            montanteEmpate.pop(0)
                    jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)
                        
                elif jogador2[0][1] == jogador1[0][1]:
                    empate(jogador1,jogador2)
                    partida = 1
                    jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)
                    print("empatou")

                elif jogador2[0][1] < jogador1[0][1]:
                    derrotaJogador2(jogador1,jogador2)
                    partida = 0
                    if (len(montanteEmpate) > 0):
                        for i in range(0,len(montanteEmpate)):
                            jogador1.append(montanteEmpate[0])
                            montanteEmpate.pop(0)
                    jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)

            elif atributoComputador == 2 :
                if nomedoarquivo != "":
                    arq = open("arquivosreplay/"+nomedoarquivo+"1.txt","a")
                    arq.write("2")
                    arq.write(" ")
                    arq.close()
                tela.blit(selecionar,(600,280))
                mostrarCarta1(tela,fotoCarta,nomePersonagem,nomeAtributo1,nomeAtributo2,nomeAtributo3,nomeAtributo4,nomeAtributo5,nomeAtributo6,personagem1)
                tela.blit(selecionar,(120,280))
                pygame.display.flip()
                pygame.time.wait(3000)
                chamarsuperTrunfo1(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo,montanteEmpate)
                if jogador2[0][2] > jogador1[0][2]:
                    vitoria2(jogador1,jogador2)
                    partida = 1
                    if (len(montanteEmpate) > 0):
                        for i in range(0,len(montanteEmpate)):
                            jogador2.append(montanteEmpate[0])
                            montanteEmpate.pop(0)
                    jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)
                        
                elif jogador2[0][2] == jogador1[0][2]:
                    empate(jogador1,jogador2)
                    partida = 1
                    chamarsuperTrunfo1(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo,montanteEmpate)
                    print("empatou")

                elif jogador2[0][2] < jogador1[0][2]:
                    derrotaJogador2(jogador1,jogador2)
                    partida = 0
                    if (len(montanteEmpate) > 0):
                        for i in range(0,len(montanteEmpate)):
                            jogador1.append(montanteEmpate[0])
                            montanteEmpate.pop(0)
                    jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)

            elif atributoComputador == 3:
                if nomedoarquivo != "":
                    arq = open("arquivosreplay/"+nomedoarquivo+"1.txt","a")
                    arq.write("3")
                    arq.write(" ")
                    arq.close()
                tela.blit(selecionar,(600,325))
                mostrarCarta1(tela,fotoCarta,nomePersonagem,nomeAtributo1,nomeAtributo2,nomeAtributo3,nomeAtributo4,nomeAtributo5,nomeAtributo6,personagem1)
                tela.blit(selecionar,(120,325))
                pygame.display.flip()
                pygame.time.wait(3000)
                chamarsuperTrunfo1(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo,montanteEmpate)
                if jogador2[0][3] > jogador1[0][3]:
                    vitoria2(jogador1,jogador2)
                    partida = 1
                    if (len(montanteEmpate) > 0):
                        for i in range(0,len(montanteEmpate)):
                            jogador2.append(montanteEmpate[0])
                            montanteEmpate.pop(0)
                    jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)
                        
                elif jogador2[0][3] == jogador1[0][3]:
                    empate(jogador1,jogador2)
                    partida = 1
                    jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)
                    print("empatou")

                elif jogador2[0][3] < jogador1[0][3]:
                    derrotaJogador2(jogador1,jogador2)
                    partida = 0
                    if (len(montanteEmpate) > 0):
                        for i in range(0,len(montanteEmpate)):
                            jogador1.append(montanteEmpate[0])
                            montanteEmpate.pop(0)
                    jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)
            elif atributoComputador == 4:
                if nomedoarquivo != "":
                    arq = open("arquivosreplay/"+nomedoarquivo+"1.txt","a")
                    arq.write("4")
                    arq.write(" ")
                    arq.close()
                    
                tela.blit(selecionar,(600,373))
                mostrarCarta1(tela,fotoCarta,nomePersonagem,nomeAtributo1,nomeAtributo2,nomeAtributo3,nomeAtributo4,nomeAtributo5,nomeAtributo6,personagem1)
                tela.blit(selecionar,(120,373))
                pygame.display.flip()
                pygame.time.wait(3000)
                chamarsuperTrunfo1(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo,montanteEmpate)
                if jogador2[0][4] > jogador1[0][4]:                       
                    vitoria2(jogador1,jogador2)                        
                    partida = 1
                    if (len(montanteEmpate) > 0):
                        for i in range(0,len(montanteEmpate)):
                            jogador2.append(montanteEmpate[0])
                            montanteEmpate.pop(0)
                    jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)
                        
                elif jogador2[0][4] == jogador1[0][4]:                        
                    empate(jogador1,jogador2)                        
                    partida = 0
                    jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)
                       
                elif jogador2[0][4] < jogador1[0][4]:                        
                    derrotaJogador2(jogador1,jogador2)                        
                    partida = 0
                    if (len(montanteEmpate) > 0):
                        for i in range(0,len(montanteEmpate)):
                            jogador1.append(montanteEmpate[0])
                            montanteEmpate.pop(0)
                    jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)

            elif atributoComputador == 5:
                if nomedoarquivo != "":
                    arq = open("arquivosreplay/"+nomedoarquivo+"1.txt","a")
                    arq.write("5")
                    arq.write(" ")
                    arq.close()
                tela.blit(selecionar,(600,420))
                mostrarCarta1(tela,fotoCarta,nomePersonagem,nomeAtributo1,nomeAtributo2,nomeAtributo3,nomeAtributo4,nomeAtributo5,nomeAtributo6,personagem1)
                tela.blit(selecionar,(120,420))
                pygame.display.flip()
                pygame.time.wait(3000)
                chamarsuperTrunfo1(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo,montanteEmpate)
                
                if jogador2[0][5] > jogador1[0][5]:                        
                    vitoria2(jogador1,jogador2)                      
                    partida = 1
                    if (len(montanteEmpate) > 0):
                        for i in range(0,len(montanteEmpate)):
                            jogador2.append(montanteEmpate[0])
                            montanteEmpate.pop(0)
                    jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)
                        
                elif jogador2[0][5] == jogador1[0][5]:                       
                    empate(jogador1,jogador2)                        
                    partida = 1
                    jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)
                        

                elif jogador2[0][5] < jogador1[0][5]:                  
                    derrotaJogador2(jogador1,jogador2)
                    partida = 0
                    if (len(montanteEmpate) > 0):
                        for i in range(0,len(montanteEmpate)):
                            jogador1.append(montanteEmpate[0])
                            montanteEmpate.pop(0)
                    jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,nomedoarquivo)
        for event in pygame.event.get():
            if (event.type==QUIT):
                exit()
        pygame.display.flip()

        pygame.quit()
                   

        pygame.display.flip()

    pygame.quit()
