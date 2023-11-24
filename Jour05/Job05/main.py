print ("Veuillez entrer un message:")
message= input()
print ("Combien de decalage ?")
n= int(input())

def decalage(message, n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cesar = ""

    for i in message:
        if i in alphabet:
            original = alphabet.index(i)
            code = (original + n) % 26
            cesar += alphabet[code]
        else:
            cesar += i

    print(cesar)

decalage(message, n)