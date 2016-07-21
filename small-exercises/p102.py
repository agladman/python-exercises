def comma(list):
    string = ''
    for item in list[0:-1]:
        string += item + ', '
    string += 'and ' + list[-1]
    print(string)

spam = ['apples', 'bananas', 'tofu', 'cats']

comma(spam)
