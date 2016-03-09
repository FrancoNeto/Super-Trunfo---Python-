import pygame

import os,sys
from pygame.locals import*
pygame.init()
tempo = pygame.time.Clock()

def cadastrarCarta():
    tamanho = (900,700)
    tela = pygame.display.set_mode(tamanho)#Cria uma tela com dimensões do tamanho(900,700)
    autor = pygame.display.set_caption("Super Trunfo")#Define o nome da tela
    background = pygame.image.load("imagens/bleach.png").convert()
    fotoCarta = pygame.image.load("imagens/cadastro.png").convert_alpha()
    #Textos
    fonteEsc = pygame.font.SysFont("Arial.ttf",25)
    voltar = fonteEsc.render("Esc - Voltar",True,(255,255,255))
    fonteTexto = pygame.font.SysFont("Arial.ttf",20)
    nome= ''
    atributo1 = ''
    atributo2 = ''
    atributo3 = ''
    atributo4 = ''
    atributo5 = ''
    atributo6 = ''
    nomePersonagem = fonteTexto.render(nome,True,(0,0,0))
    atributo1Personagem = fonteTexto.render(atributo1,True,(0,0,0))
    atributo2Personagem = fonteTexto.render(atributo1,True,(0,0,0))
    atributo3Personagem = fonteTexto.render(atributo1,True,(0,0,0))
    atributo4Personagem = fonteTexto.render(atributo1,True,(0,0,0))
    atributo5Personagem = fonteTexto.render(atributo1,True,(0,0,0))
    atributo6Personagem = fonteTexto.render(atributo1,True,(0,0,0))
    entrar  = True
    digitarNome1 = True
    digitarAtributo1 = False
    digitarAtributo2 = False
    digitarAtributo3 = False
    digitarAtributo4 = False
    digitarAtributo5 = False
    lista =[]
    while entrar and digitarNome1 : #Nome do personagem
        tela.blit(background,(0,0))
        tela.blit(fotoCarta,(400,100))
        tela.blit(nomePersonagem,(540,185))
        tela.blit(voltar,(790,10))
        for event in pygame.event.get():
            if (event.type==QUIT):
                entrar = False
            elif event.type == pygame.KEYDOWN:
                teclados = pygame.key.get_pressed()
                
                nome = nome + event.unicode
                nomePersonagem = fonteTexto.render(nome,True,(0,0,0))
                pygame.display.flip()
                if teclados[K_ESCAPE]:
                    return 
                if teclados[K_BACKSPACE]:
                    numeroNomeJogador = len(nome)
                    nomeNovoPersonagem = nome[0:numeroNomeJogador - 2]
                    nome= nomeNovoPersonagem
                    nomePersonagem = fonteTexto.render(nome,True,(0,0,0))
                    pygame.display.flip()
                elif teclados[K_RETURN]:
                    numeroNomeJogador = len(nome)
                    nomeNovoPersonagem = nome[0:numeroNomeJogador - 1]
                    nome= nomeNovoPersonagem
                    nome = nome.upper()
                    nomePersonagem = fonteTexto.render(nome,True,(0,0,0))
                    nome = nome.replace(" ","_")
                    lista.append(nome)
                    lista.append(" ")
                    digitarNome1 = False        
        pygame.display.flip()
    digitarAtributo1 = True
    while entrar and digitarAtributo1: #Atributo 1
        tela.blit(background,(0,0))
        tela.blit(fotoCarta,(400,100))
        tela.blit(nomePersonagem,(540,185))
        tela.blit(atributo1Personagem,(540,230))
        tela.blit(voltar,(790,10))
        for event in pygame.event.get():
            if (event.type==QUIT):
                entrar = False
            elif event.type == pygame.KEYDOWN:
                teclados = pygame.key.get_pressed()
                if teclados[K_0] == 1 or teclados[K_1] == 1 or teclados[K_2] == 1 or teclados[K_3] == 1 or teclados[K_4] == 1 or teclados[K_5] == 1 or teclados[K_6] == 1 or teclados[K_7] == 1 or teclados[K_8] == 1 or teclados[K_9] == 1:
                    atributo1 = atributo1 + event.unicode
                    atributo1Personagem = fonteTexto.render(atributo1,True,(0,0,0))
                    pygame.display.flip()
                if teclados[K_ESCAPE]:
                    return
                if teclados[K_BACKSPACE]:
                    numeroAtributo1Jogador = len(atributo1)
                    atributo1NovoPersonagem = atributo1[0:numeroAtributo1Jogador - 1]
                    atributo1= atributo1NovoPersonagem
                    atributo1Personagem = fonteTexto.render(atributo1,True,(0,0,0))
                    pygame.display.flip()
                elif teclados[K_RETURN]:
                    numeroAtributo1Jogador = len(atributo1)
                    atributo1NovoPersonagem = atributo1[0:numeroAtributo1Jogador]
                    atributo1= atributo1NovoPersonagem
                    atributo1Personagem = fonteTexto.render(atributo1,True,(0,0,0))
                    lista.append(atributo1)
                    lista.append(" ")
                    digitarAtributo1 = False
        pygame.display.flip()
    digitarAtributo2 = True
    while entrar and digitarAtributo2:#Atributo2
        tela.blit(background,(0,0))
        tela.blit(fotoCarta,(400,100))
        tela.blit(nomePersonagem,(540,185))
        tela.blit(atributo1Personagem,(540,230))
        tela.blit(atributo2Personagem,(540,275))
        tela.blit(voltar,(790,10))
        for event in pygame.event.get():
            if (event.type==QUIT):
                entrar = False
            elif event.type == pygame.KEYDOWN:
                teclados = pygame.key.get_pressed()
                if teclados[K_0] == 1 or teclados[K_1] == 1 or teclados[K_2] == 1 or teclados[K_3] == 1 or teclados[K_4] == 1 or teclados[K_5] == 1 or teclados[K_6] == 1 or teclados[K_7] == 1 or teclados[K_8] == 1 or teclados[K_9] == 1:
                    atributo2 = atributo2 + event.unicode
                    atributo2Personagem = fonteTexto.render(atributo2,True,(0,0,0))
                    pygame.display.flip()
                if teclados[K_ESCAPE]:
                    return    
                if teclados[K_BACKSPACE]:
                    numeroAtributo2Jogador = len(atributo2)
                    atributo2NovoPersonagem = atributo2[0:numeroAtributo2Jogador - 1]
                    atributo2= atributo2NovoPersonagem
                    atributo2Personagem = fonteTexto.render(atributo2,True,(0,0,0))
                    pygame.display.flip()
                elif teclados[K_RETURN]:
                    numeroAtributo2Jogador = len(atributo2)
                    atributo2NovoPersonagem = atributo2[0:numeroAtributo2Jogador]
                    atributo2= atributo2NovoPersonagem
                    atributo2Personagem = fonteTexto.render(atributo2,True,(0,0,0))
                    lista.append(atributo2)
                    lista.append(" ")
                    digitarAtributo2 = False
        pygame.display.flip()
    digitarAtributo3 = True
    while entrar and digitarAtributo3:
        tela.blit(background,(0,0))
        tela.blit(fotoCarta,(400,100))
        tela.blit(nomePersonagem,(540,185))
        tela.blit(atributo1Personagem,(540,230))
        tela.blit(atributo2Personagem,(540,275))
        tela.blit(atributo3Personagem,(540,325))
        tela.blit(voltar,(790,10))
        for event in pygame.event.get():
            if (event.type==QUIT):
                entrar = False
            elif event.type == pygame.KEYDOWN:
                teclados = pygame.key.get_pressed()
                if teclados[K_0] == 1 or teclados[K_1] == 1 or teclados[K_2] == 1 or teclados[K_3] == 1 or teclados[K_4] == 1 or teclados[K_5] == 1 or teclados[K_6] == 1 or teclados[K_7] == 1 or teclados[K_8] == 1 or teclados[K_9] == 1:
                    atributo3 = atributo3 + event.unicode
                    atributo3Personagem = fonteTexto.render(atributo3,True,(0,0,0))
                    pygame.display.flip()
                if teclados[K_ESCAPE]:
                    return
                if teclados[K_BACKSPACE]:
                    numeroAtributo3Jogador = len(atributo3)
                    atributo3NovoPersonagem = atributo3[0:numeroAtributo3Jogador - 1]
                    atributo3= atributo3NovoPersonagem
                    atributo3Personagem = fonteTexto.render(atributo3,True,(0,0,0))
                    pygame.display.flip()
                elif teclados[K_RETURN]:
                    numeroAtributo3Jogador = len(atributo3)
                    atributo3NovoPersonagem = atributo3[0:numeroAtributo3Jogador ]
                    atributo3= atributo3NovoPersonagem
                    atributo3Personagem = fonteTexto.render(atributo3,True,(0,0,0))
                    lista.append(atributo3)
                    lista.append(" ")
                    digitarAtributo3 = False
        pygame.display.flip()
    digitarAtributo4 = True
    while entrar and digitarAtributo4:
        tela.blit(background,(0,0))
        tela.blit(fotoCarta,(400,100))
        tela.blit(nomePersonagem,(540,185))
        tela.blit(atributo1Personagem,(540,230))
        tela.blit(atributo2Personagem,(540,275))
        tela.blit(atributo3Personagem,(540,325))
        tela.blit(atributo4Personagem,(540,370))
        tela.blit(voltar,(790,10))
        for event in pygame.event.get():
            if (event.type==QUIT):
                entrar = False
            elif event.type == pygame.KEYDOWN:
                teclados = pygame.key.get_pressed()
                if teclados[K_0] == 1 or teclados[K_1] == 1 or teclados[K_2] == 1 or teclados[K_3] == 1 or teclados[K_4] == 1 or teclados[K_5] == 1 or teclados[K_6] == 1 or teclados[K_7] == 1 or teclados[K_8] == 1 or teclados[K_9] == 1:
                    atributo4 = atributo4 + event.unicode
                    atributo4Personagem = fonteTexto.render(atributo4,True,(0,0,0))
                    pygame.display.flip()
                if teclados[K_ESCAPE]:
                    return
                if teclados[K_BACKSPACE]:
                    numeroAtributo4Jogador = len(atributo4)
                    atributo4NovoPersonagem = atributo4[0:numeroAtributo4Jogador - 1]
                    atributo4= atributo4NovoPersonagem
                    atributo4Personagem = fonteTexto.render(atributo4,True,(0,0,0))
                    pygame.display.flip()
                elif teclados[K_RETURN]:
                    numeroAtributo4Jogador = len(atributo4)
                    atributo4NovoPersonagem = atributo4[0:numeroAtributo4Jogador]
                    atributo4= atributo4NovoPersonagem
                    atributo4Personagem = fonteTexto.render(atributo4,True,(0,0,0))
                    lista.append(atributo4)
                    lista.append(" ")
                    digitarAtributo4 = False
        pygame.display.flip()
    digitarAtributo5 = True
    while entrar and digitarAtributo5:
        tela.blit(background,(0,0))
        tela.blit(fotoCarta,(400,100))
        tela.blit(nomePersonagem,(540,185))
        tela.blit(atributo1Personagem,(540,230))
        tela.blit(atributo2Personagem,(540,275))
        tela.blit(atributo3Personagem,(540,325))
        tela.blit(atributo4Personagem,(540,370))
        tela.blit(atributo5Personagem,(540,418))
        tela.blit(voltar,(790,10))
        for event in pygame.event.get():
            if (event.type==QUIT):
                entrar = False
            elif event.type == pygame.KEYDOWN:
                teclados = pygame.key.get_pressed()
                if teclados[K_0] == 1 or teclados[K_1] == 1 or teclados[K_2] == 1 or teclados[K_3] == 1 or teclados[K_4] == 1 or teclados[K_5] == 1 or teclados[K_6] == 1 or teclados[K_7] == 1 or teclados[K_8] == 1 or teclados[K_9] == 1:
                    atributo5 = atributo5 + event.unicode
                    atributo5Personagem = fonteTexto.render(atributo5,True,(0,0,0))
                    pygame.display.flip()
                if teclados[K_ESCAPE]:
                    return
                if teclados[K_BACKSPACE]:
                    numeroAtributo5Jogador = len(atributo5)
                    atributo5NovoPersonagem = atributo5[0:numeroAtributo5Jogador - 1]
                    atributo5= atributo5NovoPersonagem
                    atributo5Personagem = fonteTexto.render(atributo5,True,(0,0,0))
                    pygame.display.flip()
                elif teclados[K_RETURN]:
                    numeroAtributo5Jogador = len(atributo5)
                    atributo5NovoPersonagem = atributo5[0:numeroAtributo5Jogador]
                    atributo5= atributo5NovoPersonagem
                    atributo5Personagem = fonteTexto.render(atributo5,True,(0,0,0))
                    lista.append(atributo5)
                    lista.append(" ")
                    digitarAtributo5 = False
        pygame.display.flip()
    digitarAtributo6 = True
    while entrar and digitarAtributo6:
        tela.blit(background,(0,0))
        tela.blit(fotoCarta,(400,100))
        tela.blit(nomePersonagem,(540,185))
        tela.blit(atributo1Personagem,(540,230))
        tela.blit(atributo2Personagem,(540,275))
        tela.blit(atributo3Personagem,(540,325))
        tela.blit(atributo4Personagem,(540,370))
        tela.blit(atributo5Personagem,(540,418))
        tela.blit(atributo6Personagem,(540,460))
        tela.blit(voltar,(790,10))
        for event in pygame.event.get():
            if (event.type==QUIT):
                entrar = False
            elif event.type == pygame.KEYDOWN:
                teclados = pygame.key.get_pressed()
                if teclados[K_0] == 1 or teclados[K_1] == 1 or teclados[K_2] == 1 or teclados[K_3] == 1 or teclados[K_4] == 1 or teclados[K_a]  or  teclados[K_b]   or teclados[K_c]  or  teclados[K_d]: 
                    atributo6 = atributo6 + event.unicode
                    atributo6Personagem = fonteTexto.render(atributo6.upper(),True,(0,0,0))
                    pygame.display.flip()
                if teclados[K_ESCAPE]:
                    return
                if teclados[K_BACKSPACE]:
                    numeroAtributo6Jogador = len(atributo6)
                    atributo6NovoPersonagem = atributo6[0:numeroAtributo6Jogador - 2]
                    atributo6= atributo6NovoPersonagem
                    atributo6Personagem = fonteTexto.render(atributo6.upper(),True,(0,0,0))
                    pygame.display.flip()
                elif teclados[K_RETURN]:
                    numeroAtributo6Jogador = len(atributo6)
                    atributo6NovoPersonagem = atributo6[0:numeroAtributo6Jogador - 1]
                    atributo6= atributo6NovoPersonagem
                    atributo6 = atributo6.upper() #Transforma string para maiúsculo
                    atributo6Personagem = fonteTexto.render(atributo6.upper(),True,(0,0,0))
                    lista.append(atributo6)
                    lista.append(" ")
                    lista.append(atributo6)
                    lista.append("\n")
                    digitarAtributo6 = False
                    print(lista)
        pygame.display.flip()
    arq = open("cartas.txt","a")
    arq.writelines(lista)
    arq.close()
    return
def listarAsCartas():
    # Definindo o tamanho da tela e o nome que aparecerá na barra de título
    tela = pygame.display.set_mode((900,700))
    pygame.display.set_caption('Super Trunfo')
    background = pygame.image.load('imagens/fundo.png')
    texto = pygame.font.Font("dc_o.ttf", 25)
    fonteEsc = pygame.font.SysFont("Arial.ttf",25)
    voltar = fonteEsc.render("Esc - Voltar",True,(255,255,255))

    arq = open("cartas.txt","r")
    obtercartas = arq.read()
    obtercartas = obtercartas.split()
    arq.close()
    numdecartas = int(len(obtercartas)/8)
    asCartas = [[]]
    for i in range(0,numdecartas):
        carta = i * 8
        asCartas[i] = [ obtercartas[carta] , obtercartas[carta + 1] ,obtercartas[carta + 2] ,obtercartas[carta + 3] , obtercartas[carta + 4] , obtercartas[carta + 5] , obtercartas[carta + 6] , obtercartas[carta + 7] ] 
        asCartas.append(asCartas[i])
    asCartas.pop(numdecartas) # Pega o total de cartas do baralho

    fontesAtributos = pygame.font.Font("dc_o.1.ttf", 35)
    
    contador = 1
    while contador < len(asCartas):
        for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type==pygame.KEYDOWN:
                    teclado = pygame.key.get_pressed()
                    if teclado[K_ESCAPE]:
                        print("huhu")
                        return
  
        if contador == 1:
            tela.blit(background,(0,0)) 
            imagemCarta = pygame.image.load('imagens/carta.png')
            if os.path.exists('imagens/'+asCartas[contador][0]+'.png') == True:
                imagem = pygame.image.load('imagens/'+asCartas[contador][0]+'.png')
            else:
                imagem = pygame.image.load("imagens/SEMFOTO.png").convert_alpha()   
            nome = texto.render((asCartas[contador][0].replace("_"," ")+""), True, (255,255,255))
            destreza = fontesAtributos.render((asCartas[contador][1]+""), True, (255,255,255))
            zampakutou = fontesAtributos.render((asCartas[contador][2]+""), True,(255,255,255))
            poderEspiritual = fontesAtributos.render((asCartas[contador][3]+""), True, (255,255,255))
            conhecimento = fontesAtributos.render((asCartas[contador][4]+""), True, (255,255,255))
            percEspiritual = fontesAtributos.render((asCartas[contador][5]+""), True, (255,255,255))
            tipo = fontesAtributos.render((asCartas[contador][6]+""), True, (255,255,255))
            tela.blit(imagemCarta,(420 ,20))
            tela.blit(nome,(450,60))
            tela.blit(destreza,(600,135))
            tela.blit(zampakutou,(600,185))
            tela.blit(poderEspiritual,(600,230))
            tela.blit(conhecimento,(600,275))
            tela.blit(percEspiritual,(600,320))
            tela.blit(tipo,(600,365))
            tela.blit(imagem,(600,20))
            tela.blit(voltar,(790,10))
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type==pygame.KEYDOWN:
                    teclado = pygame.key.get_pressed()
                    if teclado[K_ESCAPE]:
                        print("huhu")
                        return
     
            pygame.display.flip()
            pygame.time.wait(3000)
   
        
        if contador != (len(asCartas)-1): #Contador Condição
            tela.blit(background,(0,0)) 
            imagemCarta = pygame.image.load('imagens/carta.png')
            if os.path.exists('imagens/'+asCartas[contador][0]+'.png') == True:
                imagem = pygame.image.load('imagens/'+asCartas[contador][0]+'.png')
            else:
                imagem = pygame.image.load("imagens/SEMFOTO.png").convert_alpha()   
            nome = texto.render((asCartas[contador][0].replace("_"," ")+""), True, (255,255,255))
            destreza = fontesAtributos.render((asCartas[contador][1]+""), True, (255,255,255))
            zampakutou = fontesAtributos.render((asCartas[contador][2]+""), True,(255,255,255))
            poderEspiritual = fontesAtributos.render((asCartas[contador][3]+""), True, (255,255,255))
            conhecimento = fontesAtributos.render((asCartas[contador][4]+""), True, (255,255,255))
            percEspiritual = fontesAtributos.render((asCartas[contador][5]+""), True, (255,255,255))
            tipo = fontesAtributos.render((asCartas[contador][6]+""), True, (255,255,255))
            tela.blit(imagemCarta,(0 ,20))
            tela.blit(imagemCarta,(450 ,20))
            tela.blit(nome,(10,60))
            tela.blit(destreza,(150,135))
            tela.blit(zampakutou,(150,185))
            tela.blit(poderEspiritual,(150,230))
            tela.blit(conhecimento,(150,275))
            tela.blit(percEspiritual,(150,320))
            tela.blit(tipo,(150,365))
            tela.blit(imagem,(150,20))
            tela.blit(voltar,(790,10))
            if os.path.exists('imagens/'+asCartas[contador+1][0]+'.png') == True:
                imagem2= pygame.image.load('imagens/'+asCartas[contador+1][0]+'.png')
            else:
                imagem2 = pygame.image.load("imagens/SEMFOTO.png").convert_alpha()

            nome2 = texto.render((asCartas[contador+1][0].replace("_"," ")+""), True, (255,255,255))
            destreza2 = fontesAtributos.render((asCartas[contador+1][1]+""), True, (255,255,255))
            zampakutou2 = fontesAtributos.render((asCartas[contador+1][2]+""), True,(255,255,255))
            poderEspiritual2 = fontesAtributos.render((asCartas[contador+1][3]+""), True, (255,255,255))
            conhecimento2 = fontesAtributos.render((asCartas[contador+1][4]+""), True, (255,255,255))
            percEspiritual2 = fontesAtributos.render((asCartas[contador+1][5]+""), True, (255,255,255))
            tipo2= fontesAtributos.render((asCartas[contador+1][6]+""), True, (255,255,255))       
            tela.blit(nome2,(455,60))
            tela.blit(destreza2,(600,135))
            tela.blit(zampakutou2,(600,185))
            tela.blit(poderEspiritual2,(600,230))
            tela.blit(conhecimento2,(600,275))
            tela.blit(percEspiritual2,(600,320))
            tela.blit(tipo2,(600,365))
            tela.blit(imagem2,(610,20))
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type==pygame.KEYDOWN:
                    teclado = pygame.key.get_pressed()
                    if teclado[K_ESCAPE]:
                        print("huhu")
                        return
            pygame.display.flip()
            pygame.time.wait(3000)
        else: #contador
        
            tela.blit(background,(0,0)) 
            imagemCarta = pygame.image.load('imagens/carta.png')
            if os.path.exists('imagens/'+asCartas[contador][0]+'.png') == True:
                imagem = pygame.image.load('imagens/'+asCartas[contador][0]+'.png')
            else:
                imagem = pygame.image.load("imagens/SEMFOTO.png").convert_alpha()   
            nome = texto.render((asCartas[contador][0].replace("_"," ")+""), True, (255,255,255))
            destreza = fontesAtributos.render((asCartas[contador][1]+""), True, (255,255,255))
            zampakutou = fontesAtributos.render((asCartas[contador][2]+""), True,(255,255,255))
            poderEspiritual = fontesAtributos.render((asCartas[contador][3]+""), True, (255,255,255))
            conhecimento = fontesAtributos.render((asCartas[contador][4]+""), True, (255,255,255))
            percEspiritual = fontesAtributos.render((asCartas[contador][5]+""), True, (255,255,255))
            tipo = fontesAtributos.render((asCartas[contador][6]+""), True, (255,255,255))
            tela.blit(imagemCarta,(0 ,20))
            tela.blit(nome,(10,60))
            tela.blit(destreza,(150,135))
            tela.blit(zampakutou,(150,185))
            tela.blit(poderEspiritual,(150,230))
            tela.blit(conhecimento,(150,275))
            tela.blit(percEspiritual,(150,320))
            tela.blit(tipo,(150,365))
            tela.blit(imagem,(150,20))
            tela.blit(voltar,(790,10))
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type==pygame.KEYDOWN:
                    teclado = pygame.key.get_pressed()
                    if teclado[K_ESCAPE]:
                        print("huhu")
                        return
            pygame.display.flip()
            pygame.time.wait(3000)
        contador = contador + 1

    
    subMenu()
    

def subMenu():
    tamanho = (900,700)
    tela = pygame.display.set_mode(tamanho)#Cria uma tela com dimensões do tamanho(900,700)
    autor = pygame.display.set_caption("Super Trunfo")#Define o nome da tela
    somClick = pygame.mixer.Sound('som-click.wav') #Recebe um som para o click 
    
    
                                  
    continuar = True
    while continuar: #Condição pra ficar atualizando a imagem na tela
        tempo.tick(60)
        #Tela Configurações
        background = pygame.image.load("imagens/bleach.png").convert()
        
        #TextosFonte
        menufont = pygame.font.Font('dc_o.1.ttf',35)
        jogofont = pygame.font.Font('gamecuben.ttf',10)
        autortext = jogofont.render('by José Franco Neto / Erickson Silva / Junior Chianca',True,(0,0,0))
        texto1 = menufont.render('Cadastrar carta',True,(255,255,255))
        texto1Rec = texto1.get_rect().move(450,280)
        texto2 = menufont.render('Atualizar carta',True,(255,255,255))
        texto2Rec = texto2.get_rect().move(450,320)
        texto3 = menufont.render('Apagar carta',True,(255,255,255))
        texto3Rec = texto3.get_rect().move(450,360)
        texto4 = menufont.render('Listar cartas',True,(255,255,255))
        texto4Rec = texto4.get_rect().move(450,400)
        texto5 = menufont.render('Voltar',True,(255,255,255))
        texto5Rec = texto5.get_rect().move(450,470)


        tela.blit(background,(0,0))
        tela.blit(texto1,(450,280))
        tela.blit(texto2,(450,320))
        tela.blit(texto3,(450,360))
        tela.blit(texto4,(450,400))
        tela.blit(texto5,(450,470))
        pygame.display.flip()

        #Mechendo no menu
        if texto1Rec.collidepoint(pygame.mouse.get_pos()):
            texto1 = menufont.render('Cadastrar carta',True,(255,0,0))
            tela.blit(texto1,(450,280))
            pygame.display.flip()
            if pygame.mouse.get_pressed()[0]:
                somClick.play()
                cadastrarCarta()
        elif texto2Rec.collidepoint(pygame.mouse.get_pos()):
            texto2 = menufont.render('Atualizar carta',True,(255,0,0))
            tela.blit(texto2,(450,320))
            pygame.display.flip()
            if pygame.mouse.get_pressed()[0]:
                somClick.play()
                import atualizarcarta
                atualizarcarta.atualizar()



        
        elif texto3Rec.collidepoint(pygame.mouse.get_pos()):
            texto3 = menufont.render('Apagar carta',True,(255,0,0))
            tela.blit(texto3,(450,360))
            pygame.display.flip()
            if pygame.mouse.get_pressed()[0]:
                somClick.play()
                import apagarcartas
                apagarcartas.apagar()

        elif texto4Rec.collidepoint(pygame.mouse.get_pos()):
            texto4 = menufont.render('Listar cartas',True,(255,0,0))
            tela.blit(texto4,(450,400))
            pygame.display.flip()
            if pygame.mouse.get_pressed()[0]:
                somClick.play()
                listarAsCartas()            
        elif texto5Rec.collidepoint(pygame.mouse.get_pos()):
            texto5 = menufont.render('Voltar',True,(255,0,0))
            tela.blit(texto5,(450,470))
            pygame.display.flip()
            if pygame.mouse.get_pressed()[0]:
                somClick.play()
                return
        for event in pygame.event.get():
            if (event.type==QUIT):
                continuar = False
        pygame.display.flip()
    pygame.quit()


