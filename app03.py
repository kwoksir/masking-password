import msvcrt
username = input("login: ")
msg = "Enter password: "
for ch in msg:
    msvcrt.putwch(ch)
    
#print("Enter password: ", end='\n')
c = ''
pw = ''
while True:
    c = msvcrt.getwch()
    msvcrt.putwch('*')
    if c == '\r' or c == '\n':
        break
    pw += c
msvcrt.putwch('\r')
msvcrt.putwch('\n')
print(username, 'Password: ', pw)
