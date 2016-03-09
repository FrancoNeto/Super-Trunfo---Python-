import pygame , sys , os
import mostraCards
from pygame.locals import*
pygame.init()

def atualizar():
    tamanho = (900,700)
    tela = pygame.display.set_mode(tamanho)
    pygame.display.set_caption('Super Trunfo')  
    background = pygame.image.load('imagens/fundo.png')
    text = pygame.font.SysFont("arial.ttf", 30)
    texto = pygame.font.SysFont("Arial.ttf", 25)
    fontesAtributos = pygame.font.Font("dc_o.1.ttf", 35)
    arq = open("cartas.txt","r")
    obtercartas1 = arq.read()
    obtercartas1 = obtercartas1.split()
    arq.close()
    numdecartas = int(len(obtercartas1)/8)
    cartasdividi = [[]]
    for i in range(0,numdecartas):
        carta = i * 8
        cartasdividi[i] = [ obtercartas1[carta] , obtercartas1[carta + 1] , obtercartas1[carta + 2] , obtercartas1[carta + 3] , obtercartas1[carta + 4] , obtercartas1[carta + 5] , obtercartas1[carta + 6] , obtercartas1[carta + 7] ] 
        cartasdividi.append(cartasdividi[i])
    cartasdividi.pop(numdecartas)
    numDaCarta = ""
    valorAtributo = ""
    valorNovoAtributo = ""
    cartaApagar = texto.render("Numero da carta :" +numDaCarta,True,(255,255,255))
    atributoApagar = texto.render("Numero do atributo:" + valorAtributo ,True,(255,255,255))
    atributoNovo = texto.render("Novo valor:" + valorNovoAtributo ,True,(255,255,255))
    verDeNovo = texto.render("Esc - Ver cartas",True,(255,255,255))
    voltarMenu = texto.render("F1 - Voltar menu",True,(255,255,255))
    def mostrarCarta(cartasdividi,numDaCarta):
        tela.blit(background,(0,0))
        pygame.draw.rect(tela,(0,0,0),(25,496,400,30))
        numDaCarta = int(numDaCarta)
        if os.path.exists('imagens/'+cartasdividi[numDaCarta][0]+'.png') == True:
            imagem = pygame.image.load('imagens/'+cartasdividi[numDaCarta][0]+'.png')
        else:
            imagem = pygame.image.load("imagens/SEMFOTO.png").convert_alpha()
        imagemCarta = pygame.image.load('imagens/carta.png')
        nome = texto.render("0-"+cartasdividi[numDaCarta][0].replace("_"," "), True, (255,255,255))
        destreza = fontesAtributos.render("1-"+cartasdividi[numDaCarta][1], True, (255,255,255))
        zampakutou = fontesAtributos.render("2-"+cartasdividi[numDaCarta][2], True,(255,255,255))
        poderEspiritual = fontesAtributos.render("3-"+cartasdividi[numDaCarta][3], True, (255,255,255))
        conhecimento = fontesAtributos.render("4-"+cartasdividi[numDaCarta][4], True, (255,255,255))
        percEspiritual = fontesAtributos.render("5-"+cartasdividi[numDaCarta][5], True, (255,255,255))
        tipo = fontesAtributos.render("6-"+cartasdividi[numDaCarta][6], True, (255,255,255))
        tela.blit(imagemCarta,(0 ,20))
        tela.blit(nome,(10,60))
        tela.blit(destreza,(150,135))
        tela.blit(zampakutou,(150,185))
        tela.blit(poderEspiritual,(150,230))
        tela.blit(conhecimento,(150,275))
        tela.blit(percEspiritual,(150,320))
        tela.blit(tipo,(150,365))
        tela.blit(imagem,(150,20))
        pygame.display.flip()
    continuar = True
    entrar = True
    atributo1 = False
    mostraCards.mostrandoCartas()
    while continuar and entrar:  #Fora da função
        tela.blit(background,(0,0))
        pygame.draw.rect(tela,(0,0,0),(618,8,250,50))
        pygame.draw.rect(tela,(0,0,0),(95,96,250,30))
        tela.blit(cartaApagar,(100,100))
        tela.blit(verDeNovo,(620,10))
        tela.blit(voltarMenu,(620,30))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN:                                                                                                                   
                teclado = pygame.key.get_pressed()
                if (teclado[K_0] == 1 or teclado[K_1] == 1 or teclado[K_2] == 1 or teclado[K_3] == 1 or teclado[K_4] == 1 or teclado[K_5] == 1 or teclado[K_6] == 1 or teclado[K_7] == 1 or teclado[K_8] == 1 or teclado[K_9] == 1):
                    numDaCarta += event.unicode
                    cartaApagar = texto.render("Numero da carta :" +numDaCarta,True,(255,255,255))
                    pygame.display.flip()
                if teclado[K_F1]:
                    return
                if teclado[K_ESCAPE]:
                    atualizar()
                if teclado[K_BACKSPACE]:
                    tamanhoN = len(numDaCarta)
                    novo = numDaCarta[0:tamanhoN-1]
                    numDaCarta = novo
                    cartaApagar = texto.render("Numero da carta :" +numDaCarta,True,(255,255,255))
                    pygame.display.flip()
                if teclado[K_RETURN]:
                    tamanhoN = len(numDaCarta)
                    novo = numDaCarta[0:tamanhoN]
                    numDaCarta = novo
                    entrar = False
                    atributo1 = True
                
    while continuar and atributo1:
        tela.blit(background,(0,0))
        pygame.draw.rect(tela,(0,0,0),(95,96,250,30))
        mostrarCarta(cartasdividi,numDaCarta)
        pygame.draw.rect(tela,(0,0,0),(618,8,250,50))
        tela.blit(atributoApagar,(10,500))
        tela.blit(verDeNovo,(620,10))
        tela.blit(voltarMenu,(620,30))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN:                                                                                                                   
                teclado = pygame.key.get_pressed()
                if (teclado[K_0] == 1 or teclado[K_1] == 1 or teclado[K_2] == 1 or teclado[K_3] == 1 or teclado[K_4] == 1 or teclado[K_5] == 1 or teclado[K_6] == 1 ):
                    valorAtributo += event.unicode
                    atributoApagar = texto.render("Numero do atributo:" + valorAtributo,True,(255,255,255))
                    pygame.display.flip()
                if teclado[K_F1]:
                    return
                if teclado[K_ESCAPE]:
                    atualizar()
                if teclado[K_BACKSPACE]:
                    tamanhoN = len(valorAtributo)
                    novo = valorAtributo[0:tamanhoN-1]
                    valorAtributo = novo
                    atributoApagar = texto.render("Numero do atributo:" + valorAtributo,True,(255,255,255))
                    pygame.display.flip()
                if teclado[K_RETURN]:
                    tamanhoN = len(valorAtributo)
                    novo = valorAtributo[0:tamanhoN]
                    valorAtributo = novo
                    atributo1 = False
                    novoAtributo = True
    while continuar and novoAtributo:
        mostrarCarta(cartasdividi,numDaCarta)
        pygame.draw.rect(tela,(0,0,0),(8,525,50,30))
        tela.blit(atributoApagar,(10,500))
        tela.blit(atributoNovo,(10,530))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN:                                                                                                                   
                teclado = pygame.key.get_pressed()
                if (teclado[K_0] == 1 or teclado[K_1] == 1 or teclado[K_2] == 1 or teclado[K_3] == 1 or teclado[K_4] == 1 or teclado[K_5] == 1 or teclado[K_6] == 1 or teclado[K_7] == 1 or teclado[K_8] == 1 or teclado[K_9] == 1):
                    valorNovoAtributo += event.unicode
                    atributoNovo = texto.render("Novo valor:" + valorNovoAtributo ,True,(255,255,255))
                    pygame.display.flip()
                if teclado[K_BACKSPACE]:
                    tamanhoN = len(valorNovoAtributo)
                    novo = valorNovoAtributo[0:tamanhoN-1]
                    valorNovoAtributo = novo
                    atributoNovo = texto.render("Novo valor:" + valorNovoAtributo ,True,(255,255,255))
                    pygame.display.flip()
                if teclado[K_RETURN]:
                    tamanhoN = len(valorNovoAtributo)
                    novo = valorNovoAtributo[0:tamanhoN]
                    valorNovoAtributo = novo
                    numDaCarta = int(numDaCarta)
                    valorAtributo = int(valorAtributo)
                    cartasdividi[numDaCarta][valorAtributo] = str (valorNovoAtributo)
                    mostrarCarta(cartasdividi,numDaCarta)        
                    numDaCarta = int(numDaCarta)
                    os.remove("cartas.txt")
                    for i in range(len(cartasdividi)):
                        abrirarq = open("cartas.txt","a")
                        abrirarq.write("%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s" %(cartasdividi[i][0]," ",cartasdividi[i][1]," ",cartasdividi[i][2]," ",cartasdividi[i][3]," ",cartasdividi[i][4]," ",cartasdividi[i][5]," ",cartasdividi[i][6]," ",cartasdividi[i][7],"\n"))
                        abrirarq.close()
                    pygame.time.wait(4000)
                    
                    return
                    
                        
        







