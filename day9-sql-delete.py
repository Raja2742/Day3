import mysql.connector as sc

config={
    "host":"localhost",
    "user":"root",
    "password":"rajareddy@123",
    "database":"sportsdb"
}

conn=sc.connect(**config)
cursor=conn.cursor()

cursor.execute("""
delete from cricket_scores
where id not in(select id from(select id from cricket_scores order by id desc limit 25) as temp)
""")

print(f"delete {cursor.rowcount} old matches")

cursor.execute("set @count=0;")
cursor.execute("update cricket_scores set id=(@count:=@count+1)")
cursor.execute("alter table cricket_scores auto_increment=1")

conn.commit()

cursor.close()
conn.close()