'''
Practical Restriction Mapping Algorithm - Author: Alexandre Lissac
Steven Skiena's algorithm
Works in Python 3.x
example input: 2 2 3 3 4 5 6 7 8 10
output: 0 2 4 7 10
References: 
	An Introduction to Bioinformatics Algorithms (Jones and Pevzner)
	http://www.cs.ukzn.ac.za/~hughm/bio/docs/IntroToBioinfAlgorithms.pdf
'''


def partialDigest(L):
    width = L[len(L) - 1]
    L = [x for x in L if x != width]
    X = [0, width]
    return sorted(place(L, L, X))


def place(targetL, modifiedL, X):
    if not modifiedL:
        return X
    yVal = modifiedL[len(modifiedL) - 1]
    x1 = yVal  # Bigger Number
    x2 = X[len(X) - 1] - yVal  # Smaller Number

    # If both acceptable, keep smallest one and remove both x
    if isXValueUsable(x2, X, targetL) and isXValueUsable(x1, X, targetL):
        X.insert(1, x2)
        modifiedL = [x for x in modifiedL if x != x2 if x != x1]
        return place(targetL, modifiedL, X)
    else:
        # Keep usable X and remove it from modified L
        if isXValueUsable(x2, X, targetL):
            X.insert(1, x2)
            modifiedL = [x for x in modifiedL if x != x2]
            return place(targetL, modifiedL, X)
        elif isXValueUsable(x1, X, targetL):
            X.insert(1, x1)
            modifiedL = [x for x in modifiedL if x != x1]
            return place(targetL, modifiedL, X)
        else:
            # Remove both value from modified L
            modifiedL = [x for x in modifiedL if x != x2 if x != x1]
            return place(targetL, modifiedL, X)


# Verify whether xValue could be inserted in X set
def isXValueUsable(xValue, X, targetL):
    XD = [abs(xValue - elem) for elem in X]
    output = True if all(elem in targetL for elem in XD) else False
    return output


if __name__ == "__main__":
    L = [2, 2, 3, 3, 4, 5, 6, 7, 8, 10]
    print(partialDigest(L))
