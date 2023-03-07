file_name = 'F:\pythonfile\practise\chapter10\pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()


birthday = input("enter your birthday, in the form of mmddyy:")
if birthday in pi_string:
    print("your birthday appears in ")

print(pi_string[:50]+ '...')
print(len(pi_string))