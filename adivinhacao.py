import random

print("Bem vindo ao jogo do advinha")

numero_secreto = random.randrange(1,101)
total_tentativas = 0

print("Escolha qual nível de dificuldade")
print("(1) Fácil  (2) Médio  (3) Difícil")

nivel = int(input("Digite o Nível :"))

if(nivel == 1 ):
    total_tentativas = 20

elif (nivel == 2):
    total_tentativas = 15

else:
        total_tentativas = 10


for rodada in range(1,total_tentativas +1):

    print("Tentativa {} de {} " .format( rodada , total_tentativas))

    chute_str = input("Digite um número entre 1 e 100 : ")
    chute = int(chute_str)
    print("você digitou  ", chute)

    if(chute < 1 or chute > 100):
        print("Você errou! Tente chutar um numero entre 1 e 100")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    fim = total_tentativas == 0

    if (acertou):
           print("Parabéns, Você acertou")
           break
    else:
        if (maior):
         print("Você errou ! Seu chute foi acima")
        else:
            if(menor):
              print("Você errou! Seu chute foi menor")
            else:
                if(fim):
                    print("Fim de jogo")







