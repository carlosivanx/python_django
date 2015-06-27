from random import randint
print ("Bem vindo")

#print (numero_sorteado)
novo_jogo = True
while novo_jogo != False:
    numero_sorteado = randint(1,100)
    contador = 1
    while True:
        chute = int(input("chute um numero: "))
        if chute == numero_sorteado:
            print ("parabens, vc é o cara")
            break
        else:
            print("Alto" if chute > numero_sorteado else "Baixo")

        contador +=1
    print("Fim de jogo!!")
    print("Numero sorteado: " + str(numero_sorteado))
    print("Numero chutado: " + str(chute))
    print("Numero de tentativas: "+ str(contador))
    novo_jogo = int(input("Jogar novamente? 1 - Sim ou 0 - Nao: "))

