def make_shirt(size='large', message='I love Python!'):
    """Modifying the shirt."""
    print(f"\nIn the process of selling a {size} t-shirt.")
    print(f'This is what you will read in the shirt: "{message}"')

make_shirt()
make_shirt(size='medium')
make_shirt('extra large', 'CSS is the way to go.')
