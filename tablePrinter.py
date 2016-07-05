# tablePrinter.py - an exercise from p143 of ATBS

# script returns the expected result, but to be honest it looks like
# a horrible mess. I bet this is not the best way to do it.

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    colWidths = [0] * len(tableData)

    # capture the colWidths to use later in .rjust()
    for i in range(len(tableData)):
        colWidths[i] = len((max(tableData[i], key=len)))

    # print the table

    # attempt without using range - failed
    # a = 0
    # for word in tableData[a]:
    #     for wordlist in tableData:
    #         print(word)
    #         a += 1
    # print('\n')

    # from p103.py - didn't understand it then either and had to google
    for j in range(len(tableData[0])):
        for i in range(len(tableData)):
            print(tableData[i][j].rjust(colWidths[i]), end=' ')
        print('\n')

printTable(tableData)
