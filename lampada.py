import time

# lâmpada funciona ou não
lampada = False

# Disponibilidade dos itens necessários para trocar a lâmpada

escada = True
lampadaEmCasa = True


while lampada == False:
    print("A lâmpada está queimada! \n")

    conseguirLampada = input("Adquirir a lâmpada no mercado ou procurar em casa? \n 1.Mercado \n 2.Casa \n Digite a opção: ")

    if conseguirLampada == True:
        print("Foi encontrada um lâmpada em Casa!")

    else:
        print("A lampada não foi encontrada em Casa.")
        print("Indo ao mercado...")
        time.sleep(5)
        
    


    
