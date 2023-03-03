def divide(n1,n2):
    try:
        r=n1//n2
        print(r)
    except ZeroDivisionError:
        print("cant")
    else:
        print("evnfreo")
    finally:
        print("er ngeiu r")
divide(5,2)
print("*"*50)
divide(1,0)