def check_upper(input):
    uppers = 0
    upper_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for char in input:
        if char in upper_list:
            uppers += 1
    if uppers > 0:
        return True
    else:
        return False

def check_lower(input):
    lowers = 0
    lower_list = 'abcdefghijklmnopqrstuvwxyz'
    for char in input:
        if char in lower_list:
            lowers += 1
    if lowers > 0:
        return True
    else:
        return False

def check_number(input):
    numbers = 0
    number_list = '0123456789'
    for char in input:
        if char in number_list:
            numbers += 1
    if numbers > 0:
        return True
    else:
        return False

def check_special(input):
    specials = 0
    special_list = '@#$'
    for char in input:
        if char in special_list:
            specials += 1
    if specials > 0:
        return True
    else:
        return False

def check_length(input):
    if 6 <= len(input) <= 12:
        return True
    else:
        return False

def valid_passwords(input):
    split_input = input.split(',')
    for name in split_input:
        check_dict = {
            'upper' : check_upper(name),
            'lower' : check_lower(name),
            'number' : check_number(name),
            'special' : check_special(name),
            'len' : check_length(name)
        }

        valid = True
        for i in check_dict.keys():
            if not check_dict[i]:
                valid = False
                break
        if valid:
            yield name

def output_func(passwords):
    my_list = []
    for valid in valid_passwords(passwords):
        my_list.append(valid)
    my_strings = ','.join(map(str, my_list))
    return my_strings

if __name__ == '__main__':
    input_passwords = ['f@b1$cH', 'jane', 'R0ok1e@']
    passw = ','.join(input_passwords)
    print(output_func(passw))
