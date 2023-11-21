def nombre_premier(number):
    for i in range(2 , number):
        if number % i == 0:
            return False
        return True
for x in range(1, 1000):
    if nombre_premier(x):
        print(x)   
