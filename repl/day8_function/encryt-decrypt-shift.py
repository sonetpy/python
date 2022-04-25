
#global shift
def encrypt(direction, text, shift):
    if direction == 'encrypt':
        for i in text:
            #shift_char = chr(ord(i) + shift)
            print(chr(ord(i) + shift), end='')

def decrypt(direction, text, shift):
    if direction == 'decrypt':
        for i in text:
            print(chr(ord(i) - shift), end='')

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("Type your Message:\n").lower()
shift = int(input("type the shift number:\n"))
shift_char = []
original_char = []
encrypt(direction, text, shift)
print ("\nYour decrypted message is : ")
decrypt(direction, text, shift)





"""
direction = input("\nDo you want to decrypt yes or no: ")
if direction == 'yes':
    for d in shift_char:
        #print(chr(ord(decrypt) - shift))
        original_char = chr(ord(d) - shift)
        print(original_char, end='')

else:
    print("You entered something else neither it encrypt or decrypt option that you entered")
    print("Good Bye")
"""