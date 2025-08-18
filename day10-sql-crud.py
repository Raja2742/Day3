import mysql.connector as sc

config={
    "host":"localhost",
    "user":"root",
    "password":"rajareddy@123",
    "database":"sportsdb"
}

conn=sc.connect(**config)
cursor=conn.cursor()

#create-upload new  match

cursor.execute("""
insert into cricket_scores(match_name,status,score,fetched_at)
values(%s,%s,%s,now())
""",("india vs america","upcoming match","['s':130,'a','s':150,'b']"))
print("inserted succesfully")


#read-fetch rows

cursor.execute("select * from cricket_scores  where status='not started' order by id")

rows=cursor.fetchall()
for row in rows:
    print("match:",row[1],end=" | ")
    print("score:",row[3])


#update-replace  with others

cursor.execute("update cricket_scores set match_name='india vs ingland',status='playing' where match_name='raja' ")
cursor.execute("select id from cricket_scores where match_name='india vs ingland'")
up=cursor.fetchall()
for u in up:
    print("updated",u,end=" ")

# delete-last 3 matches

cursor.execute("delete from cricket_scores where id in (select id from (select id from cricket_scores order by id desc limit 3) as temp)")



conn.commit()
cursor.close()
conn.close()
