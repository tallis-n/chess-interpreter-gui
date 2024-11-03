str1 = ""
for i in range(0,64):
    str1 += " "
    str1 += str(i)
    if (i + 1) < 10:
        str1 += " "
    if (i + 1) % 8 == 0:
        str1 += "\n"
letter_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
str1 += "\n"
j = 8
for i in range(0, 64):
    str1 += " "
    str1 += letter_list[i % 8]
    str1 += str(j)
    if (i + 1) % 8 == 0:
        j -= 1
        str1 += "\n"
print(str1)
