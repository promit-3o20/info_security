'''
this is an encryption algorithm; please try to understand how it works and
modify it thus it works for integers as well.
'''

def encrypt(text, shift):
    result = ""
    
    # traverse text
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr(((ord(char)) + shift - 65) % 26 + 65)
            
        # Encrypt lowercase characters
        else:result += chr(((ord(char)) + shift - 97) % 26 + 97)
    return result