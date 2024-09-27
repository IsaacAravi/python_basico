

### tuples ###

# Definicion

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (33, 1.77, "Jesus", "Araujo", "Jesus")
my_other_tuple = (33, 60, 30)
"""
print(my_tuple)
print(type(my_tuple))

# Acceso a elementos y búsqueda

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

print(my_tuple.count("Jesus"))
print(my_tuple.index("Araujo"))
print(my_tuple.index("Jesus"))

# my_tuple[1] = 1.80 'tuple' object does not support item assignment
"""
#Concatenacion

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# subtuplas

print(my_sum_tuple[3:6])

# tupla mutable con conversion a lista

my_sum_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4]="JesusAA"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

#Eliminacion

#del my_tuple[1] object does not support item assignment

del my_tuple
print(my_tuple)

