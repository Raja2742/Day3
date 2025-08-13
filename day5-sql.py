import mysql.connector as sc
import pandas as pd
import matplotlib.pyplot as plt

#connect to my sql
conn=sc.connect(
    host="localhost",
    user="root",
    password="rajareddy@123",
    database="studentdb"
)

cursor=conn.cursor()

#query using pandas
df=pd.read_sql("select * from student",conn)
print("All students:\n",df)

#filter aids students
aids_df=pd.read_sql("select name,marks from student where dep='aids'",conn)
print("AIDS students:\n",aids_df)

top_cse=pd.read_sql("select name,marks from student where dep='cse' and marks>60 ",conn)
plt.bar(top_cse["name"],top_cse["marks"],color='skyblue')
plt.title("top cse scored students")
plt.xlabel("name")
plt.ylabel("marks")
plt.show()
conn.close