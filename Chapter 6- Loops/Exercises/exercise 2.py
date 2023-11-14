prompt = "\nWelcome to the cinema, how old are you?"
prompt += "\nAs soon as they answer, enter 'quit: '"

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("Great! Your baby gets in for free, no need to pay!")
    elif age < 13:
        print("Thank You, Your ticket will be $10.")
    else:
        print("Thank You, Your ticket will be $15.")
