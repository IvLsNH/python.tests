import time
import random

# lâmpada funciona ou não
lampada = False

# Disponibilidade dos itens necessários para trocar a lâmpada

locaisDaEscada = ['sala', 'garagem', 'pátio', 'despensa']
lampadaEmCasa = False


while lampada == False:

    lampadaEsc = [True, False]

    localDefinido = random.choice(locaisDaEscada)
    
    print("A lâmpada está queimada! \n")

    conseguirLampada = input("Adquirir a lâmpada no mercado ou procurar em casa? \n 1.Mercado \n 2.Casa \n Digite a opção: ")

    if conseguirLampada == 2:
        print("Foi encontrada um lâmpada em Casa!")

    else:
        print("A lâmpada não foi encontrada em Casa.")
        print("Indo ao mercado...")
        time.sleep(5)
        print("Comprando a lâmpada...")
        time.sleep(2)
        print("Voltando para Casa...")
        time.sleep(5)
        print("A lâmpada foi colocada em cima da mesa")

    print("A escada foi encontrada em " + localDefinido)

    print("Colocando a escada debaixo da lâmpada...")
    time.sleep(3)

    print("Pegando a lâmpada que foi deixada em cima da mesa")

    print("Subindo a escada...")
    time.sleep(4)

    print("Efetuando a troca da lâmpada...")
    time.sleep(6)

    print("Descendo a escada...")
    time.sleep(4)

    print("Indo testar a lâmpada")
    lampteste = random.choice(lampadaEsc)
    time.sleep(2)

    if lampteste == True:
        print("A lâmpada está funcionando corretamente!")
        lampada = True
        input()
    else:
        print("A lâmpada ainda não está funcionando.")
        print("Começando a tarefa novamente...")
        time.sleep(5)
