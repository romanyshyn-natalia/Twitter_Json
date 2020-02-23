import json


def get_dict(path):
    '''
    str -> dict
    Function for retrieving data from json to dict. 
    '''
    with open(path, 'r', encoding='utf-8') as f:
        decoded_data = json.load(f)
    return decoded_data


def key_inf(data):
    '''
    dict -> lst
    Function for getting needed information from dict, which was obtained from json. 
    '''
    profile = []
    print("You can choose through these keys: ")
    for key in data:
        print(key)
    inpt = input('Type here: ')
    profile.append(inpt)
    try:
        if inpt == 'users':
            elem = input('This is a list. Type an index (0-4) of element you want to look at:')
            try:
                for elemnt in range(len(data['users'])):
                    if elem == str(elemnt):
                        dct = data['users'][elemnt]
                        print('Now look at these keys, choose and write afterwards: ')
                        for key in dct:
                            print(key)
                        dct_content(dct, profile)
            except IndexError:
                print('There is only 5 elements in a list.')
        else:
            profile.append(data[inpt])
    except KeyError:
        print('This is the end of our journey(')
    return profile


def dct_content(dct, profile):
    '''
    dict, lst -> ()
    Function for iterating through dictionary.
    '''
    inp = input()
    profile.append(inp)
    for key in dct:
        if key == inp:
            profile.append(dct[key])
    print(profile)
    answer = input('Do you want some information (type y/n): ')
    if answer == 'y':
        dct_content(dct, profile)
    else:
        return profile


if __name__ == '__main__':
    path = 'data.json'
    dat = get_dict(path)
    print(key_inf(dat))
