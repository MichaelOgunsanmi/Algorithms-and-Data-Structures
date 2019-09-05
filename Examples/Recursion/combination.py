def NCR(nValue, rValue):
    if rValue == 0 or nValue == rValue:
        return 1 
    return NCR(nValue -1, rValue - 1) + NCR(nValue-1, rValue) 

print(NCR(2,0))