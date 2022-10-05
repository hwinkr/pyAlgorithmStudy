sugar = int(input())
bag = 0

while sugar >= 0:
  if sugar % 5 == 0:
    bag = bag + sugar // 5
    print(bag)
    break
  
  sugar = sugar - 3
  bag = bag + 1
  
else:
  print(-1)