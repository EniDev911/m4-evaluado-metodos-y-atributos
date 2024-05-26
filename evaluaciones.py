from pizza import Pizza


print(Pizza.precio)
print(Pizza.tamanio)
print(Pizza.validar("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

p = Pizza()

p.ordenar()

print(f"Ingredientes Vegetales: {p.vegetal1}, {p.vegetal2}")
print(f"Ingrediente Proteico: {p.proteico}")
print(f"Tipo de masa: {p.t_masa}")
print(f"¿Es una pizza válida?: {p.es_valido}")

""" REQUERIMIENTO 5

Usar la función print(), para mostrar en pantalla
si la clase Pizza es una pizza válida o no,
sin crear una instancia de la clase. En este punto,
la ejecución del script debe mostrar un error
(todos los pasos anteriores se deben haber ejecutado correctamente).
"""
print(Pizza.es_valido)
