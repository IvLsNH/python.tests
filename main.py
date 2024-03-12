import random
import time

listaDePoss = [10, 35, 50, 120, 125, 150, 200, 300, 345, 500]

print("Roleta da Sorte!")

def Girar():
    print("Girando...")
    time.sleep(2)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    val1 = random.choice(listaDePoss)
    val2 = random.choice(listaDePoss)

    val = val1 - val2

    return val

result = Girar()
print(result)

if result < 0:
    print("Você perdeu dinheiro!")
    
elif result == 0:
    print("Você não ganhou nada!")

else:
    print("Você ganhou dinheiro!")



