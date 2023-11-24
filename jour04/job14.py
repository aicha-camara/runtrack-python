def length(list):
    count=0
    for i in list:
        count+=1
    return count

def my_long_word(n , String): 
    word=""  
    new_String="" 

    for char in String :
   
        if (char != " ") and (char != ","):
            word += char
         
        else:
            if length(word) > n :
                new_String += word
                new_String+=' '
                word=""
            
            else:
                word=""
            
    return new_String
        



word="La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à"
print(word)

print(my_long_word(3,word))


