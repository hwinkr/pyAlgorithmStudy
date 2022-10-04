# x값이 최소가 되는  n - 3x == (5의 배수) or 0  일때 설탕을 최소한으로 배달할 수 있다

n = input()

if n == '4' or n == '7': 
    print(-1)
    
else:
    n_list = list(map(int, str(n))) # 끝자리 수를 보면서 최소한 3을 뺴는 방식으로 구했다
                                    # 다만 4와 7은 최소한의 3으로 빼는데 한계가 있어 구하지 못한다
    if n_list[-1] == 0 or n_list[-1] == 5:
        count = int(n) // 5
        
    elif n_list[-1] == 3 or n_list[-1] == 8:
        count = (int(n)-3) // 5 + 1
        
    elif n_list[-1] == 1 or n_list[-1] == 6:
        count = (int(n)-6) // 5 + 2 
         
    elif n_list[-1] == 4 or n_list[-1] == 9:
        count = (int(n)-9) // 5 + 3  
          
    elif n_list[-1] == 2 or n_list[-1] == 7:
        count = (int(n)-12) // 5 + 4   
        
    print(count)