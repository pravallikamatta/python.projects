import os
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def divi(a,b):
    return a/b

sym={ 
    '+':add,
    "-":sub,
    "*":mul,
    "/":divi
}
def cacula():
    first=int(input("enter first number-"))
    tuple=("+ "," -"," *"," /")
    print(tuple)
    end=False
    while not end:
        oper=input("pick an operator:")
        second=int(input("enter 2nd number:"))
        fun=sym[oper]
        res=fun(first,second)
        print(res)
        print(f"{first} {oper} {second}={res}")
        yn=input(f"continue calculation with {res} ?").lower()
        if yn=='yes':
            first=res
        elif yn == 'no':
                end=True
                os.system('cls')
                cacula()
        else:
            end=True
            print("----")  
cacula()            