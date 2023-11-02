rivers = {
    'pasig': 'philippines',
    'amazon': 'south america',
    'danube': 'europe',
    'nile': 'egypt',
    'yangtze': 'china',
    }

for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")

print("\nThese rivers are included in this data set:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nHere are the countries that are included in this data set:")
for country in rivers.values():
    print(f"- {country.title()}")
