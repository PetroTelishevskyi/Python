from T3 import func
arg1 = int(input())
arg2 = int(input())
def newfunc(arg1, arg2):
    func(arg1,arg2)
    if arg1 > arg2:
        arg1, arg2 = arg2, arg1
    lst = []
    for i in range(arg1, arg2 + 1):
        if i > 0:
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                lst.append(i)
    if len(lst) == 0:
        raise Exception("NoSimpleDigits!!!")
    else:
        return lst

print(newfunc(arg1,arg2))
