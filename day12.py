def prime_num_check(num):
    if num == 1:
        return False
    if num == 2:
        return True
    
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True
        
for i in range(1, 100+1):
    print(i, prime_num_check(i))