#Pegando a segunda metade da frase --> 09/04/2024

frase = input('Digite a sua frase: ')

metade_da_frase = (len(frase) // 2)

sgnd_mtd = frase[metade_da_frase: ]

print(f'''A metade da frase possui {metade_da_frase} letras de comprimento.
A 2º metade da frase é {sgnd_mtd}.
''')
