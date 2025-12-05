import string 

setence = "Yo from the @$*! side"

print(''.join(c for c in setence if c not in string.punctuation))

