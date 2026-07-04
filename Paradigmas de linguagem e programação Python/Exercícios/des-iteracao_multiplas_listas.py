valores1 = [2, 4, 6]
valores2 = [1, 2, 6, 8]

for v1 in valores1:
   for v2 in valores2:
      if v1 == v2:
        print(f'Valor {v1} aparece nas duas listas.')
      

elemento_em_comum = False

for v1 in valores1:
   if elemento_em_comum:
      break
   for v2 in valores2:
      if v1 == v2:
         elemento_em_comum = True
         break

if elemento_em_comum:
   print(f'As listas possuem valores em comum!')
else:
   print(f'As listas Não possuem valores em comum!')


         

