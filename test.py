def coef(x, y):
    n = len(x)
    a = []
    for i in range(n):
        a.append(y[i])

    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            a[i] = float(a[i]-a[i-1])/float(x[i]-x[i-j])

    return a # return an array of coefficient

def Eval(a, x, r):
    n = len(a)
    sum=a[0]
    for i in range(1,n,1):
        temp=1
        for j in range(i):
            temp *= r-x[j]
        sum+=a[i]*temp
    return sum # return the y_value interpolation

def generateFormula(x,coef):
    formula=str(coef[0])
    for i in range(1,len(coef),1):
        if (coef[i] != 0):
            if(coef[i]<0):
                formula += ' - '
            else:
                formula += ' + '
            formula+='{}'.format(coef[i])
            for j in range(i):
                formula+='(x-{})'.format(x[j])
    return formula



x=input("Enter a list of x-points (separated by space): ")
y=input("Enter a list of corresponding y-points (separated by space): ")

xList=[int(xInt) for xInt in x.split(' ')]
yList=[int(yInt) for yInt in y.split(' ')]
coefNewton=coef(xList,yList)
print('Final Polynomial: '+generateFormula(xList,coefNewton))
print('The coefficients are: '+str(coefNewton))
evaluate='10'
while(evaluate.isnumeric()):
    evaluate=input('Enter the x-point to be evaluated: ')
    if(evaluate.isnumeric()):
        evalInt=int(evaluate)
        print('The evaluated y-point is: '+str(Eval(coefNewton,xList,evalInt)))