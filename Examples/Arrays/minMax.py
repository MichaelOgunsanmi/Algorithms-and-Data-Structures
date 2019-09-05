def minMax(arrayInput):
    minValue = float('inf')
    maxValue = float('-inf')

    for element in arrayInput:
        if element > maxValue:
            maxValue = element  
        if element < minValue:
             minValue = element  
    
    print(maxValue, minValue) 

minMax([5,8,3,9,6,2,10,7,-1,4])

