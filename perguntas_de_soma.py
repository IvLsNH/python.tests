import random
import time

enter = True

class txtcolors:
    CORRECT = "\033[92m"  # Verde
    NUM = "\033[93m"  # Amarelo
    FAIL = "\033[91m"  # Vermelho
    RESET = "\033[0m"  # Resetar a cor

while enter == True:

    num1 = random.randrange(20, 9999)
    num2 = random.randrange(20, 9999)
    soma = num1 + num2
    print(soma)

    print(f"Operação:{txtcolors.NUM} {num1} + {num2} {txtcolors.RESET} ")
    
    #           Transformar em Inteiro, pois o valor recebido pela input é uma Sting
    resultado = int(input("Digite o resultado: "))

    if resultado == (num1 + num2):
        print(f"{txtcolors.CORRECT}Resposta Correta!{txtcolors.RESET}")
        time.sleep(5)
    else:
        print(f"{txtcolors.FAIL}Resposta incorreta!{txtcolors.RESET} \nO resultado era: {num1 + num2}")
        time.sleep(5)

    continuar = int(input("1 para continuar \n2 para sair \n "))

    if continuar != 1:
        enter = False
        
