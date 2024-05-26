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