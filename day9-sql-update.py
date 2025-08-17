import mysql.connector as sc

config={
    "host":"localhost",
    "user":"root",
    "password":"rajareddy@123",
    "database":"sportsdb"
    }

conn=sc.connect(**config)
cursor=conn.cursor()


cursor.execute("select id from cricket_scores where status='draw'")
rows=cursor.fetchall()
if not rows:
    print("no rows found")
else:
    print("rows that will be updated",[r[0] for r in rows ])


#update
cursor.execute("""
update cricket_scores
set status='India A Women won by 2 wkts'
where status='draw'
""")


conn.commit()
print(f"updated {cursor.rowcount} rows")

cursor.close()
conn.close()