def TOH(numOfDisks, pole1, pole2, pole3):   
    if numOfDisks > 0:        
        TOH(numOfDisks - 1, pole1, pole3, pole2)       
        print((pole1, pole3))
        TOH(numOfDisks - 1, pole2, pole1, pole3)

TOH(4,1,2,3) 

