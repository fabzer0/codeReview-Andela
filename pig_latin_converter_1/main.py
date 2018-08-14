from pythonds.basic.queue import Queue
from pythonds.basic.stack import Stack

def pig_latin_converter(word):

    if type(word) != str:
        raise TypeError('Argument should be a string')

    my_simulation = Queue()
    to_lower = word.lower()
    modified = list(to_lower)
    pos = 0
    found = True
    if modified[0] in ['a', 'e', 'i', 'o', 'u']:
        return word + 'way'
    else:
        while pos <= len(word) and found:
            if modified[pos] in ['a', 'e', 'i', 'o', 'u']:
                found = False
            else:
                my_simulation.enqueue(modified[pos])
                pos += 1
    rounds = my_simulation.size()
    simulator_stack = Stack()
    for i in modified:
        simulator_stack.push(i)
    diff = len(word) - rounds
    fixed = []
    for j in range(diff):
        fixed.append(simulator_stack.pop())
    fixed.reverse()
    final_word = ''
    to_fix_with = []
    while not my_simulation.isEmpty():
        to_fix_with.append(my_simulation.dequeue())
    final_word = ''.join(fixed) + ''.join(to_fix_with) + 'ay'
    return final_word


if __name__ == '__main__':
    print(pig_latin_converter('will'))
    print(pig_latin_converter('dog'))
    print(pig_latin_converter('category'))
    print(pig_latin_converter('chatter'))
    print(pig_latin_converter('trash'))
    print(pig_latin_converter('gynacologist'))
    print(pig_latin_converter('andela'))
    print(pig_latin_converter('electrician'))
