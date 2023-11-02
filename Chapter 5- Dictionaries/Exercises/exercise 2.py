glossary = {
    'string': 'A series of characters.',
    'comment': 'Notes for humans that are ignored by Python.',
    'list': 'mutable, a collection of items in a particular order.',
    'concatenation' : 'the process of appending one string to the end of another string.',
    'len': "returns the number of characters in a text string.",
    }

word = 'string'
print(f"\n{word.title()}: {glossary[word]}")

word = 'comment'
print(f"\n{word.title()}: {glossary[word]}")

word = 'list'
print(f"\n{word.title()}: {glossary[word]}")

word = 'concatenation'
print(f"\n{word.title()}: {glossary[word]}")

word = 'len'
print(f"\n{word.title()}: {glossary[word]}")
