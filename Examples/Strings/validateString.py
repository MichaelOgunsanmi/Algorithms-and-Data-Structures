def validateString(stringInput):
    for element in stringInput:
        if 65 <= ord(element) <= 96 or 97 <= ord(element) <= 122 or 48 <= ord(element) <= 57:
            continue  
        else:
            return False  
    return True  


print(validateString('How4are3you2doing'))
print(validateString('How are you doing?'))

#Using built in function
print('How4are3you2doing'.isalnum())
