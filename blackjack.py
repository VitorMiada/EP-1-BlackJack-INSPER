import random

dinheiro_jogador = 10000

n_baralhos = int(input("Com quantos baralhos você quer jogar? "))*4

baralhos = ["2 ouros","2 paus","2 copas","2 espadas",
            "3 ouros","3 paus","3 copas","3 espadas",
           "4 ouros","4 paus","4 copas","4 espadas",
           "5 ouros","5 paus","5 copas","5 espadas",
            "6 ouros","6 paus","6 copas","6 espadas",
            "7 ouros","7 paus","7 copas","7 espadas",
            "8 ouros","8 paus","8 copas","8 espadas",
            "9 ouros","9 paus","9 copas","9 espadas",
            "10 ouros","10 paus","10 copas","10 espadas",
            "J ouros","J paus","J copas","J espadas",
            "Q ouros","Q paus","Q copas","Q espadas",
            "K ouros","K paus","K copas","K espadas",
            "A ouros","A paus","A copas","A espadas"]






baralho = baralhos * n_baralhos   #juntando todos os baralhos em uma lista


valor = {"2 ouros": 2,"2 paus": 2,"2 copas": 2,"2 espadas": 2,"3 ouros": 3,"3 paus": 3,"3 copas": 3,"3 espadas": 3,
        "4 ouros": 4,"4 paus": 4,"4 copas": 4,"4 espadas": 4,"5 ouros": 5,"5 paus": 5,"5 copas": 5,"5 espadas": 5,
        "6 ouros": 6,"6 paus": 6,"6 copas": 6,"6 espadas": 6,"7 ouros": 7,"7 paus": 7,"7 copas": 7,"7 espadas": 7,
        "8 ouros": 8,"8 paus": 8,"8 copas": 8,"8 espadas": 8,"9 ouros": 9,"9 paus": 9,"9 copas": 9,"9 espadas": 9,
        "10 ouros": 10,"10 paus": 10,"10 copas": 10,"10 espadas": 10,"J ouros": 10,"J paus": 10,"J copas": 10,"J espadas": 10,
        "Q ouros": 10,"Q paus": 10,"Q copas": 10,"Q espadas": 10,"K ouros": 10,"K paus": 10,"K copas": 10,"K espadas": 10,
        "A ouros": 11,"A paus": 11,"A copas": 11,"A espadas": 11}

random.shuffle(baralho)      #embaralhando o baralho



gameover = False
while gameover == False: #esta while: 1 so para fazer loop dpois eu tiro
    soma_jogador = 0
    soma_cpu = 0
    jogador = []
    cpu = []  
    #PARTE DO CPU
    
    
    #parte de escolher as cartas
        
    for i in range(2):   #selecionando as cartas do CPU
        cartas = random.choice(baralho)
        cpu.append(cartas)
    print("----------NOVO JOGO----------")
    print("A carta do CPU é: ",cpu[1])
    for x in valor.keys():
        if x in cpu:
            soma_cpu += valor[x]
    while soma_cpu < 18:
        cartas = random.choice(baralho)
        cpu.append(cartas)
        soma_cpu += valor[cartas]
    print(soma_cpu)
        

                

        
    

        
 
    
    #PARTE DO JOGADOR
    
    
    #parte da aposta
    fim = input("Você quer continuar? ")
    if fim == "nao":
        break
        
    aposta = int(input("Faça uma aposta inicial "))
    while aposta > dinheiro_jogador:
        print("Você não tem dinheiro suficiente")
        aposta = int(input("Faça uma aposta inicial "))
        
     #parte de escolher as cartas   
        
    for i in range(2):    #selecionando as cartas do jogador
        cartas = random.choice(baralho)
        jogador.append(cartas)
    print("Suas cartas são ",jogador)
    mais = input("Mais cartas, digite mais, se não quiser, pressione Enter ")
    while mais == "mais":
        cartas = random.choice(baralho)
        if cartas not in jogador:
            jogador.append(cartas)
        
        
            print(jogador)
        mais = input("Mais cartas, digite mais, se não quiser, pressione Enter ")
        
       #parte de somar os valores de cada carta 
        
    for j in valor.keys():
        if j in jogador:
            soma_jogador += valor[j]   #valor[j], é a carta que ele tem na lista jogador só que com valor numerico
            if "A ouros" in jogador or "A paus" in jogador or "A copas" in jogador or "A espadas" in jogador:                
                if soma_jogador >= 22:
                    q = 0
                    while q < len(jogador):
                        if jogador[q] == "A paus" or jogador[q] =="A copas" or jogador[q] == "A espadas" or jogador[q] == "A ouros":
                            soma_jogador -= 10
                        q +=1
                    
            
            
            #Jogador ganha do CPU 
    if soma_jogador > soma_cpu and soma_jogador <= 21:
        print("Sua soma deu", soma_jogador)
        print("A soma do CPU deu", soma_cpu)
        print("Você ganhou do CPU")
        dinheiro_jogador += aposta * 1.5
        print("Você tem $",dinheiro_jogador)
        
        # Jogador ganha do CPU
        
    elif soma_cpu > 21 and soma_jogador <= 21:
        print("Sua soma deu", soma_jogador)
        print("A soma do CPU deu", soma_cpu)
        print("Você ganhou do CPU")
        dinheiro_jogador += aposta * 1.5
        print("Você tem $",dinheiro_jogador)


        
        
        #Jogador tirar 21
        
        
    elif soma_jogador == 21 and soma_cpu != 21:
        print("Sua soma deu", soma_jogador)
        print("A soma do CPU deu", soma_cpu)
        print("PARABENS, você GANHOU!!")
        dinheiro_jogador += aposta * 1.5
        print("Você esta com $",dinheiro_jogador)
        
        
        
        
        
        
        
         #CPU ganha do jogador
        
    elif soma_jogador < soma_cpu and soma_cpu <= 21:
        print("Sua soma deu", soma_jogador)
        print("A soma do CPU deu", soma_cpu)
        soma_jogador = 0
        print("Você perdeu")
        dinheiro_jogador -= aposta
        print("Você tem $",dinheiro_jogador)

        
        
       #Se a CPU faz blackjack, ganha do jogador: 
        
    elif soma_cpu == 21 and soma_jogador != 21:
        print("Sua soma deu", soma_jogador)
        print("A soma do CPU deu", soma_cpu)
        print("Você perdeu")
        dinheiro_jogador -= aposta 
        print("Você esta com $",dinheiro_jogador)
        
        
        #jogador tira mais que 21
        
    elif soma_jogador > 21 and soma_cpu <= 21:
        
        print("Sua soma deu", soma_jogador)
        print("A soma do CPU deu", soma_cpu)
        jogador = []
        soma_jogador = 0
        print("Você perdeu")
        dinheiro_jogador -= aposta
        print("Você tem $",dinheiro_jogador)
    
    elif soma_jogador > 21 and soma_cpu > 21:
        print("Sua soma deu", soma_jogador)
        print("A soma do CPU deu", soma_cpu)
        jogador = []
        soma_jogador = 0
        print("Ninguém venceu, seu dinheiro retornou")
        dinheiro_jogador += 0
        print("Você tem $",dinheiro_jogador)
        
        
        
    elif soma_jogador == soma_cpu:
        print("Sua soma deu", soma_jogador)
        print("A soma do CPU deu", soma_cpu)
        jogador = []
        soma_jogador = 0
        print("Ninguém venceu, seu dinheiro retornou")
        dinheiro_jogador += 0
        print("Você tem $",dinheiro_jogador)
        
        
        
    if dinheiro_jogador == 0:
        print("Você não tem mais dinheiro para apostar :)")
        break

    
    

#falta :multijogador
