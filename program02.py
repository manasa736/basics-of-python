def fun(str1):
    print(str1)
    return
fun("I'm first call to user defined function!")
fun("Again second call to the same function")


def printMe(str1,n):
    n[0]='deepika'
    print(str1,n)
    return

a=['harshi','manasa']
printMe("wakeup",a)
print('a:',a)


def changeMe(lstn):
    lstn=['pavani','madhavi','gagana']
    print(lstn)
    return
lst=[1,4,11,44]
print(changeMe(lst))
print('lst:',lst)
