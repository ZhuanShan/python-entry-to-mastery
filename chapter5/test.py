# 5-8

users = ['admin', 'user1', 'user2', 'user3']

try_login_user = '  user1'
login_user = try_login_user.strip()    # .strip()删除前后空格
print(login_user)

if login_user in users:
    if login_user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {login_user}, thank you for logging in again.")  #f 字符串格式化
elif login_user:
    print("Sorry, your acount was not sign in.")
else:
    print("We need to find some users!")

# 5-10

current_users = ['admin', 'user1', 'user2', 'user3']
new_users = ['neW1', 'new2', 'new3', 'new4', 'User3']
new_low_users = []
for new_user in new_users:
    new_low_users.append(new_user.lower())
print(new_low_users)

for current_user in current_users:
    if current_user.lower() in new_low_users:
        print("sorry")
    else:
        print("ok")

# 5-11

numbers = list(range(1,11))
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    else:
        print(f"{number}" + "rd")

