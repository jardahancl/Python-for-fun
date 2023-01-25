def triangle(row):

    def getLetterPosition(letter):
        return ord(letter) - ord('a')

    def getMod26(n):
        return (n + 1) % 26

    while len(row) > 1:
        newrow = ''
        for i in range(len(row) - 1):
            newrow = newrow + chr(getMod26(getLetterPosition(row[i]) + getLetterPosition(row[i+1])) + ord('a'))
        row = newrow

    return row


# print(triangle('abcd'))
# print(triangle('codewars'))
print(triangle('youhavechosentotranslatethiskata'))
