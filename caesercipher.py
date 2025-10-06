alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']

def encry(txt,shift):
    cipher_txt=""
    for i in txt:
        if i in alphabet:
            index=alphabet.index(i)  
            new_index=index+shift
            if new_index>26:
             new_index-=26 
            cipher_txt+=alphabet[new_index]
        else:
           cipher_txt+=i    
    print(cipher_txt)
def decry(txt,shift):
    cipher_txt=""
    for i in txt:
      if i in txt:
        index=alphabet.index(i)  
        new_index=index-shift
        if new_index <= 0:
         new_index+=26
        cipher_txt+=alphabet[new_index] 
      else: 
        cipher_txt+=i   
    print(cipher_txt)
end = False    
while not end:     
    wht_todo=input("type encrypt for encryption, type decrypt for decryption: ").lower()
    msg=input("type your message: ").lower()
    num=int(input("type the shift number:"))
    if wht_todo=="encrypt":
        encry(txt=msg,shift=num)
    elif wht_todo=="decrypt":
        decry(txt=msg,shift=num)
    again=input("continue y/no:")
    if again =="no":
       end= True
       print("bye-bye")