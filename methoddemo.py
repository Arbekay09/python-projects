
def methdemo():
    n1=int (input("enter first number:"))
    n2=int (input("enter second number:"))
    v=int(input("Enter your choice. 1.ADDITION  2.SUBTRACTION  3.MULTIPLICATION  4.DIVISION"))

    if v == 1:
        sum = int (n1) + int (n2)
        print(sum)
    if v == 2:
        sub = int(n1) - int(n2)
        print(sub)
    if v == 3:
        mul = int(n1)* int(n2)
        print(mul)
    if v == 4:
        div = int(n1)/int(n2)
        print(div)
methdemo()







#
# def meth():
#     n=int(input("enter number"))
#     print (str(n)[::-1])
# meth()