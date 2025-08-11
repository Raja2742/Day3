#1
int=int()
float=float()
string=""
list=[]
tuple=()
dict={}

print(type(int))
print(type(float))
print(type(string))
print(type(list))
print(type(tuple))
print(type(dict))

#2
list1=[1,2,3,4,5]
list2=[]
for num in list1:
    nums=num**2
    list2.append(nums)
print(list2)

keys=['name','age','dept','state']
values=['john',20,'aids']
dict1=dict(zip(keys,values))
print(dict1)


#3
n=int(input("give a numper:"))
def is_prime(num):
    if num<2 :
        return False
    for i in range(2,int(num*1/2)+1):
        if num%i==0:
            return False
        else:
            return True

if is_prime(n):
    print(n,"is  an prime number")
else:
    print(n,"is not an prime number")

#4
class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
a = input("Enter name: ")
b = int(input("Enter roll number: "))
c = int(input("Enter marks: "))

stu=Student(a,b,c)
print(stu.name)
print(stu.roll_no)
print(stu.marks)
