import pygame , submenu  #Importa as blibliotecas pygame e também o arquivo submenu no meu diretorio
import os,sys #Importa as funções de os e do sys
from pygame.locals import* #importa todas as funções do pygame para não precisar usar o diretorio  exemplo pygame.exemplo
pygame.init() #Necessario para iniciar as funções de pygame
tempo = pygame.time.Clock()
def ajuda():
    fonteesc = pygame.font.SysFont("Arial.ttf",25)
    voltar = fonteesc.render("Esc - Voltar",True,(255,255,255))
    ajuda = pygame.image.load("imagens/ajuda.png")
    while True:
        tela.blit(ajuda,(0,0))
        tela.blit(voltar,(780,670))
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                teclado = pygame.key.get_pressed()
                if teclado[K_ESCAPE]:
                    return
        pygame.display.flip()
def menuSingleMult():
    while True:
        texto4 = menufont.render('Singleplay',True,(255,255,255))
        texto4Rec = texto4.get_rect().move(550,330)
        texto5 = menufont.render('Multiplay',True,(255,255,255))
        texto5Rec = texto5.get_rect().move(550,380)
        texto8 = menufont.render('Voltar',True,(255,255,255))
        texto8Rec = texto8.get_rect().move(550,430)
        
        tela.blit(background,(0,0))
        tela.blit(texto4,(550,330))
        tela.blit(texto5,(550,380))
        tela.blit(texto8,(550,430))
        if texto4Rec.collidepoint(pygame.mouse.get_pos()):
            texto4 = menufont.render('Singleplay',True,(255,0,0))
            tela.blit(texto4,(550,330))
            if pygame.mouse.get_pressed()[0]:
                pygame.mixer.music.pause()
                import jogopygamesingle
        if texto5Rec.collidepoint(pygame.mouse.get_pos()):
            texto5 = menufont.render('Multiplay',True,(255,0,0))
            tela.blit(texto5,(550,380))
            if pygame.mouse.get_pressed()[0]:
                pygame.mixer.music.pause()
                import jogopygame

        if texto8Rec.collidepoint(pygame.mouse.get_pos()):
            texto8 = menufont.render('Voltar',True,(255,0,0))
            tela.blit(texto8,(550,430))
            if pygame.mouse.get_pressed()[0]:
                return
        for event in pygame.event.get(): #Para o evento receber o tipo do evento 
            if (event.type==QUIT):#se clicar no X da  tela ..
                exit()
        pygame.display.flip()
tamanho = (900,700) #Tamanho que vou usar para tela do jogo
tela = pygame.display.set_mode(tamanho) #variavél tela com a função do pygame que chama a janela do jogo passando como argumento o tamanho que eu quero na tela
autor = pygame.display.set_caption("Super Trunfo") # função que passa com argumento O nome que vai ficar no topo da janela
#Música

#Intro
while True:
    movie = pygame.movie.Movie ('intro.mpg')
    #pygame.mixer.music('intro.mp3')
    #pygame.mixer.music.play()
    tela = pygame.display.set_mode(tamanho)
    movie.set_display (pygame.display.get_surface ())
    movie.play ()
    while movie.get_busy ():
        pygame.time.wait (100)
    break

#pygame.mixer.music.load("Bleach Alternative Opening 7.mp3") # Função que faz o load da música
#pygame.mixer.music.set_volume(.5) #Função que define o volume que a música vai ser executada
#pygame.mixer.music.play(-1) #Função que define o tempo que ficará sendo executada a música (-1) - fica infinita
somClick = pygame.mixer.Sound('som-click.wav') #Função que faz um load de uma música pequena no caso o som de um click.
continuar = True #Variável com o valor True
while continuar: #Enquanto contin   uar for verdadeiro ficar no looping
    tempo.tick(60)
    #Tela Configurações
    background = pygame.image.load("imagens/bleach.png").convert() #Variável com a função de faz um load na imagem e que ficará no fundo

    #TextosFonte
    menufont = pygame.font.Font('dc_o.1.ttf',35) # variável que tem a Função que define a fonte do texto 
    jogofont = pygame.font.Font('gamecuben.ttf',10)# Outra variável que recebe outra fonte
    autortext = jogofont.render('by José Franco Neto / Erickson Silva / Junior Chianca',True,(0,0,0))
    texto1 = menufont.render('Gerenciar carta',True,(255,255,255))#Texto1 com a fonte da variável menufont e que passa como string Gerenciar carta
    texto1Rec = texto1.get_rect().move(450,280)#funçao que define o texto1 com um retangulo para um possivel evento  do mause passando a posição 450 ,280
    texto2 = menufont.render('Jogar',True,(255,255,255))#Texto2 com a fonte da variável menufont e que passa como string jogar
    texto2Rec = texto2.get_rect().move(450,330)#funçao que define o texto2 com um retangulo para um possivel evento  do mause passando a posição 450 ,330
    texto3 = menufont.render('Ajuda',True,(255,255,255))#Texto3 com a fonte da variável menufont e que passa como string ajuda
    texto3Rec = texto3.get_rect().move(450,380)#funçao que define o texto3 com um retangulo para um possivel evento  do mause passando a posição 450 ,380
    texto6 = menufont.render('Replay',True,(255,255,255))
    texto6Rec = texto6.get_rect().move(450,430)
    texto7 = menufont.render('Sair',True,(255,255,255))#Texto4 com a fonte da variável menufont e que passa como string sair
    texto7Rec = texto7.get_rect().move(450,510)#funçao que define o texto4 com um retangulo para um possivel evento  do mause passando a posição 450 ,430
    #Mostrar na tela da janela as variaveis background , texto1,texto2,texto3,texto4 com as suas posicoes no plano x,y

    tela.blit(background,(0,0))
    tela.blit(texto1,(450,280))
    tela.blit(texto2,(450,330))
    tela.blit(texto3,(450,380))
    tela.blit(texto6,(450,430))
    tela.blit(texto7,(450,510))
    pygame.display.flip()
    #Mechendo no menu
    if texto1Rec.collidepoint(pygame.mouse.get_pos()):#Quando o mause passar(colidir) pelo rentangulo do texto 1
        texto1 = menufont.render('Gerenciar carta',True,(255,0,0))#O texto1 vai passar a ter a cor vermelha
        tela.blit(texto1,(450,280))#Aqui mostra na tela da janela o texto 1
        pygame.display.flip()
        if pygame.mouse.get_pressed()[0]:#envento que recebe o click do mouse com o botão esquerdo [0] se clicado...
            somClick.play()# Passa o nome da varial que recebeu o som do click e dá play 
            
            submenu.subMenu()#Chama a função submenu.
    if texto2Rec.collidepoint(pygame.mouse.get_pos()):
        texto2 = menufont.render('Jogar',True,(255,0,0))
        tela.blit(texto2,(450,330))
        pygame.display.flip()
        if pygame.mouse.get_pressed()[0]:
            menuSingleMult()    
    if texto3Rec.collidepoint(pygame.mouse.get_pos()):
        texto3 = menufont.render('Ajuda',True,(255,0,0))
        tela.blit(texto3,(450,380))
        pygame.display.flip()
        if pygame.mouse.get_pressed()[0]:
            ajuda()
    if texto6Rec.collidepoint(pygame.mouse.get_pos()):
        texto6 = menufont.render('Replay',True,(255,0,0))
        tela.blit(texto6,(450,430))
        pygame.display.flip()
        if pygame.mouse.get_pressed()[0]:
            import escolherreplay
            escolherreplay.escolherReplay()        
    if texto7Rec.collidepoint(pygame.mouse.get_pos()):
        texto7 = menufont.render('Sair',True,(255,0,0))
        tela.blit(texto7,(450,510))
        pygame.display.flip()
        if pygame.mouse.get_pressed()[0]:
            continuar = False

    for event in pygame.event.get(): #Para o evento receber o tipo do evento 
        if (event.type==QUIT):#se clicar no X da  tela ..
            continuar = False # Continuar vai ser falso e sairá do while
    pygame.display.flip()#Função para mostrar o que você quer na tela mais rápido     
pygame.quit()#Fecha as funções pygame


