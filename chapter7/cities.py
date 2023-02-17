prompt = "\nplease enter a city:"
prompt += "\n(enter quit to finish)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")