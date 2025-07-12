import random,string

pw = ""
chrs = string.ascii_letters + string.digits + string.punctuation
while len(pw) != int(input("lenth of password")):
    pw += random.choice(chrs)
print(pw)