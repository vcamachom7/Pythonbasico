# Numeros
print(int(7))
print(float(7.7))
type(7)
type(7.7)
print(int(1+2))
print(int(10*2))
print(int(1 + 4 - 2))
print(float(1 + 2.0))


# Operadores de matematicas
# +
# -
# *
# /
# **
# % Modulo


print(int(2**3))
print(int(4**9))
print(float(10%3))
print(float(26%4))
print(float(16%2))
print(float(10/3))


# Variables
print("========VARIABLES========")
x = 100
y = 1
print(x+y)


ventas = 199991
print("Nuestras ventas fueron:", ventas)


is_active = True
print(is_active)


game_over = False
print(game_over)


some_string = "Hola soy un sting"
print(some_string)


print("=========Condicionales========")
edad = 18


if(edad >= 18):
    print("Si puedo entrar a el Bar!!!")
else:
    print("No puedo entrar a el Bar!!!")


print("========FUNCIONES DE PAR_IMPAR========")
mi_numero = int(input("Cual es numero que deseas verificar:"))
if mi_numero % 2 == 0:
    print(f"El numero {mi_numero} par!")
else:
    print(f"El numero {mi_numero} es impar!")


def par_impar(numero):
    if numero % 2 == 0:
        print(f"El numero {numero} es par!")
    else:
        print(f"El numero {numero} es impar!")


mi_numero = int(input("Cual es numero que deseas verificar?:"))
print(f"El numero que deseas verificar es {mi_numero}")
print(par_impar (mi_numero))

