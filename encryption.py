def main():
    print()
    print("Choose one option")
    choice = int(input("1.Encryption \n 2.Decryption \n Choose 1 or 2:- 1"))
    if(choice==1):
        encryption()
    
    elif(choice==2):
        decryption()

    else:
        print("wrong choice")

def encryption():
    print("Encryption")
    msg = input("Enter your message:- ")
    key = int(input("Enter Key-1 to 94:- "))
    encrypted_text = ""

    for i in range (len(msg)):
        temp = (ord(msg[i])+key)
        if temp>126:
            temp = temp-127+32 
        encrypted_text+=chr(temp)

    print("Encrypted message is -"+encrypted_text)
    main()

 


def decryption():
    print("Decryption")
    print("Message can only be lower or upper case alphabet")
    encrypted_msg = input("Enter Encryted Message")
    decryption_key = int(input("Enter Key-1 to 94"))
    decrypted_text = ""

    for i in range(len(encrypted_msg)):
        temp = (ord(encrypted_msg[i])-decryption_key)
        if temp<32:
            temp= temp+127-32
        decrypted_text+=chr(temp)

    print("Decrypted message is -"+decrypted_text)

if __name__=="__main__":
    main()