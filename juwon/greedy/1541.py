# x = input()
# x = '(' + x + ')'

# i = 0
# while i < len(x):

#     if x[i] == '-':
#         x = x[:i] + ')' + x[i:i+1] + '(' + x[i+1:]
#         i = i + 2
         
#     i = i + 1
    
# result = eval(x)

# print(result)

#todo  처음에는 위의 방법으로 했지만 실패했다
#todo  0으로 시작하는 수를 eval함수가 계산하지 못해서 그렇다
#todo  아래는 다시 푼 코드



x = input().split('-') #* -를 기준으로 나눈다음
# print(x)  -  ['55', '50+40']

li = list()

for i in x: #* +부분을 다 더한다
    # print(i)  -  50+40 
    a = list(map(int, i.split('+')))
    #print(a)  -  [50, 40]
    plus_sum = sum(a)
    #print(plus_sum)  -  90
    li.append(plus_sum)
    
#print(li)  -  [55, 90]

result = li[0] #* 리스트 안에 처음 값만 +고 나머지는 -이므로

for j in range(1,len(li)): #* li[0]에서 나머지 리스트값을 전부 빼면 된다
    result = result - li[j]
    
print(result)
