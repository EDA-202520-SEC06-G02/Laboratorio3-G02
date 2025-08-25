def new_list():
    newlist = {"first": None, "last": None, "size": 0, }
    return newlist

def get_element(my_list, pos):
    searchpos = 0 
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1 
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0 
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
            
    if not is_in_array:
        count = -1
    return count

def add_first(my_list, element):
    """
    Agrega un elemento al inicio de la lista enlazada.
    """
    new_node = {"info": element, "next": None}
    if my_list["size"] == 0:
        my_list["first"] = new_node
        my_list["last"] = new_node
    else:
        new_node["next"] = my_list["first"]
        my_list["first"] = new_node
    my_list["size"] += 1


def add_last(my_list, element):
    """
    Agrega un elemento al final de la lista enlazada.
    """
    new_node = {"info": element, "next": None}
    if my_list["size"] == 0:
        my_list["first"] = new_node
        my_list["last"] = new_node
    else:
        my_list["last"]["next"] = new_node
        my_list["last"] = new_node
    my_list["size"] += 1


def size(my_list):
    """
    Retorna el número de elementos de la lista.
    """
    return my_list["size"]


def first_element(my_list):
    """
    Retorna el primer elemento de la lista.
    Si la lista está vacía, retorna None.
    """
    if my_list["size"] == 0:
        return None
    return my_list["first"]["info"]

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
    return my_list["last"]["info"]

def delete_element(my_list, pos):
    """Elimina el elemento en la posición dada"""
    if pos < 0 or pos >= my_list["size"]:
        return None

    if pos == 0:  # eliminar el primero
        return remove_first(my_list)

    prev = my_list["first"]
    for _ in range(pos - 1):
        prev = prev["next"]

    elem = prev["next"]["info"]
    prev["next"] = prev["next"]["next"]

    if pos == my_list["size"] - 1:  # si fue el último
        my_list["last"] = prev

    my_list["size"] -= 1
    return elem

def remove_first(my_list):
    """Elimina y retorna el primer elemento"""
    if is_empty(my_list):
        return None
    elem = my_list["first"]["info"]
    my_list["first"] = my_list["first"]["next"]
    if my_list["size"] == 1:
        my_list["last"] = None
    my_list["size"] -= 1
    return elem

def remove_last(my_list):
    """Elimina y retorna el último elemento"""
    if is_empty(my_list):
        return None

    if my_list["size"] == 1:
        elem = my_list["first"]["info"]
        my_list["first"] = None
        my_list["last"] = None
        my_list["size"] = 0
        return elem

    prev = my_list["first"]
    while prev["next"] != my_list["last"]:
        prev = prev["next"]

    elem = my_list["last"]["info"]
    prev["next"] = None


