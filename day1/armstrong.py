def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == n
print(is_armstrong(256)) 
print(is_armstrong(153)) 