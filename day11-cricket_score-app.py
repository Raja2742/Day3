import mysql.connector as sc

config={
    "host":"localhost",
    "user":"root",
    "password":"rajareddy@123",
    "database":"sportsdb"
}

def con():
    return sc.connect(**config)

def insert_match():
    conn=con()
    cursor=conn.cursor()
    match_name=input("give match_name:")
    status=input("give status:")
    score=input("give score:")
    
    cursor.execute("""insert into cricket_scores(match_name,status,score,fetched_at)
                   values(%s,%s,%s,now())""",(match_name,status,score))
    conn.commit()
    cursor.close()
    conn.close()


def read():
    conn=con()
    cursor=conn.cursor()
    cursor.execute("select * from cricket_scores")
    matches=cursor.fetchall()
    print("="*49,"matches","="*49)
    for match in matches:
        print("match_name:",match[1],end="\n")
        print("status:",match[2],end="\n")
        print("score:",match[3],end="\n")
        print("="*50)
    conn.commit()
    cursor.close()
    conn.close()


def update():
    conn=con()
    cursor=conn.cursor()
    match_name=input("enter match_name where you want to update:")
    status=input("give status what you want to update:")
    
    
    # cursor.execute("select id from cricket_scores where match_name=%s",(match_name))
    # udid=cursor.fetchall()
    # print("updated id:",udid)

    cursor.execute("""update cricket_scores set status=%s where match_name=%s
    """,(status,match_name))
    
    conn.commit()
    cursor.close()
    conn.close()


def delete():
    conn=con()
    cursor=conn.cursor()
    match_name=input("enter match_name  you want to delete:")
    cursor.execute("select id from cricket_scores where match_name=%s",(match_name,))
    udid=cursor.fetchall()
    print("deleted id:",udid)

    cursor.execute("delete from cricket_scores where match_name = %s",(match_name,))
    conn.commit()
    cursor.close()
    conn.close()

def menu():
    print("==select any one==")
    print("1 -> insert match")
    print("2 -> read")
    print("3 -> update")
    print("4 -> delete")

    selected=input("enter number:")

    if selected=="1":
        insert_match()
    elif selected=="2":
        read()
    elif selected=="3":
        update()
    elif selected=="4":
        delete()
    else:
        print("enter from 1 to 4")

menu()