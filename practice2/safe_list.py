#Escribe get_item(lst, index) 
# que retorne None (en vez de fallar) cuando el índice esté fuera de rango.

def get_item(lst, index):
    try: 
        return lst[index]
    except IndexError:
        return None

numeros = [10, 20, 30]
print(get_item(numeros, 1))
print(get_item(numeros, 10))