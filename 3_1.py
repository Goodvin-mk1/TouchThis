# Первый способ
print("Enter your text: ")
entered_text = input()
print(entered_text.replace(' ', '-'))

# Второй способ
print("Enter your text: ")
entered_text = input()
entered_text = entered_text.split(' ')
print('-'.join(entered_text))
