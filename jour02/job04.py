
while True:
    y = int(input("Saisir un entier supérieur a 0 : "))
    if y > 0:
        break
for i in range(1, 11):
    print( "Table de multiplication de" , y , ":")
    print(i, "x", y, "=", i * y)