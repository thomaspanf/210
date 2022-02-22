import sys

def encode(string):
    prev = ""
    count = 0
    firstLetter = True
    encoding = ""
    letterCount = 0
    for letter in string: #iterate letter by letter in string
        letterCount += 1 #letter count = 1
        if firstLetter: 
            firstLetter = False #if loop is at a firstletter, iterate count
            count+=1
        else:
            if prev == letter: #if prev is the same as letter, iterate count
                count+=1
            else:
                encoding += prev + str(count)  #append letter and count, reset count to 1
                count = 1
            
        prev = letter #set prev letter to current letter 
        if letterCount == len(string): #condition if string is all the same letter 
            encoding += prev + str(count)
    return encoding

def decode(s): 
    result = ""
    for letter in s: #iterate letter by letter in string
        if not letter.isdigit(): #letter.isdigit() false if not digit, true if digit 
            prev = letter
        else:
            result += prev*int(letter)
    return result


def decodeMultiDigit(s):
    decodedString = ""
    currentCharacter = ""
    currentCount = ""
    stringCount = 0
    length = len(s)
    for letter in s:
        stringCount+=1
        if letter.isdigit():
            currentCount += letter
        else:
            if len(currentCount) > 0:
                for i in range(int(currentCount)):
                    decodedString += currentCharacter
            currentCharacter = letter
            currentCount = ""
        if stringCount == length:
            if len(currentCount) > 0:
                decodedString += currentCharacter * int(currentCount)
    return decodedString


print(encode(sys.argv[1]))
print(decode(sys.argv[2]))
        