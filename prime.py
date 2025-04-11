import math
def prime(n):
    if not isinstance(n,int):
        return "Enter a whole number"
    elif n ==0 or n==1:
        return "Enter a bigger number"
    elif n <0:
        return "enter whole numbers"
    
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n % i ==0:
                return f"the given number {n} is not a prime number"
                break
        else:
            return f"the given number is a prime number"
n = 31
result = prime(n)
print(result)