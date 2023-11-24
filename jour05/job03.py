def afficher_triangle(height):
    for i in range(height):
        espaces_gauche = height - i - 1
        ligne = ' ' * espaces_gauche

        ligne += '/'
        if i == height - 1:
            ligne += '-' * (2 * i)
        else:
            ligne += ' ' * (2 * i)

        ligne += '\\'

        print(ligne)

afficher_triangle(5)