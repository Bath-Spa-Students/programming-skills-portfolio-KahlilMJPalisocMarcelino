# Invite some people to dinner.
guests = ['Samantha Lee', 'Jack Wolfe ', 'Robert Pickering']

name = guests[0].title()
print(f"{name}, we hope you can come to dinner this Saturday.")

name = guests[1].title()
print(f"{name}, we hope you can come to dinner this Saturday.")

name = guests[2].title()
print(f"{name}, we hope you can come to dinner this Saturday.")

name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")

# Jack can't make it :( so we will invite Michelle Yeoh instead.
del(guests[1])
guests.insert(1, 'Michelle Yeoh')

# Print the invitations again.
name = guests[0].title()
print(f"\n{name}, we hope you can come to dinner this Saturday.")

name = guests[1].title()
print(f"{name}, we hope you can come to dinner this Saturday.")

name = guests[2].title()
print(f"{name}, ")

# We got a bigger table, so let's add some more people to the list.
print("\nWe got a bigger table!")
guests.insert(0, 'Johnny Depp')
guests.insert(2, 'Robert Downey Jr.')
guests.append('Erin Kellyman')

name = guests[0].title()
print(f"{name}, we hope you can come to dinner this Saturday.")

name = guests[1].title()
print(f"{name}, we hope you can come to dinner this Saturday..")

name = guests[2].title()
print(f"{name}, we hope you can come to dinner this Saturday.")

name = guests[3].title()
print(f"{name}, we hope you can come to dinner this Saturday.")

name = guests[4].title()
print(f"{name}, we hope you can come to dinner this Saturday.")

name = guests[5].title()
print(f"{name}, we hope you can come to dinner this Saturday.")

# It has called to our attention that some cannot reach on time!
print("\nWe are deeply sorry but we must inform you that we can only invite 2 people to dinner.")

name = guests.pop()
print(f"Our sincerest apologies, {name.title()} unfortunately there is no more room at the table.")

name = guests.pop()
print(f"Our sincerest apologies, {name.title()} unfortunately there is no more room at the table.")

name = guests.pop()
print(f"Our sincerest apologies, {name.title()} unfortunately there is no more room at the table.")

name = guests.pop()
print(f"Our sincerest apologies, {name.title()} unfortunately there is no more room at the table.")

# There should be two people left. Let's invite them.
name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

# Empty out the list.
del(guests[0])
del(guests[0])

# Prove the list is empty.
print(guests)
