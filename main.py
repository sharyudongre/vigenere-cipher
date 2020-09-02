alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_to_index=dict(zip(alphabet, range(1,len(alphabet))))
index_to_letter=dict(zip(range(1,len(alphabet)),alphabet))

def encrypt(text,key):
    encrypted_text=""
    split_message=[text[i:i+len(key)] for i in range(0,len(text),len(key))]

    for j in split_message:
        i=0
        for l in j:
            number=(letter_to_index[l]+letter_to_index[key[i]]) % 26
            encrypted_text+=index_to_letter[number]
            i=i+1
    return encrypted_text


def decrypt(text,key):
    decrypted_text=""
    split_message = [text[i:i + len(key)] for i in range(0, len(text), len(key))]

    for j in split_message:
        i = 0
        for l in j:
            number = (letter_to_index[l] - letter_to_index[key[i]]) % 26
            decrypted_text+=index_to_letter[number]
            i = i + 1
    return decrypted_text

def main():
    while(1):
        choice=input("ENTER A OPTION:\nPress 1 for encryption \nPress 2 for decryption \nPress 3 to exit\n")
        if int(choice)==1:
            message = input("Enter your message\n")
            key = input("Enter the key\n")
            ans=encrypt(message,key)
            print("Encrypted message is : ",ans)
        elif int(choice)==2:
            message = input("Enter your message\n")
            key = input("Enter the key\n")
            ans=decrypt(message,key)
            print("Decrypted message is : ",ans)
        elif int(choice)==3:
            break
        else:
            print("Choose a proper option")

main()
