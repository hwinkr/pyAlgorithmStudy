count = 1

while 1:
  result = 0
  L, P, V = map(int, input().split())
  
  if L + P + V == 0:
    break
  else:
        if V % P > L:
            result = ((V // P) * L) + L
        else:
            result = ((V // P) * L) + (V % P)
  print("Case {}: {}".format(count, result))
  count = count + 1