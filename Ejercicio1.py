"""
1. Escribir un programa que almacene la cadena de caracteres `contraseña` en una
variable, pregunte al usuario por la contraseña e imprima por pantalla si la
contraseña introducida por el usuario coincide con la guardada en la variable
sin tener en cuenta mayúsculas y minúsculas."""

password = "contraseña"
mensaje = (
    "La contraseña es correcta"
    if input("Introdusca la contraseña: ").lower() == password
    else "La contraseña es inccorrecta"
)
print(mensaje)
