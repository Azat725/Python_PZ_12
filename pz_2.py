user_str = input("Введите строку >> ")
digit_count = 0
letter_count = 0

for i in user_str:
    if i.isdigit():
        digit_count += 1
    elif i.isalpha():
        letter_count += 1
        
print(f"Количество цифр в вашем преложении: {digit_count}")
print(f"Количество букв в вашем предложении: {letter_count}")