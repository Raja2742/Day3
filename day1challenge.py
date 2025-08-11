list=input("enter marks").split(",")
marks=[]
for i in list:
    mark=int(i)
    marks.append(mark)
avg=0
highest=0
lowest=0
greatmarks=0
for i in marks:
    avg+=i
    avg/=len(marks)
for i in marks:
    if i>highest:
        highest=i
    if i>avg:
        greatmarks+=1
hig=highest
for i in marks:
    if i<hig:
        lowest=i
        hig=lowest
    
print(int(avg),"is an average mark")
print(highest,"is an highest mark")
print(lowest,"is an lowest mark")
print(greatmarks,"getting more than average")