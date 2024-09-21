def read_file(file_name):
    # Lee el archivo quitando los saltos de línea
    with open(file_name, "r", encoding="utf-8") as file:
        return file.read().splitlines()

# Lee el contenido de los .txt
fruit_list = read_file("Frutas.txt")
vegetable_list = read_file("Vegetales.txt")

# Se le pide al usuario ingresar una fruta o verdura
word = input("Ingrese una fruta o vegetal: ")

# Comprueba si la palabra esta en una de las dos listas
if word in fruit_list:
    print(f"La fruta {word} está en la lista de frutas")
elif word in vegetable_list:
    print(f"El vegetal {word} está en la lista de vegetales")
else:
    print(f"{word} no esta en ninguna lista")