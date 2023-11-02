glossary = {
    'string': 'A series of characters.',
    'comment': 'Notes for humans that are ignored by Python.',
    'list': 'mutable, a collection of items in a particular order.',
    'concatenation' : 'the process of appending one string to the end of another string.',
    'len': "returns the number of characters in a text string.",
    'float': 'A numerical value with a decimal component.',
    'value': 'An item associated with a key in a dictionary.',
    'key': 'The first item in a key-value pair in a dictionary.'
    }

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")
