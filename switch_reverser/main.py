def switch_reverser(alist):

    if type(alist) != list:
        raise TypeError('Argument should be a list')

    if all(isinstance(n, int) for n in alist):
        alist.reverse()
        return alist
    elif all(isinstance(n, str) for n in alist):
        to_upper = [x.upper() for x in alist]
        return to_upper
    else:
        return alist

if __name__ == '__main__':
    print(switch_reverser([1,2,3,4,5,6]))
    print(switch_reverser([1,'fabisch',3,4,True,6]))
    print(switch_reverser(['jake','mike','lebron','kevin','star']))
