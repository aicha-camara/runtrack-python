nom = "crayon"
prix_unitaire = 50
quantité_en_stock = 100
print("Nom du produit :", nom)
print("Prix unitaire :", prix_unitaire)
print("Quantité en stock :", quantité_en_stock)


achat = int(input("saisir la quantité de produits que vous souhaitez acheter: "))
quantité_en_stock -= achat 


print( "Nom=" , nom , "Prix_unitaire=" , prix_unitaire , "Quantité_en_stock=" , quantité_en_stock )
prix_unitaire *= 1.10  

print("Nom du produit :" , nom)
print("Prix unitaire (après inflation) :", f"{prix_unitaire :.2f}")
print("Nouvelle quantité en stock :", quantité_en_stock)
