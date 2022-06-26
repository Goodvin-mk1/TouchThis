text = list(input("Enter text: "))
key = list(input("Enter key: "))
result_list = []
counter = 0
binary_counter = 0
for i in text:
    binary_char_text = bin(ord(i))[2:]
    binary_char_text = "0" * (8 - len(binary_char_text)) + binary_char_text
    print("(text)", i, " = ", binary_char_text)
    for j in key[counter]:
        binary_char_key = bin(ord(j))[2:]
        binary_char_key = "0" * (8 - len(binary_char_key)) + binary_char_key
        counter += 1
        print("(key)", j, " = ", binary_char_key)
        binary_counter = 0
        print("result = ", end='')
        for i_1 in binary_char_text:
            for j_1 in binary_char_key[binary_counter]:
                if int(i_1) != int(j_1):
                    result = 1
                else:
                    result = 0
                result_list.append(result)
                binary_counter += 1
                print(result, end='')
                break
        result_list.append(' ')
        print("\n")
print(result_list)
