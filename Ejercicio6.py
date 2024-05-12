'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla
un triángulo rectángulo como el de más abajo.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
'''
num = int(input('Escriba un numero entero: '))

for i in range(1, num + 1, 2): # Bucle externo que itera sobre los números impares hasta el número ingresado
    for j in range(i, 0, -2): # Bucle interno que itera desde el número actual hasta 1, en pasos de -2
        print(j, end=' ')  # Imprime el valor de j seguido de un espacio
    print('')  # Imprime una línea en blanco después de cada conjunto de números impresos
