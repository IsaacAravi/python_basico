### Sets ### Conjunto de Valores no ordenados que no se duplican

#Definicion

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set ={"luis", "Bustos", 35}
print(type(my_other_set))

print(len(my_other_set))

# Insercion

my_other_set.add("JesusAA")

print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add("JesusAA")

print(my_other_set)

#Busqueda

print("Luis" in my_other_set)
print("Lois" in my_other_set)

#Eliminacion

my_other_set.remove("Bustos")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
#print (my_other_set) NameError: name 'my_other_set' is not defined

#Transformacion

my_set ={"Luis", "Bustos", 35}# el set siempre se pone en llaves
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"kotlin", "Swift", "Python"}

# Otras operaciones

my_new_set = my_set.union(my_other_set)
print(my_other_set.union(my_new_set).union({"JavaScript", "C#"}))
print(my_new_set.difference(my_set))