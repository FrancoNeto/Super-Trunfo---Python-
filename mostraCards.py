import pygame , os , sys
from pygame.locals import*
pygame.init()

def mostrandoCartas():
    
    # Definindo o tamanho da tela e o nome que aparecerá na barra de título
    tela = pygame.display.set_mode((900,700))
    pygame.display.set_caption('Super Trunfo')
    background = pygame.image.load('imagens/fundo.png')
    texto = pygame.font.Font("dc_o.ttf", 25)
    textoOP = pygame.font.Font("dc_o.ttf", 35)

    # Pega o total de cartas do baralho

    fontesAtributos = pygame.font.Font("dc_o.1.ttf", 35)
    textoEntrar = fontesAtributos.render('Pressione F2 para escolher a opcao',True,(255,255,255))
  
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
    asCartas.pop(numdecartas)
    fontesAtributos = pygame.font.Font("dc_o.1.ttf", 35)
    contador = 1
    while contador < len(asCartas):
        for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type==pygame.KEYDOWN:
                    teclado = pygame.key.get_pressed()
                    if teclado[K_F2]:
                        print("huhu")
                        return
        
        
        if contador == 1:
            tela.blit(background,(0,0)) 
            imagemCarta = pygame.image.load('imagens/carta.png')
            numeroDaOpcao = textoOP.render(str(contador),True,(255,255,255))
            
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
            tela.blit(imagemCarta,(450 ,20))
            pygame.draw.circle(tela,(0,0,0),(470,30),50)
            tela.blit(nome,(450,60))
            tela.blit(destreza,(600,135))
            tela.blit(zampakutou,(600,185))
            tela.blit(poderEspiritual,(600,230))
            tela.blit(conhecimento,(600,275))
            tela.blit(percEspiritual,(600,320))
            tela.blit(tipo,(600,365))
            tela.blit(imagem,(600,20))
            pygame.draw.rect(tela,(0,0,0),(100,500,620,35))
            tela.blit(numeroDaOpcao,(465,15))
            tela.blit(textoEntrar,(100,500))
            
            
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type==pygame.KEYDOWN:
                    teclado = pygame.key.get_pressed()
                    if teclado[K_F2]:
                        print("aewww")
                        return
            pygame.display.flip()
            pygame.time.wait(3000)
            
        if contador != (len(asCartas)-1): #Contador Condição
            tela.blit(background,(0,0)) 
            imagemCarta = pygame.image.load('imagens/carta.png')
            numeroDaOpcao = textoOP.render(str(contador),True,(255,255,255))
            numeroDaOpcao2 = textoOP.render(str(contador+1),True,(255,255,255))
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
            
            pygame.draw.circle(tela,(0,0,0),(30,30),50)
            pygame.draw.rect(tela,(0,0,0),(100,500,620,35))
            tela.blit(nome,(10,60))
            tela.blit(destreza,(150,135))
            tela.blit(zampakutou,(150,185))
            tela.blit(poderEspiritual,(150,230))
            tela.blit(conhecimento,(150,275))
            tela.blit(percEspiritual,(150,320))
            tela.blit(tipo,(150,365))
            tela.blit(imagem,(150,20))
            
            
            tela.blit(numeroDaOpcao,(25,15))
            tela.blit(textoEntrar,(100,500))
     
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
            pygame.draw.circle(tela,(0,0,0),(495,30),50)
            tela.blit(nome2,(500,60))
            tela.blit(destreza2,(600,135))
            tela.blit(zampakutou2,(600,185))
            tela.blit(poderEspiritual2,(600,230))
            tela.blit(conhecimento2,(600,275))
            tela.blit(percEspiritual2,(600,320))
            tela.blit(tipo2,(600,365))
            
            tela.blit(numeroDaOpcao2,(465,15))
            tela.blit(imagem2,(610,20))
            
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type==pygame.KEYDOWN:
                    teclado = pygame.key.get_pressed()
                    if teclado[K_F2]:
                        return
            pygame.display.flip()
            pygame.time.wait(3000)
            
        else: #contador
        
            tela.blit(background,(0,0)) 
            imagemCarta = pygame.image.load('imagens/carta.png')
            numeroDaOpcao = textoOP.render(str(contador),True,(255,255,255))
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
            pygame.draw.rect(tela,(0,0,0),(100,500,620,35))
            tela.blit(textoEntrar,(100,500))
            

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type==pygame.KEYDOWN:
                    teclado = pygame.key.get_pressed()
                    if teclado[K_F2]:
                        print("bum")
                        return
            pygame.display.flip()
            pygame.time.wait(3000)
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type==pygame.KEYDOWN:
                    teclado = pygame.key.get_pressed()
                    
                    if teclado[K_F2]:
                        print("xaaaa")
                        return
            
        
        contador +=1       

