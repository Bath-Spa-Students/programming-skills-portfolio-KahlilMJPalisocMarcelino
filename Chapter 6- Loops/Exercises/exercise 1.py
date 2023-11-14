prompt = "\nHello dear customer, what pizza topping do you prefer?"
prompt += "\nAs soon as they answer, enter 'quit: '"

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"Thank you for confirming, we will add {topping} to your pizza.")
    else:
        break
