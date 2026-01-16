def is_prime(n:int):

    if n<=1:
        return False
    else:
        prime=True
        for i in range(2,n):
                if n%i==0:
                     prime=False
                     break
        return prime
    
print(is_prime(34))
                 
