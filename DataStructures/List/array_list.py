def new_list():
    newlist = {'elementos': [], 'size': 0, }
    return newlist

def get_element(my_list, index):
    
    return my_list["elements"][index]


def is_present(my_list, element, cmp_function):
    
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def add_first(my_list, element):
    """
    Agrega un elemento al inicio de la lista.
    """
    my_list["elementos"].insert(0, element)
    my_list["size"] += 1


def add_last(my_list, element):
    """
    Agrega un elemento al final de la lista.
    """
    my_list["elementos"].append(element)
    my_list["size"] += 1


def size(my_list):
    """
    Retorna el tamaño de la lista.
    """
    return my_list["size"]

def first_element(my_list):
    """
    Retorna el primer elemento de la lista.
    Si la lista está vacía, retorna None.
    """
    if my_list["size"] == 0:
        return None
    return my_list["elementos"][0]

def is_empty(my_list):
    """Retorna True si la lista está vacía"""
    return my_list["size"] == 0

def size(my_list):
    """Retorna el tamaño de la lista"""
    return my_list["size"]

def last_element(my_list):
    """Retorna el último elemento"""
    if is_empty(my_list):
        return None
    return my_list["elementos"][-1]

def delete_element(my_list, pos):
    """Elimina un elemento en la posición dada"""
    if pos < 0 or pos >= my_list["size"]:
        return None
    elem = my_list["elementos"].pop(pos)
    my_list["size"] -= 1
    return elem

def remove_first(my_list):
    """Elimina y retorna el primer elemento"""
    if is_empty(my_list):
        return None
    elem = my_list["elementos"].pop(0)
    my_list["size"] -= 1
    return elem

def remove_last(my_list):
    """Elimina y retorna el último elemento"""
    if is_empty(my_list):
        return None
    elem = my_list["elementos"].pop()
    my_list["size"] -= 1
    return elem

def insert_element(my_list, element, pos):
    """Inserta un elemento en la posición dada"""
    if pos < 0 or pos > my_list["size"]:
        return None
    my_list["elementos"].insert(pos, element)
    my_list["size"] += 1
    return element

def change_info(my_list, pos, element):
    """Cambia el valor de un elemento en la posición dada"""
    if pos < 0 or pos >= my_list["size"]:
        return None
    my_list["elementos"][pos] = element
    return element

def exchange(my_list, pos1, pos2):
    """Intercambia dos elementos de posición"""
    if pos1 < 0 or pos1 >= my_list["size"] or pos2 < 0 or pos2 >= my_list["size"]:
        return None
    my_list["elementos"][pos1], my_list["elementos"][pos2] = my_list["elementos"][pos2], my_list["elementos"][pos1]
    return True

def sub_list(my_list, pos, num):
    """Retorna una sublista desde pos con num elementos"""
    if pos < 0 or pos >= my_list["size"]:
        return None
    sub = {"elementos": [], "size": 0}
    fin = min(pos + num, my_list["size"])
    sub["elementos"] = my_list["elementos"][pos:fin]
    sub["size"] = len(sub["elementos"])
    return sub
