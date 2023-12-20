LOWER_ASCII = 97
UPPER_ASCII = 65
ALPHABET_SIZE = 26

def modular_inverse(a, n):
    t = 0
    r = n
    newt = 1
    newr = a
    
    while newr != 0:
        q = r // newr
        t, newt = newt, (t - q * newt)
        r, newr = newr, (r - q * newr)
        
    if r > 1:
        return -1 #not invertibe
    if t < 0:
        t = t + n
    return t

class AffineCipher:
    
    def __init__(self, a, b, plaintext = "", ciphertext = ""):
        self.plaintext = plaintext
        self.a = a
        self.b = b
        self.ciphertext = ciphertext
        
    def encrypt(self):
        for i in self.plaintext:
            if i.isspace():
                self.ciphertext += " "
            elif i.islower():
                self.ciphertext += chr((self.a * (ord(i) - LOWER_ASCII) + self.b) % ALPHABET_SIZE + LOWER_ASCII)
            else:
                self.ciphertext += chr((self.a * (ord(i) - UPPER_ASCII) + self.b) % ALPHABET_SIZE + UPPER_ASCII)
                
    def decrypt(self):
        self.plaintext = ""
        a_inverse = modular_inverse(self.a, ALPHABET_SIZE)
        for i in self.ciphertext:
            if i.isspace():
                self.plaintext += " "
            elif i.islower():
                self.plaintext += chr((a_inverse * ((ord(i) - LOWER_ASCII) - self.b)) % ALPHABET_SIZE + LOWER_ASCII)
            else:
                self.plaintext += chr((a_inverse * ((ord(i) - UPPER_ASCII) - self.b)) % ALPHABET_SIZE + UPPER_ASCII)
            
                
def main():
    test = AffineCipher(3, 7, "Sutirtha")
    test.encrypt()
    test.decrypt()
    print(test.ciphertext)
    print(test.plaintext)
    
main()
