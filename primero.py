print(" tienes 3 intentos para saber si tu numero es par")

x= 3
par = 0

while par ==0:

    if x ==0:
        print ("se te acabaron los intentos")
        break

    number = int(input("introduce el numero: "))
    if (number % 2) == 0:
        print ("tu numero es par felicitaciones")
        break
    else:
        print ("tu numero es impar")


    x= x-1
        

