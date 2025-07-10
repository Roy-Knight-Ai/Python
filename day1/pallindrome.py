def pallindrome(a):
    if str(a) == str(a)[::-1]:
        print("Pallindrome")
    else:
        print("Not Pallindrome")
pallindrome(121)
pallindrome("15264")