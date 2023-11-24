def length(list):
    count=0
    for i in list:
        count+=1
    return count
def tri(list):
    len=length(list)
    for i  in range (len-1):
        for j in range (i+1 ,len):
            if list[i]>list[j]:
                l=list[i]
                list[i]=list[j]
                list[j]=l
    return list
def round_number(number):
    integer=int(number)   
    decimal=number-integer  

    if decimal >= 0.5:
        number = integer + 1 
    else: 
        number=integer
     
    return number
def round_list(list):
    for i in range(length(list)) :
        list[i]= round_number(list[i])
    
    return list 
L=[22.4, 4.0, 16.22, 9.10, 11.00,12.22, 14.20, 5.20, 17.50]

print(L)

liste_arrondi=(round_list(L))
print(liste_arrondi)
print(tri(liste_arrondi))
