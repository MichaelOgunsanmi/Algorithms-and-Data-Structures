def countVowelWord(stringInput):
    vowelCount = 0
    wordCount = len(stringInput.split())

    for element in stringInput:
        if element == 'a' or element == 'e' or element == 'i' or element == 'o' or element == 'u':
            vowelCount += 1 
    
    print('There are {words} words and {vowels} vowels'.format(words = wordCount, vowels = vowelCount))

countVowelWord('How are you doing?')

