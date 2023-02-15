my_name ='zed A.shaw'
my_age=35
my_height=74
my_weight=180
my_eye='blue'
my_teeth='white'
my_hair='brown'

print("let's talk about", my_age)   #在print后加f可以输出字符串时省略大括号，
print("He's",my_height,"inchs tall")
print(f"he's {my_weight} ponds heavy")#在print后加f可以输出字符串时省略大括号，
print("actually that's not too heavy")
print(f"He's got {my_hair+str(my_age)}")  #在数字前加str可以使数字和字符连起来

print(f"his teeth are usually {my_teeth} depending on the coffee")

#this line is tricky, try to get it exactly right
total=my_age+my_height+my_weight
print(f"If i add {my_age},{my_height},and {my_weight} I get {total}.")
