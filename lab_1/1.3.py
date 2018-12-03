
n1 = int(input())
n2 = int(input())
def func(num1,num2):
    if num1 > 0 or num2 > 0:
        if num1 % num2  is 0:
            return True
        else:
            return False
    else:
        raise Exception("NO dodatny chisla")




print(func(n1,n2))
