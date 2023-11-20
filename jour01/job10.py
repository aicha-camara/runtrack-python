montant = 10000
taux_en_pourcentage = 10
gain_annuel = montant* taux_en_pourcentage /100
taux_en_pourcentage= taux_en_pourcentage + 2
print("gain_annuel" , gain_annuel)

capital = 5000
montant = montant+ capital
gain_annuel = montant * taux_en_pourcentage /100
print("Nouveau_gain_annuel" , gain_annuel)
montant = montant * 0.1
taux_en_pourcentage = taux_en_pourcentage - 1

gain_annuel = montant* taux_en_pourcentage /100
print("Nouveau_gain_annuel" , gain_annuel)
