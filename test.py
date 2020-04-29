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
    firstStr=str(coef[0])
    for i in range(1,len(coef),1):
        if (coef[i] > 0):
            firstStr+='+{}'.format(coef[i])
            for j in range(i):
                firstStr+='(x-{})'.format(x[j])
    print(firstStr)


x=[1,2,3,4]
y=[1,2,3,5]
abc=coef(x,y)
generateFormula(x,abc)
print(abc)
print(Eval(abc,x,100))