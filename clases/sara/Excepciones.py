# Para poder agarrar excepciones, ponemos dentro de un try lo que queremos comprobar
try:
    print(x)
except NameError:
    print("No existe lo que queres imprimir")
except:
    print("Ocurrio algun error")

try:
    print(5/0)
except NameError:
    print("No existe lo que queres imprimir")
except:
    print("Ocurrio algun error")

try:
    num = int(input("Ingrese un numero: "))
    print(num / 2)
except ValueError:
    print("No ingresaste un numero!")
except TypeError:
    print("Ingresaste algo del tipo erroneo")
else:  # este else solo se ejecuta cuando el try se ejecuta exitosamente
    print("Exito!")
finally:  # se ejecuta SIEMPRE al finalizar el try except
    print("Me ejecuto si hay errores o no")


# Ejemplo de uso de finally, TODO ver bien como es el manejo de ficheros
try:
    fichero = open("hola.txt")
    fichero.write("Hola")
except:
    print("Ocurrio algun error")
finally:
    fichero.close()

# ejecutar un bucle hasta que la persona ingrese un numero positivo
incorrecto = True
while incorrecto:
    try:
        num = int(input("Ingrese un numero positivo: "))
        if num > 0:
            incorrecto = False
        else:
            print("No ingresaste un numero positivo")
    except ValueError:
        print("No ingresaste un numero")

print("Ingresate exitosamente un numero positivo!!!")
