def plante(type, saison):
    if type == "fruits" and saison == "hiver":
        return print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "ete":
        return print("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        return print("carotte, topinambour, endive")
    elif type == "legume" and saison == "ete":
        return print("artichaut, aubergine,navet")
plante("fruits", "ete")    
