'''
Greedy Algorithm - Author: Alexandre Lissac
Improved Breakpoint Reversal Sort Algorithm
Works in Python 3.x
example input: [0, 8, 2, 7, 6, 5, 1, 4, 3, 9]
output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
References: 
	An Introduction to Bioinformatics Algorithms (Jones and Pevzner)
	http://www.cs.ukzn.ac.za/~hughm/bio/docs/IntroToBioinfAlgorithms.pdf
'''

'''
Get unsorted list and return sorted list using breakpoing reversal sort
'''


def breakpointReversalSort(liste):
    while getBreakpoint(liste) > 0:
        print(liste)
        asc_list, desc_list = identifyAscDesc(liste)
        if hasDescStrip(desc_list):
            liste = identifyBestReverse(
                liste, [element for element in desc_list if len(element[1]) > 1])
        else:
            liste = flipAscStrip(
                liste, [element for element in asc_list if len(element[1]) > 1])
    return liste


def getBreakpoint(liste):
    '''Return amount of breakpoints in the list'''
    count = 0
    for i in range(len(liste) - 1):
        if abs(liste[i] - liste[i+1]) != 1:
            count += 1
    return count


def hasDescStrip(liste):
    '''Check if desc_list has a strip, which is a sequence of more than 1 element'''
    descTripFound = False
    for element in liste:
        if len(element[1]) > 1:
            descTripFound = True
    return descTripFound


def identifyBestReverse(liste, desc_list):
    '''Identify strip with smaller k element and correctly reverse'''
    smallestK = min([element for _, strip in desc_list for element in strip])
    startIndex, endIndex = liste.index(smallestK-1), liste.index(smallestK)
    reversedCutArray = liste[:][startIndex+1:endIndex+1][::-1]
    return doReverseDesc(liste, startIndex, endIndex, reversedCutArray)


def flipAscStrip(liste, asc_liste):
    '''Pick first element of ascendant list and correctly reverse'''
    for element in asc_liste:
        if 0 not in element[1] and len(liste)-1 not in element[1]:
            startIndex = element[0]
            endIndex = startIndex + len(element[1])
            reversedCutArray = liste[:][startIndex:endIndex][::-1]
            return doReverseAsc(liste, startIndex, endIndex, reversedCutArray)


def doReverseDesc(liste, startIndex, endIndex, reversedCutArray):
    '''
    Do the reverse for descendant list
    startIndex+1 & endIndex+1 because smallest k needs to be next to smallest k-1, and not replace it
    '''
    return liste[:startIndex+1] + reversedCutArray + liste[endIndex+1:]


def doReverseAsc(liste, startIndex, endIndex, reversedCutArray):
    '''
    Do the reverse for ascendant list
    startIndex & endIndex because last value of strip needs to replace first value of strip
    '''
    return liste[:startIndex] + reversedCutArray + liste[endIndex:]


def identifyAscDesc(liste):
    '''Identify and return list of ascendent and descendent strip'''
    asc_list, desc_list = [], []
    countIndex = 0
    while countIndex <= (len(liste) - 1):
        if countIndex < (len(liste) - 2) and liste[countIndex] - 1 == liste[countIndex+1]:
            holder = []
            startIndex = countIndex
            while countIndex < (len(liste) - 2) and liste[countIndex] - 1 == liste[countIndex+1]:
                holder.append(liste[countIndex])
                countIndex += 1
            else:
                holder.append(liste[countIndex])
                countIndex += 1
            desc_list.append((startIndex, holder))
        elif countIndex < (len(liste) - 2) and liste[countIndex] + 1 == liste[countIndex+1]:
            holder = []
            startIndex = countIndex
            while countIndex < (len(liste) - 2) and liste[countIndex] + 1 == liste[countIndex+1]:
                holder.append(liste[countIndex])
                countIndex += 1
            else:
                holder.append(liste[countIndex])
                countIndex += 1
            asc_list.append((startIndex, holder))
        else:
            if countIndex == 0 or countIndex == (len(liste) - 1):
                asc_list.append((countIndex, [liste[countIndex]]))
            else:
                desc_list.append((countIndex, [liste[countIndex]]))
            countIndex += 1
    return asc_list, desc_list


if __name__ == "__main__":
    liste = [0, 8, 2, 7, 6, 5, 1, 4, 3, 9]
    print(breakpointReversalSort(liste))
