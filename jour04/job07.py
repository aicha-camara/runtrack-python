L = [8, 24,48,2,16]

def multiple(list):
   count = 0
   for nombre in list:
      if nombre % 3 == 0:
         count += 1
   print(count)     
multiple(L)   