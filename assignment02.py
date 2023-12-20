'''
this is an encryption algorithm and it takes input as encrypt('text',[17,20])
write a decryption algorithm. Use Extended Euclidean Algorithm
 for finding modular inverse. So you have to keep in mind wheather 
 modular inverse exists or not.
'''

    
def encrypt(text, key):
    
    #C = (a*P + b) % 26
    
    return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26)
                  + ord('A')) for t in text.upper().replace(' ', '') ])

