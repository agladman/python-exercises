# tablePrinter.py - an exercise from p143 of ATBS

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    colWidths = [0] * len(tableData)

    # capture the colWidths to use later in .rjust()
    # correct result should be [8, 5, 5]
    for i in range(len(tableData)):
        colWidths[i] = len(max(tableData[i]))


    return colWidths # remove this line and lines 18 and 20 once this part is working

debug = printTable(tableData)

print(debug)
