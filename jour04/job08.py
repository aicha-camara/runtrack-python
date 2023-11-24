L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
def paire(list):
     result = 0
     for nombre in list:
          if nombre % 2 == 0:
           result += nombre
     print(result)  
paire(L)          