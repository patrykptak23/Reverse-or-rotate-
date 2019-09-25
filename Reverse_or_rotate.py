from textwrap import wrap


def revrot(strng, sz):
    # your code
    if 0 < sz < len(strng):
        howManyDigits = len(list(strng))
        rest = howManyDigits % sz
        word = strng[:-rest]
        newDigits = wrap(word, sz)
        splitList = []
        finalList =[]
        for x in newDigits:
            splitedDigits = list(x)
            sum = 0
            for y in splitedDigits:
                sum += int(y)**3
            if sum % 2 == 0:
                splitedDigits.reverse()
            else:
                splitedDigits += [splitedDigits.pop(0)]
            splitList.append(splitedDigits)
        for z in splitList:
            finalList += z
        return ''.join(finalList)
    else:
        return ''

