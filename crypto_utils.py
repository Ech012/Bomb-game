from itertools import cycle

def encryptDecrypt(inpString):
    xorKey = 'P'
    for i in range(len(inpString)):
        inpString = (inpString[:i] +
                     chr(ord(inpString[i]) ^ ord(xorKey)) +
                     inpString[i + 1:])

    return inpString






