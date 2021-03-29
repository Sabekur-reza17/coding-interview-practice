def division(n1,n2):
    try:
        return n1/n2
    except ZeroDivisionError:
        print("can't divide by zero")    