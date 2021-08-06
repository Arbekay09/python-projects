### seperate into list and strings
x=(input("Enter numbers seperated by comas: "))
list= x.split(",")
tuple = tuple(list)
print('List :',list)
print("Tuple: ",tuple)


print()

### ext of a file
x=input("Enter the filename : ")
x_ext= x.split(".")
print("Extension of the file is : "+ repr(x_ext[-1]))
print()

### first and last of a list
x=(input("Enter a list of numbers seperated by comas"))
list= x.split(",")
print("List : ",list)
print("The first element of the LIST is :" ,x[0])
print("The last element of the List is :",x[-1])

print()


### adding ls
stg= input("enter a word")
if stg[:2] == 'ls':
    print(stg)
else:
    print("ls"+ stg)



print()

###searching
def search(lst,x):
    if x in lst:
       return("TRUE")
    return("FAlSE")

print(search([1,5,8,3],3))
print(search([1,5,8,3],-1))

###diff in list
color1= set(["white","black","red" ])
color2= set (["red","green"])
print(color1.difference(color2))
print()

###
def thirdno(list):
    pos = 3-1
    index=0
    list1=(len(list))
    while list1>0:
        index = (pos+index) % list1
        print(list.pop(index))
        list1-=1
thirdno([10,20,30,40,50,50,70,80,90])


print()

def count(str):
    d = {}
    for n in str:
        keys= d.keys()
        if n in keys:
          d[n] += 1
        else:
         d[n] = 1
    return d
print(count('Google.com'))
print()



def diff(list1,list2):
    result = False
    for x in list1:
        for y in list2:
            if x==y:
                result = True
    return result

print(diff([1,2,3,4],[0,6,7,8]))
print(diff([1,2,3,4],[6,7,8,9]))

print()


s= input("enter string")
d=l=0
for x in s:
    if x.isdigit():
        d=d+1
    else:
        l=l+1
print("number of digits: " ,+ d)
print("number of letters: " ,+l)
print()
