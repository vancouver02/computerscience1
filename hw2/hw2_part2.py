
# this function converts english to encrpytion using .replace()
def encrypt(word):
    word = word.replace('a', 'rxr')
    word = word.replace('he', 'vw')
    word = word.replace('e', 'az az')
    word = word.replace('y', 'eie')
    word = word.replace('u', 'yyy')
    word = word.replace('an', 'uq')
    word = word.replace('th', 'aige')
    word = word.replace('o', 'tzzt')
    return word

# this function convert encryption to regular english using .replace()
def decrypt(word):
    word = word.replace('tzzt', 'o')
    word = word.replace('aige', 'th')
    word = word.replace('uq', 'an')
    word = word.replace('yyy', 'u')
    word = word.replace('eie', 'y')
    word = word.replace('az az', 'e')
    word = word.replace('vw', 'he')
    word = word.replace('rxr', ' a')
    return word


cipher_text = input("Enter cipher text ==> ")
plain_text = decrypt(cipher_text) # this variable calls the decrypt function 

print("Deciphered as ==> " + plain_text)
print("Difference in length ==> " + str(abs(len(cipher_text) - len(plain_text))))

plain_text = input("Enter regular text ==> ")
cipher_text = encrypt(plain_text)

print("Encrypted as ==> " + cipher_text)
print("Difference in length ==> " + str(abs(len(cipher_text) - len(plain_text))))



