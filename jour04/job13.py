
def length(list):
    count=0
    for i in list:
        count+=1
    return count

def add_list(list, e):
    new_list = list[:] + [e]
    return new_list

def delete_double(list):
    len=length(list)
    new_list=[]

    for i  in range (len-1):
        for j in range (i+1 ,len):
         
            if list[i] == list[j]:
                list[j]= None

    for i in range(len):
        if list[i] != None:
            new_list=add_list(new_list,list[i]) 
    return new_list     
  
L = [ 1 , 2 , 4 ,8 , 4 ,9 ,0 , 2]
print(L)
print(delete_double(L))
