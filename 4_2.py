text = input('Write something: ')
letter_counter = {i: text.count(i) for i in text}
print(letter_counter)
