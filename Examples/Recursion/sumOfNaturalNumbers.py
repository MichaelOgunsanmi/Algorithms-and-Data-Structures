def naturalNumbersSum(number):
    if number == 1:
        return 1 
    
    return naturalNumbersSum(number - 1) + number

print(naturalNumbersSum(99))
