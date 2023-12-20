import math

def encode(text, key):
    ct = ""
    k_in = 0
    msg_len = len(text)
    msg_lst = list(text)
    key_lst = sorted(list(key))

    col = len(key)
    row = math.ceil(msg_len / col)

    fill_null = int((row * col) - msg_len)
    msg_lst.extend("#" * fill_null)

    mat = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)]

    for _ in range(col):
        curr_ind = key.index(key_lst[k_in])
        ct += "".join([row[curr_ind] for row in mat])
        k_in += 1

    return ct

def main():
    txt = input("Enter the text--> ")
    key = input("Enter the key as text--> ")
    en = encode(txt, key)
    print("Encrypted text--> ", en)

main()