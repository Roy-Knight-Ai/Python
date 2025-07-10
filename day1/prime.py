def is_prime(n):
    if n == 1:
        print ("not prime not composite")
        return
    if n == 2:
        print("prime")
        return 
    if n % 2 == 0:
        print ("not prime")
        return
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            print ("not prime")
            return
    print ("prime")
is_prime(25)
is_prime(29)