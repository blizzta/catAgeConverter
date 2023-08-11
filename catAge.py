catOrDog = input('Hey do you have a cat or a dog ?? ').lower()

if catOrDog == 'cat':
 cat_age = int(input('How old is your cat ?? '))

 cat_age_in_human = cat_age * 8

 print(f'Hey your cat is {cat_age_in_human} in human years')
 
elif catOrDog == 'hund':
    dogAge = int(input('How old is your dog ?? '))
    
    dogAgeInHuman = dogAge * 6
    
    print(f'Hey your {dogAgeInHuman} in human years')
    
else :
    print('Please enter cat or dog')