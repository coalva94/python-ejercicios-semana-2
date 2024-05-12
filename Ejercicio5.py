'''
Solicita al usuario ingresar un número, lo divide por 10 y muestra el resultado.
Si el usuario ingresa algo que no puede convertirse en un entero (ValueError) o
intenta dividir por cero (ZeroDivisionError), el programa captura la excepción y
muestra un mensaje de error adecuado.
'''
try:
    usuario = int(input('Ingrese un número: '))
    resultado = usuario / 10
    print('El resultado es: ',resultado)
except ValueError:
    print('Error: Debes introducir un número válido')

except ZeroDivisionError:
    print('Error: Debes introducir un número válido')
