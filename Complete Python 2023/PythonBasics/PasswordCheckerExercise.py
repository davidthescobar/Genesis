user_name = input('username ')
user_password = input('password ')
password_encrypt = '*' * len(user_password)

print(f'{user_name}, your password {password_encrypt} is {len(user_password)} letters long.')