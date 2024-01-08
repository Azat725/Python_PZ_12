user_str = input("Введите строку: ")
user_word = input("Введите слово которое вы хотите заменить: ")
user_word_change = input("Введите слово для замены: ")

new_user_str = user_str.replace(user_word, user_word_change)

print(new_user_str)