"""
In this demo, we will try out:
1. Creation of List
2. Random access of elements
3. Adding of elements & concatanation of list

"""

#Creating List

lis1=["apple",1,1.4,1+2j]
print(lis1)             

print(type(lis1[3]))   #Finding type of any element of list based on index
print(type(lis1))

print(len(lis1))    #Finding Length of list

fruits=list(('apple','mango','orange','banana','grapes'))           #Creating list using List constructor
print(fruits)
print(type(fruits))

print(fruits[3])

fruits[1]='pineapple'
print(fruits)

lis1=[1,2,3]
lis1.append('a')
print(lis1)
print(len(lis1))

"""
Output:

['apple', 1, 1.4, (1+2j)]
<class 'complex'>
<class 'list'>
4
['apple', 'mango', 'orange', 'banana', 'grapes']
<class 'list'>
banana
['apple', 'pineapple', 'orange', 'banana', 'grapes']
[1, 2, 3, 'a']
4

"""