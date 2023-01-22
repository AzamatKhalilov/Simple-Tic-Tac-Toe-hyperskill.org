string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
n = 0
for i in vowels:
    for j in string:
        if i == j:
            n += 1
print(n)
