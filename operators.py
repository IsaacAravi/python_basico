

#Operaciones Enteros
print(3+4)
print(3-4)
print(3*4)
print(3/4)
print(10 % 3)






#Operaciones con cadenas de texto
print("Hola" + "python" + "¿que tal?")
print("Hola" + str(5))

#Operaciones Mixtas
print("Hola" * 5)
print("Hola" *(2 ** 3))

my_float = 2.5 * 2
print("Hola " * int(my_float))

### Operadores Comparativos ###

# Operaciones con Cadenas de texto
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa") # Ordenación alfabetica pos ASCII
print(len("aaaa") >= len("abaa")) # Cuenta Caracteres
print("Hola" <= "Python")
print("Hola" == "Hola") #comparacion
print("Hola" !="Python") # es igual a 

### Operadores Logicos ###

#Basadas en el Algebra de Boole https://es.wikipedia.org/wiki/%c3%81lgebra_de_Boole
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4))

