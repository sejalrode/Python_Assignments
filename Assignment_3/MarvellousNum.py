def ChkPrime(values):
    for i in range(2,values):
        if(values % i == 0):
            return False
    return True