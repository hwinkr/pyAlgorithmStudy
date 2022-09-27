n = int(input())
km = list(map(int, input().split()))
price = list(map(int, input().split()))

price_sum = 0 # 최소 비용
low = 0 # 리터 당 가격이 가장 싼 주유소 위치를 나타내는 변수

for i in range(n-1): # 리터당 가격이 전보다 싼 주유소를 만나면 
    if price[low] > price[i]: # 더 싼 주유소를 만나기 전 거리까지만큼 기름을 주유하면 된다
        price[low] = price[i] 
        
    price_sum = price_sum + price[low] * km[i]
    
print(price_sum)
