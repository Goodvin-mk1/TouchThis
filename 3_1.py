# Замена ' ' на '-'

print("Enter your text: ")

# Первый способ
entered_text = input()
print(entered_text.replace(' ', '-'))

# Второй способ
entered_text = entered_text.split(' ')
print('-'.join(entered_text))
