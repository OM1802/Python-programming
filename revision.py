#Revision practice class codes
import pandas as pd
import numpy as np
#greatest of 4 numbers 
a=int(input("ENTER VALUE: "))
b=int(input("ENTER VALUE: "))
c=int(input("ENTER VALUE: "))
d=int(input("ENTER VALUE: "))
if(a>b and a>c and a>d):
    print(a, "IS THE GREATEST NUMBER")
elif(b>a and b>c and b>d):
    print(b, "IS THE GREATEST NUMBER")
elif(c>a and c>b and c>d):
    print(c, "IS THE GREATEST NUMBER")
else:
    print(d, "IS THE GREATEST NUMBER")

#odd numbers
for n in range(1,10,2):
    print(n)

#right angle triangle 📐 pattern 
for i in range(5):
    for j in range(i+1):
        print(j, end=" ")
    print()

#area of a room, no of chair size accomodable
a=40
b=50
cs=4
ar=(2*(a+b))
print(ar/cs)

#implementation of pandas library using different data structures
d1=np.array([10,20,30,40,50])#using array
d2=[1,2,3,4,5]#using list
d3=(70,52,41,71,55)#using tuple
d4={'OM':35, 'RAWAT':100, 'SHIWA':80, 'UDIT':50}#using set
myseries=pd.Series(d4)
print(myseries)


#user defined mathematical function declaration and calling 
def add(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)
    
def div(a,b):
    print(a//b)

def pro(a,b):
    print(a*b)
    
a=int(input("ENTER FIRST VALUE: "))
b=int(input("ENTER SECOND VALUE: "))
add(a,b)
sub(a,b)
div(a,b)
pro(a,b)

#switch case
student_details = {
    101: 'John',
    102: 'Alice',
    103: 'Bob',
    104: 'Emily',
    105: 'David'
}


student_marks = {
    101: 95,
    102: 87,
    103: 78,
    104: 65,
    105: 53
}


def assign_grade(marks):
    if marks >= 90:
        return 'O'
    elif marks >= 80:
        return 'A+'
    elif marks >= 70:
        return 'A'
    elif marks >= 60:
        return 'B+'
    elif marks >= 50:
        return 'B'
    else:
        return 'Fail'

student_results = {}

for reg_num, name in student_details.items():
    marks = student_marks.get(reg_num)
    if marks is not None:
        grade = assign_grade(marks)
        student_results[name] = {'Registration Number': reg_num, 'Marks': marks, 'Grade': grade}
print("Student Results:")
for name, result in student_results.items():
    print(f"Name: {name}, Registration Number: {result['Registration Number']}, Marks: {result['Marks']}, Grade: {result['Grade']}")


#sum of all numbers 
numele = int(input("Enter the number of elements: "))
numbers = []
for i in range(numele):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
total= 0
for num in numbers:
    total+= num
print("The sum of the numbers is:", total)

from queue import LifoQueue
stack =LifoQueue(maxsize=3)
print(stack.qsize())
stack.put('a')
stack.put('b')
stack.put('c')
print ("full:",stack.full())
print("size:",stack.qsize())


def km_to_miles(km):
    miles = km * 0.621371
    return miles
if __name__ == "__main__":
    km = float(input("Enter distance in kilometers: "))
    miles = km_to_miles(km)
    print(f"{km} kilometers is equal to {miles} miles")

from numpy import *
a=array([['mon',18,20,22,17],['Two',11,18,21,18],
['wed',15,21,20,19],['Thu',11,20,22,21],
['fri',18,17,23,22],['sat',12,22,20,18],
['sun',13,15,19,16]])
m=reshape(a,(7,5))
print(m)


from numpy import *
a=array([['mon',18,20,22,17],['Two',11,18,21,18],
['wed',15,21,20,19],['Thu',11,20,22,21],
['fri',18,17,23,22],['sat',12,22,20,18],
['sun',13,15,19,16]])
m=reshape(a,(7,5))
print(m)

from numpy import *
a=array([['mon',18,20,22,17],['Two',11,18,21,18],
['wed',15,21,20,19],['Thu',11,20,22,21],
['fri',18,17,23,22],['sat',12,22,20,18],
['sun',13,15,19,16]])
m=append(m,[['Avg',12,15,13,11]],0)
print(m)

from numpy import *
a=array([['mon',18,20,22,17],['Two',11,18,21,18],
['wed',15,21,20,19],['Thu',11,20,22,21],
['fri',18,17,23,22],['sat',12,22,20,18],
['sun',13,15,19,16]])
m=reshape(a,(7,5))
print(m)


set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
intersection_set = set1.intersection(set2)
print(intersection_set) 

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

union_set = set1 | set2
print("Union:", union_set) 

intersection_set = set1 & set2
print("Intersection:", intersection_set)  

difference_set = set1 - set2
print("Difference (set1 - set2):", difference_set)  

import collections
dict1 ={'day1':'mon','day2':'tue')
dict2 ={'day3':'wed','day4':'thu')

res = collection.chainmap(dict1,dict2)



class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def push(self,newVa1):
        
        NewNode = Node(newVa1)
        NewNode.next= self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode
            
    def listprint(self,node):
        while(node is not None):
            print(node.data),
            list=node
            node=node.next
                        
dllist=DoublyLinkedList()
dllist.push(12)
dllist.push(8)
dllist.push(62)
dllist.listprint(dllist.head)
#################################################################

def insert(self,prev_node,NewVal):
    if prev_node is None:
        if prev_node is None:
            return
        NewNode = Node(NewVa1)
        NewNode.next =prev_node.next
        prev_node.next =NewNode
        NewNode.prev =prev_node
        if NewNode.next is not None:
            NewNode.next,prev =NewNode
            
        #####################################################
         def append(self,NewVal):
             NewNode = Node(NewVa1)
              NewNode.next =None
              if self.head is None:
                  NewNode.prev =None
                  self.head =NewNode
                  return
              last = self.head
              while (last.next is not None):
                  last =last.next
                  last.next =NewNode
                  NewNode.prev =last
