import requests
import mysql.connector 
from datetime import datetime
import time
import json

#api
api_name="57be8f05-9ff1-464f-bfea-38de9a24b101"
base="https://api.cricapi.com/v1/currentMatches"
url=f"{base}?apikey={api_name}&offset=0"
db_config={
    "host":"localhost",
    "user":"root",
    "password":"rajareddy@123",
    "database":"sportsdb"
}
def fetch_live_score():
    try:
        responce=requests.get(url,timeout=10)
        responce.raise_for_status()
        data=responce.json()
        if data.get("status")!="success":
            raise ValueError(data)
        return data.get("data",[])
    except Exception as e:
        print("error fetching data:",e)
        return []

#mysql
conn=mysql.connector.connect(**db_config)
cursor=conn.cursor()
cursor.execute("create database if not exists sportsdb")
cursor.execute("""
create table if not exists cricket_scores(
    id int AUTO_INCREMENT primary key,
    match_name VARCHAR(255),
    status varchar(200),
    score text,
    fetched_at datetime
)
""")

def store_score(matches):
    for match in matches:
        match_name=match.get("name","unknown")
        status=match.get("status","unknown")
        score=json.dumps(match.get("score","No score"))
        timestamp=datetime.now()
        

        test_match = matches[0]
        print("Tuple length:", len((match_name, status, json.dumps(score), timestamp)))



        print(f"inserting:({str(match_name)},{str(status)},{str(score)},{timestamp})")

        try:
            cursor.execute("""
            INSERT INTO cricket_scores(match_name,status,score,fetch_at)
            values(%S,%S,%S,%s)
            """,(str(match_name),str(status),json.dumps(score),timestamp))
        except Exception as e:
            print("insert error:",e)
    
    conn.commit()


matches=fetch_live_score()
if matches:
    store_score(matches)
    print(f"stored{len(matches)} matches at {datetime.now()}")
else:
    print("no matches found.")


# #autometic
# import time

# while True:
#     matches = fetch_live_score()
#     if matches:
#         store_score(matches)
#         print(f"Stored {len(matches)} matches at {datetime.now()}")
#     else:
#         print("No matches found.")
#     time.sleep(300)  # wait 5 minutes
