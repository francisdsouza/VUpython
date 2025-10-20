# Give the user some context.
print("\nThis program stores passwords")

#global variable to store the password during the program run
data = {}


def read_passworddb_file():
    with open("data.txt", "r") as file:
        for line in file:
            name, pwd, url = line.strip().split(":")
            data[name] = [pwd, url]

#ROT3 encryption
def encrypt_pwd(pwd):
    clearText = pwd
    print(pwd)
    charSet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\\}]{[\"':;?/>.<, "
    encText = "".join([charSet[(charSet.find(c)+3)%94] for c in clearText])
    #print(encText)
    return(encText)

def dencrypt(encrptedpwd):
    clearText = encrptedpwd
    charSet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\\}]{[\"':;?/>.<, "
    dencText = "".join([charSet[(charSet.find(c)-3)%94] for c in clearText])
    #print(dencText)
    return(dencText)
            
def set_new_entry_1():
    newname= input("Enter a new name: ")
    newpassword= input("Enter a new password: ")
    newURL= input("Enter a new URL: ")
    data[newname] = [encrypt_pwd(newpassword), newURL]
    #print(data)

def display_apassword():
    disname = input("Enter the name you want to display the password for: ")
    if disname in data:
        ar=data[disname]
        #print(ar)
        pwd = dencrypt(ar[0])
        url = data[disname][1]
        #print(f"login name : {disname}")
        print(f"\npassword------ : {pwd}")
        print(f"URL----------- : {url}")
    else:
        print("\nUsername does not exist in the database\n")

def change_pwd_url():
    name = input("Enter the name for which you want to change pwd and url :")
    
    if name in data:
        pwd = input(f"the password for {name} : ")
        url = input(f"the url for {name}")
        data[name] = [encrypt_pwd(pwd), url]
    else:
        print("Login does not exist")

def write_password_file():
    with open("data.txt", "w") as file:
        for key, value in data.items():
            mypwd = value[0]
            myurl = value[1]
            file.write(f"{key}:{mypwd}:{myurl}\n")

################################################################################################
#main##main##main##main##main##main##main##main##main##main##main##main##main##main##main##main#

# Set an initial value for choice other than the value for 'quit'.
choice = ''

read_passworddb_file()

# Start a loop that runs until the user enters the value for 'quit'.
while choice != 'q':
    # Give all the choices in a series of print statements.
    print("\n[1] Enter 1 to create an encryption key.")
    print("[2] Enter 2 to display password")
    print("[3] Enter 3 to change your password")
    print("[q] Enter q to quit.")
    
    # Ask for the user's choice.
    choice = input("\nMake your choice: ")
    
    # Respond to the user's choice.
    if choice == '1':
        print("\nEnter a name for the encryption key\n")
        set_new_entry_1()
    elif choice == '2':
        print("\nDisplay your password.\n")
        display_apassword()
    elif choice == '3':
        print("\nChange your password\n")
        change_pwd_url()
    elif choice == 'q':
        print("\nExiting the menu\n")
        write_password_file()
    else:
        print("\nInvalid option, please try again.\n")
        
# Print a message that we are all finished.
print("Program exited.-------------------\n\n")