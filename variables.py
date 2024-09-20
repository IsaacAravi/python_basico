###variables###

my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)
print(type(my_int_variable))

my_float_variable = 1.8
print(my_float_variable)
print(type(my_float_variable))

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_viariable = True
print(my_bool_viariable)
print(type(my_bool_viariable))

#concatenacion de variables en un print
print(my_string_variable,my_int_to_str_variable,my_bool_viariable)
print("Este es el valor de:",my_bool_viariable)

# Algunas funciones del sistema
# len obtiene largo de la cadena
print(len(my_string_variable))

# Variables en una sola linea. ¡cuidado con abusat de esta sintaxis!
name, surname, alias , age ="Brais", "Moure", 'MoureDev', 35
print("Me llamo", name, surname, ". Mi edad es:",
      age, ". Y mi alias es:", alias)
      
      
      
      #inputs
name = input('¿cúal es tu nombre?')
age = input('¿Cuanntos años tienes?')
print(name)
print(age)

#Cambiamos su tipo
name = 35
age = "Brais"
print(name)
print(age)
print(type(name))
print(type(age))


#¿Forzamos el tipo?
address: str = "Mi direccion es:"
address = input('¿Cual es tu direccion?')
address = True
address = 5
address = 1.2
print(type(address))