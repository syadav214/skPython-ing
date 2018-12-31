def translate(pharse):
    translation = ''
    for letter in pharse:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation += 'G'
            else:
                translation += 'g'
        else:
            translation += letter
    return translation


print(translate(input("Enter a phrase: ")))
