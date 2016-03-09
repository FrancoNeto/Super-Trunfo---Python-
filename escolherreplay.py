import pygame
from pygame.locals import*
pygame.init()
def escolherReplay():
    tamanho = (900,700)
    tela = pygame.display.set_mode(tamanho)
    pygame.display.set_caption('Super Trunfo')
    background = pygame.image.load('imagens/fundoR.png')
    text = pygame.font.SysFont("arial.ttf", 30)
    arquivo = open("arquivosreplay/nomesreplay.txt","r")
    listaDeCodigo = arquivo.read()
    listaDeCodigo = listaDeCodigo.split()
    arquivo.close()
    totalDecodigos = int(len(listaDeCodigo)/3)
    codigosReplay = [[]]
    for i in range(0,totalDecodigos):
        carta = i * 3
        codigosReplay[i] = [ listaDeCodigo[carta] , listaDeCodigo[carta + 1] , listaDeCodigo[carta + 2]] 
        codigosReplay.append(codigosReplay[i])
    codigosReplay.pop(totalDecodigos)
    print(codigosReplay)
    replay1 = text.render(listaDeCodigo[0],True,(255,255,255))
    op = ''
    opcao = text.render("Digite o código:" + op ,True,(255,255,255))
    voltarMenu = text.render("Aperte ESC para voltar",True,(255,255,255))
    espaco = 0
    espaco1 = 0
    codigosReplay.reverse()
    print(codigosReplay)
    for i in range(0,totalDecodigos):
        if i <= 10:
            espaco += 20
            replay = text.render("Cod.  -  "+codigosReplay[i][0]+"  -   "+codigosReplay[i][1]+" "+codigosReplay[i][2][0:5],True,(255,255,255))
            tela.blit(replay,(5,espaco))
            pygame.display.flip()
        elif i > 10 and i <= 20:
            
            espaco1 += 20
            replay = text.render("Cod.  -  "+codigosReplay[i][0]+"  -   "+codigosReplay[i][1]+" "+codigosReplay[i][2][0:5],True,(255,255,255))
            tela.blit(replay,(370,espaco1))
            pygame.display.flip()

    while True:
        tela.blit(background,(0,0)) 
       
        tela.blit(voltarMenu,(650,525)) 
        tela.blit(opcao,(10,400))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                teclado = pygame.key.get_pressed()
                op += event.unicode
                
                opcao = text.render("Digite o código:  " + op.upper() ,True,(255,255,255))
                pygame.display.flip()
                if teclado[K_BACKSPACE]:
                    numeroOP = len(op)
                    novo = op[0:numeroOP - 2]
                    op= novo
                    opcao = text.render("Digite o código:  " + op.upper() ,True,(255,255,255))
                    pygame.display.flip()
                if teclado[K_ESCAPE]:
                    return
                if teclado[K_RETURN]:
                    numeroOP = len(op)
                    novo = op[0:numeroOP - 1]
                    op = novo
                    op.upper()
                    pygame.mixer.music.pause()
                    #Música
                    pygame.mixer.music.load("bleachmusic.mp3") # Função que faz o load da música
                    pygame.mixer.music.set_volume(.5) #Função que define o volume que a música vai ser executada
                    pygame.mixer.music.play(-1) #Função que define o tempo que ficará sendo executada a música (-1) - fica infinita

                    import replay
                    replay.replayRodada(op)
      
escolherReplay()
