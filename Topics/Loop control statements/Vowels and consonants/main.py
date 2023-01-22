import string
phrase = input()
vowels = 'aeiou'
for c in phrase:
    if c in string.ascii_letters:
        if c in vowels:
            print('vowel')
        else:
            print('consonant')
    else:
        break
