
from fractions import Fraction
import math
import pandas as pd

def coef(x, y):
    n = len(x)
    a = []
    for i in range(n):
        a.append(y[i])

    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            a[i] = Fraction(float(a[i]-a[i-1]) /
                            float(x[i]-x[i-j])).limit_denominator()

    return a  # return an array of coefficient


def Eval(a, x, r):
    n = len(a)
    sum = a[0]
    for i in range(1, n, 1):
        temp = 1
        for j in range(i):
            temp *= r-x[j]
        sum += a[i]*temp
    return sum  # return the y_value interpolation


def generateFormula(x, coef):
    formula = str(coef[0])
    for i in range(1, len(coef), 1):
        if (coef[i] != 0):
            if(coef[i] < 0):
                formula += ' - '
            else:
                formula += ' + '
            formula += '({})'.format(coef[i])
            for j in range(i):
                formula += '(x-{})'.format(x[j])

    return formula


def determineXPoint(xList, location):
    if location > len(xList)-1:
        return 'error'
    lowerLoc = math.floor(location)
    upperLoc = math.ceil(location)
    lowerX = xList[lowerLoc]
    higherX = xList[upperLoc]
    diff = higherX-lowerX
    pointInt = float(splitIntDec(location))
    toBePlus = diff*pointInt
    xPoint = lowerX+toBePlus
    return xPoint


def splitIntDec(location):
    splitted = str(location).split('.')
    return '0.'+splitted[1]


def convertFraction(frac):
    if('/' in frac):
        fracs = frac.split('/')
        return float(fracs[0])/float(fracs[1])
    return float(frac)


def main():
    # x = input("Enter x-points (separated by comma): ")
    # y = input("Enter corresponding y-points (separated by comma): ")

    df = pd.read_csv("data.txt", header=None, sep=" ")
    data = df.T
    xList = list(data[0].values)
    yList = list(data[1].values)
    print("X points:", xList)
    print("Y points:", yList)

    # xList = [convertFraction(xFloat) for xFloat in x.split(',')]
    # yList = [convertFraction(yFloat) for yFloat in y.split(',')]

    assert len(xList) == len(yList)

    coefNewton = coef(xList, yList)
    print('Final Polynomial: ' + generateFormula(xList, coefNewton))
    print('The coefficients are: ' + str([str(i) for i in coefNewton]))
    evaluate = '10'
    while(evaluate.isalpha() == False):
        evaluate = input(
            'Enter the location to be evaluated (Character to quit): ')
        if(evaluate.isalpha() == False):
            evalInt = convertFraction(evaluate)
            xPoint = determineXPoint(xList, evalInt)
            if xPoint == 'error':
                print(
                    'The location exceeds the length of the input list given. Please select another location.')
            else:
                print('The x-point at the location is: '+str(xPoint))
                print('The evaluated corresponding y-point is: ' +
                      str(Eval(coefNewton, xList, xPoint)))


if __name__ == '__main__':
    main()
