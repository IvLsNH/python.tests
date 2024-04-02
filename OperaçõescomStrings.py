#Operações com Strings - 02/04/2024

nome = "Ivan Lucas Schaurich"
idade = 16
altura = 1.70


#Composição com marcador de %:

print("Me chamo %s." % nome)
                # %s --> String

print("Tenho %d anos." % idade)
            # %d --> Digito numérico Inteiro

print("Tenho %.2f de altura" % altura)
            # %f --> Float
            #.2 é usado para determinar o numero de casas decimais

print("Sou %s tenho %d anos e %.2f de altura." %(nome, idade, altura))
                                                  #Parênteses para mais de um valor

#Utilizando o Format:
print("Meu nome é {} e tenho {} anos".format(nome, idade))
