fruit_list = ["Manzana", "Banano", "Pera", "Uva"]
vegetable_list = ["Cebolla", "Ajo", "Cilantro", "Perejil"]

word = input("Ingrese una fruta o vegetal: ")

if word in fruit_list:
    print(f"La fruta {word} esta en la lista de frutas")
elif word in vegetable_list:
    print(f"El vegetal {word} esta en la lista de vegetales")
else:
    print(f"{word} no esta en ninguna de las dos listas")

