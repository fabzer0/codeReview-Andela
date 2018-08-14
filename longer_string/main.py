def longer_string(a, b):

    if type(a) != str and type(b) != str:
        raise TypeError('Argument should be a string')

    if len(a) > len(b):
        return a

    elif len(a) == len(b):
        x = (a,b)
        return '\n'.join(x)

    else:
        return b

if __name__ == '__main__':
    print(longer_string('andela', 'kenya'))
    print(longer_string('andela', 'nigeria'))
    print(longer_string('andela', 'rwanda'))
