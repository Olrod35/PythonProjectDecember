additional_str = input('Введите что-нибудь:')
existing_str = "Это строка, в которую {} новую строку".format(additional_str)
new_add = 'замена в строке'
new_str = f"Это строка, в которую {new_add} новую строку"
print(existing_str)
print(new_str)
print(len(new_str))
