L = [8, 0, 5, 20, 22, 15, 9]

def tri(list):
    x = len(list)
    for i in range(x):
        for j in range(0, x-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

tri(L)
print(L)
