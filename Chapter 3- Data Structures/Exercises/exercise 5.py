# Inviting people to dinner.
guests = ['Samantha Lee', 'Jack Wolfe ', 'Robert Pickering']

name = guests[0].title()
print(f"{name}, we are looking forward to seeing you this Saturday for dinner.")

name = guests[1].title()
print(f"{name}, we are looking forward to seeing you this Saturday for dinner.")

name = guests[2].title()
print(f"{name}, we are looking forward to seeing you this Saturday for dinner.")

name = guests[1].title()
print(f"\nUnfortunately, {name} has informed that they couldn't make it to dinner.")

# Robert can't make it so Michelle it is.
del(guests[1])
guests.insert(1, 'Michelle Yeoh')

# Print the invitations again.
name = guests[0].title()
print(f"\n{name}, we are looking forward to seeing you this Saturday for dinner.")

name = guests[1].title()
print(f"{name}, we are looking forward to seeing you this Saturday for dinner.")

name = guests[2].title()
print(f"{name}, we are looking forward to seeing you this Saturday for dinner.")
