import random

dinheiro_jogador = 10000

n_baralhos = int(input("Com quantos baralhos você quer jogar? "))*4

baralhos = ["2","3","4","5","6","7","8","9","J","Q","K","A"]

baralho = baralhos * n_baralhos   #juntando todos os baralhos em uma lista

valor = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8,
         "9":9, "J":10, "Q": 10, "K":10, "A":1}

random.shuffle(baralho)      #embaralhando o baralho



#gameover == False
while 1: #esta while: 1 so para fazer loop dpois eu tiro
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
        

                

        
    

        
 
    
    #PARTE DO JOGADOR
    
    
    #parte da aposta
    fim = input("Você quer continuar? ")
    if fim == "nao":
        #gameover == True
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
        jogador.append(cartas)
        print(jogador)
        mais = input("Mais cartas, digite mais, se não quiser, pressione Enter ")
        
       #parte de somar os valores de cada carta 
        
    for j in valor.keys():
        if j in jogador:
            soma_jogador += valor[j]   #valor[j], é a carta que ele tem na lista jogador só que com valor numerico
            if 21 - soma_jogador == 11 and "A" in jogador:
                soma_jogador == 21 #O As vira 11 quando a somatoria do A sendo 11 + o resto = 21, caso contrario ele valerá 1. Certo?
        #parte de ver se o jogador perdeu/venceu    
            
            
            
            #Jogador ganha do CPU por maior soma mas n chega em 21
    if soma_jogador > soma_cpu and soma_jogador <= 21:
        print("Sua soma deu", soma_jogador)
        print("A soma do CPU deu", soma_cpu)
        print("Você ganhou do CPU")
        dinheiro_jogador += aposta * 1.5
        print("Você tem $",dinheiro_jogador)
        jogador = []
        cpu = []
        
        
        #jogador tira 21
        
        
    if soma_jogador == 21 and soma_cpu != 21:
        print("Sua soma deu", soma_jogador)
        print("A soma do CPU deu", soma_cpu)
        print("PARABENS, você GANHOU!!")
        dinheiro_jogador += aposta * 1.5
        print("Você esta com $",dinheiro_jogador)
        jogador = []
        cpu = []
        
         #CPU ganha do jogador
        
    if soma_jogador < soma_cpu and soma_cpu <= 21:
        print("Sua soma deu", soma_jogador)
        print("A soma do CPU deu", soma_cpu)
        jogador = []
        soma_jogador = 0
        print("Você perdeu")
        dinheiro_jogador -= aposta
        print("Você tem $",dinheiro_jogador)
        cpu = []
        
        
        
       #Se a CPU faz blackjack, ganha do jogador: 
        
    if soma_cpu == 21 and soma_jogador != 21:
        print("Sua soma deu", soma_jogador)
        print("A soma do CPU deu", soma_cpu)
        print("Você perdeu")
        dinheiro_jogador -= aposta 
        print("Você esta com $",dinheiro_jogador)
        jogador = []
        cpu = []
        
        
        #jogador tira mais que 21
        
    if soma_jogador > 21:
        
        print("Sua soma deu", soma_jogador)
        print("A soma do CPU deu", soma_cpu)
        jogador = []
        soma_jogador = 0
        print("Você perdeu")
        dinheiro_jogador -= aposta
        print("Você tem $",dinheiro_jogador)
        cpu = []
        
    if dinheiro_jogador == 0:
        print("Você não tem mais dinheiro para apostar :)")
        break #gambiarra para parar o jogo

    
    



#oq falta: fazer o blackjack pro CPU, colocar as features(ja fiz a feature da aposta, fim qnd fim e multiplos baralhos), mudar o valor de A para 1 ou 11(eu fiz mas n sei se ta certo)
