
pet1 = {'type': 'dog',
    'owner': 'sammy'}

pet2 = {'type': 'cat',
    'owner': 'sarah'}

pet3 = {'type': 'parrot',
    'owner': 'omar'}
pet4 = {'type': 'hamster',
    'owner': 'Dana'}

pets = [pet1, pet2, pet3, pet4]

for pet in pets:
    print("Pet information:")
    for key, value in pet.items():
        print(f"{key.title()}: {value}")
    print()