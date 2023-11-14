sandwich_orders = [
    'pastrami', 'pastrami', 'chicken & ham', 'shrimp & cheese', 'tuna & mayo',
    'peanut butter & jelly', 'pastrami']
finished_sandwiches = []

print("We regret to inform you but the deli has run out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Please wait while we make your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"Ding ding ding, calling in for your {sandwich} sandwich.")
