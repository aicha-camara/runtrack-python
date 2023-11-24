L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
def produit(list):
     result = 1
     for nombre in list:
          if 25 < nombre <90:
            result *= nombre
     print(result)          
               
produit(L)       
    