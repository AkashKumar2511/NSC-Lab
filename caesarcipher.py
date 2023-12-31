#Caeser Cipher Algorithm
#Scope of chars : Aplhanumerics
 
def encrypt(plain_text):
    cipher_text = ""
    shifts = int(input("Enter the key/shifts : ")) % 26
    for char in plain_text:
        char_ascii = ord(char)
        if(char_ascii >= 65 and char_ascii <= 90):
            cipher_text += chr((((char_ascii - 65) + shifts) % 26) + 65)
        elif(char_ascii >= 97 and char_ascii <= 122):
            cipher_text += chr((((char_ascii - 97) + shifts) % 26) + 97)
        elif(char_ascii >= 48 and char_ascii <= 57):
            cipher_text += chr((((char_ascii - 48) + shifts) % 26) + 48)
        else:
            cipher_text += char
    print("Encrypted text :", cipher_text)
    
def decrypt(cipher_text):
    plain_text = ""
    shifts = int(input("Enter the key/shifts : "))
    for char in cipher_text:
        char_ascii = ord(char)
        if(char_ascii >= 65 and char_ascii <= 90):
            plain_text += chr((((char_ascii - 65) - shifts) % 26) + 65)
        elif(char_ascii >= 97 and char_ascii <= 122):
            plain_text += chr((((char_ascii - 97) - shifts) % 26) + 97)
        elif(char_ascii >= 48 and char_ascii <= 57):
            plain_text += chr((((char_ascii - 48) - shifts) % 26) + 48)
        else:
            plain_text += char
    print("Decrypted text :", plain_text)
 
if __name__ == "__main__" :
    text = input("Enter text : ")
    flag = int(input("Enter 1 for encryption and 0 for decryption : "))
    if(not flag):
        decrypt(text)
    elif(flag == 1):
        encrypt(text)
    else:
        print("Invalid input")