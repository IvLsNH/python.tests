
    
import time
import random

# lâmpada funciona ou não
lampada = False

# Disponibilidade dos itens necessários para trocar a lâmpada

locaisDaEscada = ['sala', 'garagem', 'pátio', 'despensa']
lampadaEmCasa = False


while lampada == False:

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

    print("A escada foi encontrada em " + localDefinido)


    

        
    


    
