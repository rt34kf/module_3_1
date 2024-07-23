calls = 0

def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    string1 = []
    string1.append(len(string))
    string1.append(string.upper())
    string1.append(string.lower())
    count_calls()
    return string1

def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    i = []
    for j in list_to_search:
        if string.lower() in j.lower():
            i.append(j.lower())
            return True
    else:
        return False


print(string_info('Viktoriya'))
print(string_info('Penza'))
print(is_contains('Rebys', ['bus', 'RyS', 'REBYS']))
print(is_contains('cyclik', ['recycling', 'cyclic']))
print(calls)


















