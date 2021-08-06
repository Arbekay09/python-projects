a = 1 , 2 , 3 ,4 ,-5,-6,-12,0,-1,-100
sum = 0
for n in a:
    if n>0:
        sum = sum+n
        if n == 0:
            break
print (sum)
# space indexing
# string = 'This  is  a sentence'
# for s in string:
#     if s == " ":
#         print (" ",end="")
#     else:
#         print (s,end='')
print('*'*20)
s = 'This  is  a sentence'
print ("input:", (s))
print("output:",(s.replace("  ", " ")))