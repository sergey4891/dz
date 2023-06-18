import json

# data_user = {'user1: '123', 'user2': 234}
# with open('user.json', 'w') as f:
#     json.dump(data_pizza, f)

sicret_info = "Вы вошли в систему"
def register(login, passwd):
    with open('user.json', 'r') as f:
        data_user = json.load(f)
    if login not in data_user.keys():
        data_user[login] = passwd
        with open('user.json', 'w') as f:
            json.dump(data_user, f)
    else:
        print('Пользователь существует')

def login_finction(login, passwd):
    with open('user.json', 'r') as f:
        data_user = json.load(f)
    # login = input('Введите логин: ')
    # passwd = input('Введите пароль: ')
    if login in data_user.keys():
        data_user[login] == passwd
        print(sicret_info)
    else:
      print("Неверный логин или пароль")

# login_finction(input('Введите логин: '), input('Введите пароль: '))

# q1 = input("Вход или регистрация(вход или рег)")
# if q1 == 'вход':
#     log = input('Введите логин: ')
#     passwd = input('Введите пароль: ')
#     if login in data_user.keys()
#         data_user[login] == passwd:
# #             print("Успешный")
#     else:
#     print("Неверный логин или пароль")



q1 = input("Вход или регистрация(вход или рег): ")
if q1 == 'вход':
    login_finction(input('Введите логин: '), input('Введите пароль: '))
elif q1 == 'рег':
    register(input('Придумайте логин: '), input('Придумайте пароль: '))

else:
    print("Вы ошиблись c выбором")


