# crack me
table = [0x0C, 0x0A, 0x13, 0x09, 0x0C, 0x0B, 0x0A, 0x08]
code, k = 0, 0
username = input("Please input the username:\n")
for i in range(3, len(username)):
    if k > 7:
        k = 0
    code += ord(username[i]) * table[k]
    k += 1
print("The code is:\n" + str(code))
