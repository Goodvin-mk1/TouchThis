# Отформатированное приветственное сообщение
print("Enter your name, age and city: ")
name = input("Name: ").capitalize()
age = input("Age: ")
city = input("City: ").capitalize()
print(f"Hi everyone. My name is {name}. I'm {age} years old. And i'm live in {city} city.\n")
print("Hi everyone. My name is {}. I'm {} years old. And i'm live in {} city.".format(name, age, city))
