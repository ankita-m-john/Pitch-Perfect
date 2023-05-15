import mysql.connector  
  
#Create the connection object   
myconn = mysql.connector.connect(host = "127.0.0.1", user = "root",password = "ankita", auth_plugin='mysql_native_password', database = "Pitch_Perfect")  
  
#printing the connection object   
# print(myconn)  
#creating the cursor object  
cur = myconn.cursor()  

try:  
    #     #creating a new database  
    # cur.execute("create database Pitch_Perfect")  
    dbs = cur.execute("desc table Song") 
    # dbs = cur.execute("create table Song(song_id int(20) autoincrement primary key, name varchar(20) not null, artist int(20) not null, genre varchar(50), mp3 varchar(100) not null, csv varchar(100) not null, lyrics varchar(100) not null)") 
    # dbs = cur.execute("create table User(user_id int(20) not null primary key, name varchar(20) not null, low_note float not null, high_note float not null)") 
    # dbs = cur.execute("create table Scoring(user_id varchar(20) not null, song_id int(20) not null primary key, Total_Score int(20))") 
    # dbs = cur.execute("alter table Song add artist")
    # dbs = cur.execute("insert into Song(name,id,mp3,csv) values("Shape Of You","")")
    # dbs = cur.execute("drop table User")  
except:  
    myconn.rollback()  
for x in cur:  
     print(x)  
myconn.close()  