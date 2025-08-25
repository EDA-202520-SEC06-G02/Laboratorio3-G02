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
