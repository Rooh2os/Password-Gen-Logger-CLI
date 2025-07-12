import basic,random,string
print("WARNING: This program saves passwords for your use. The passwords are stored in plain text. USE WITH CAUTION")

input = None
while input == None:
    try:
        input = int(input(""))
    except(ValueError,IndexError):
            basic.clear
            print("Oops, thats not a valid choice. Try again.\n")

if input == 1:
    pw = ""
    chrs = string.ascii_letters + string.digits + string.punctuation
    while len(pw) != int(input("lenth of password")):
        pw += random.choice(chrs)
    print(pw)