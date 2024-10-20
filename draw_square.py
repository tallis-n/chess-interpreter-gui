str1 = ""
for i in range(0,64):
    str1 += " "
    str1 += str(i)
    if (i + 1) < 10:
        str1 += " "
    if (i + 1) % 8 == 0:
        str1 += "\n"
print(str1)
