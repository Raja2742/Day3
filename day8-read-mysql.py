import mysql.connector as sc

db_config={
    "host":"localhost",
    "user":"root",
    "password":"rajareddy@123",
    "database":"sportsdb"
}

conn=sc.connect(**db_config)
cursor=conn.cursor()


#fetch last 5 matches
cursor.execute("select match_name,status,fetched_at from cricket_scores order by id desc limit 5 ")

rows=cursor.fetchall()
print("\n📌 last 5 matches stored:\n")
for row in rows:
    print(f"match:{row[0]}")
    print(f"status:{row[1]}")
    print(f"fetched at:{row[2]}")
    print("-"*40)
cursor.close()
conn.close()