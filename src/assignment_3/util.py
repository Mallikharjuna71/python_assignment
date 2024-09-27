def mutate_string():
    string = input('enter a string: ')
    position = int(input('index where you want to insert: '))
    character = input('enter the character to insert: ')
    r = string[:position]+character+string[position:]
    return r