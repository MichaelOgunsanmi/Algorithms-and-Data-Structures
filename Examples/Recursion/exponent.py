def exponent(base, power):
    if power == 0:
        return 1

    if power % 2 == 0:
        return exponent(base * base, power/2) 
    else:
        return exponent(base * base, (power -1)/2) * base

print(exponent(2, 5))