# Give the user some context.
print("\nThis program stores passwords")

#global variable to store the password during the program run
data = {}


#this function reads the file data.txt which store the passwords 
#the file data is read into dictionary called data
def read_passworddb_file():
    with open("data.txt", "r") as file:
        for line in file:
            name, pwd, url = line.strip().split(":")
            data[name] = [pwd, url]
    

#ROT3 encryption
#the fuction take one parameter string
#function return the encpted word
def encrypt_pwd(pwd ):
    clearText = pwd
    #print(pwd)
    charSet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\\}]{[\"':;?/>.<, "
    encText = "".join([charSet[(charSet.find(c)+3)%94] for c in clearText])
    #print(encText)
    return(encText)

    
#ROT3 encryption
#the fuction take one parameter string
#function return the deencpted word
def dencrypt(encrptedpwd):
    clearText = encrptedpwd
    charSet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\\}]{[\"':;?/>.<, "
    dencText = "".join([charSet[(charSet.find(c)-3)%94] for c in clearText])
    #print(dencText)
    return(dencText)


#add new login to the data base
def set_new_entry_1():
    newname= input("Enter a new name: ").strip()
    newpassword= input("Enter a new password: ").strip()
    newURL= input("Enter a new URL: ").strip()
    data[newname] = [encrypt_pwd(newpassword), newURL]
    #print(data)


#display the password and url to a existing login
def display_apassword():
    disname = input("Enter the name you want to display the password for: ").strip()
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


#change the password for an existing login name
def change_pwd_url():
    name = input("Enter the name for which you want to change pwd and url :").strip()
    
    if name in data:
        pwd = input(f"the password for {name} : ").strip()
        url = input(f"the url for {name}").strip()
        data[name] = [encrypt_pwd(pwd), url]
    else:
        print("Login does not exist")

#write password file before quiting
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
    print("\n[1] Enter 1 to create an encryption password.")
    print("[2] Enter 2 to display password")
    print("[3] Enter 3 to change your password")
    print("[q] Enter q to quit.")
    
    # Ask for the user's choice.
    choice = input("\nMake your choice: ").strip()
    
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