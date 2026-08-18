from itertools import cycle

def encryptDecrypt(inpString):
    xorKey = 'P'
    for i in range(len(inpString)):
        inpString = (inpString[:i] +
                     chr(ord(inpString[i]) ^ ord(xorKey)) +
                     inpString[i + 1:])
        print(inpString[i], end="")

    return inpString


if __name__ == '__main__':
    sampleString = "GeeksforGeeks"

    print("Encrypted String: ", end="")
    sampleString = encryptDecrypt(sampleString)
    print("\n")

    print("Decrypted String: ", end="")
    encryptDecrypt(sampleString)
