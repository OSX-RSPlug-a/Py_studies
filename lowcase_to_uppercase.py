my_string = " VARIABLE_NAME_UPPER  VARIABLE_NAME_UPPER1  VARIABLE_NAME_UPPER2 "

uppercase_string = my_string.lower()

print(uppercase_string)

def switch_underscore_hyphen(input_string):
    return input_string.replace('_', '#TEMP#').replace('-', '_').replace('#TEMP#', '-')

mixed_string = uppercase_string
switched_string = switch_underscore_hyphen(mixed_string)

print(f"Original: {mixed_string}")
print(f"Modified: {switched_string}")
