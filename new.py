abc = "aaaa aaaa ssss dffd ssss aaaa bbbb"
spnei =abc.split()
#print(abc)
for num in spnei:
    if num == "aaaa" or num == "ssss":
        print("good")
