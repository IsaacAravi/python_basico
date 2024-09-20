"""
my_string = "Mi string"
my_other_string ='Mi otro string'

#print(len(my_string))
#print(len(my_other_string))
#print(my_string + "" + my_other_string)

my_new_line_string = "Este es un string\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulacion"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\ n escapado"
print(my_scape_string)

#Formato
name, lastname, age = "Isaac", "Araujo", 33
print("Mi nombres es {} {} y mi edad es {}".format(name, lastname, age))
print("Mi nombres es %s %s y mi edad es %d"%(name, lastname, age))
print("Mi nombres es" + name + "" + lastname + "y mi edad es" + str(age))
print(f"Mi nombre es {name} {lastname} y mi edad es {age}")
"""

#Desempacado de caracteres

language = "python"
"""
a, b, c, d, e, f = language
print(b)
print(e)

# División


language_slice = language [1:3]
print(language_slice)

language_slice = language [0:5]
print(language_slice)

language_slice = language [-2]
print(language_slice)

language_slice = language [6:0:2]
print(language_slice)

language_slice = language [0:7:2]
print(language_slice)

reversed_language = language [::-1]
print(reversed_language)
"""

#Funciones del lenguaje con  cadenas
print(language.capitalize())
print(language.upper())
print(language.count(t))
print(language.isnumeric())
print("1".isnumeric)
print(language.lower())
print(language.lower().isupper())
print(language.startswicht("py"))
print("Py" =="py") #No es lo mismo