import mysql.connector  
  
#Create the connection object   
myconn = mysql.connector.connect(host = "127.0.0.1", user = "root",password = "ankita", auth_plugin='mysql_native_password', database = "Pitch_Perfect")  
  
#printing the connection object   
print(myconn)  
#creating the cursor object  
cur = myconn.cursor()  

try:  
    #     #creating a new database  
    # cur.execute("create database Pitch_Perfect")  
    # dbs = cur.execute("show databases")  
    # dbs = cur.execute("create table Song(name varchar(20) not null, artist int(20) not null, song_id int(20) autoincrement primary key,genre varchar(50), mp3 varchar(100) not null, csv varchar(100) not null, Total_Score int(20))") 
    # dbs = cur.execute("create table User(name varchar(20) not null, id int(20) not null primary key, low_note float not null, high_note float not null)") 
    # dbs = cur.execute("create table Scoring(user_id varchar(20) not null, song_id int(20) not null primary key, total_score )") 
    # dbs = cur.execute("alter table Song add artist")
    # dbs = cur.execute("insert into Song(name,id,mp3,csv) values("Shape Of You","")")
    dbs = cur.execute("insert into Song(name,id,mp3,csv) values("Shape Of You","")")
except:  
    myconn.rollback()  
for x in cur:  
    print(x)  
myconn.close()  