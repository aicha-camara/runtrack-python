def moyenne(num1, num2, num3):
    moyenne = (num1+num2+num3)/3
    return moyenne

x = float(input("Saisir la premiere note:"))
y = float(input("Saisir la deuxieme note:"))
z = float(input("Saisir la troisieme note:"))

moyenne_etudiant = moyenne(x,y,z)
if moyenne_etudiant < 8:
    print("l'eleve a eu =", moyenne_etudiant, "/20 : l'Élève devrait faire des efforts")
elif moyenne_etudiant < 10:
    print("l'eleve a eu =",moyenne_etudiant, "/20 : l'Élève moyen")
elif moyenne_etudiant < 14:
    print("l'eleve a eu =",moyenne_etudiant ,"/20 : Bon élève")
elif moyenne_etudiant < 20:
    print("l'eleve a eu =",moyenne_etudiant ,"/20 : Très bon élève")


